# coding: utf8

"""
负责与问题数据表交互
"""

import logging

from random import randint
from MySQLdb.cursors import DictCursor

from db.dbmanager import DBManager

from tool.util import copy_dict_by_keys, time_now_str, copy_dict_by_keys_with_new_keys
from db.util import FormatCondition, forEachPlusInsertProps, FormatUpdateStr


def query_user_question_list(username, cur_page, page_size):
    """
    查询用户问题列表
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    sql = "select *from `%s` where username='%s'" % ("tb_user", username)
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor_0.execute(sql)
    result = cursor_0.fetchone()
    cursor_0.close()
    question_list = []
    if result is None or len(result) == 0:
        return False, None, None
    identifier = result['identifier']
    grade = result['grade']
    if identifier == 0:
        # 获取总页数
        sql_0 = "select count(*) as counts from `%s` where question_grade=%s" % ("tb_question", grade)
        cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor_0.execute(sql_0)
        tmp = cursor_0.fetchone()
        cursor_0.close()
        if tmp is None or len(tmp) == 0:
            return True, question_list, 0
        counts = tmp['counts']
        sql1 = "select *from `%s` where question_grade=%s order by question_time desc limit %s, %s" % \
               ("tb_question", grade, (cur_page - 1) * page_size, page_size)
    elif identifier == 1:
        subject = result['subject']
        # 获取总页数
        sql_0 = "select count(*) as counts from `%s` where question_grade=%s and question_subject=%s" % \
                ("tb_question", grade, subject)
        cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor_0.execute(sql_0)
        tmp = cursor_0.fetchone()
        cursor_0.close()
        if tmp is None or len(tmp) == 0:
            return True, question_list, 0
        counts = tmp['counts']
        sql1 = "select *from `%s` where question_grade=%s and question_subject=%s order by question_time desc limit %s, %s" % \
               ("tb_question", grade, subject, (cur_page - 1) * page_size, page_size)
    msg0 = "[in query_user_question_list] sql1=" + sql1
    logging.info(msg0)
    cursor1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor1.execute(sql1)
    result1 = cursor1.fetchall()
    cursor1.close()
    if result1:
        for item in result1:
            # 拿到用户信息
            tmp = dict()
            tmp_username = item['question_username']
            question_id = item['question_id']
            sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", tmp_username)
            cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            cursor0.execute(sql0)
            result0 = cursor0.fetchone()
            cursor0.close()
            tmp['avatar_url'] = result0['avatar_url']
            tmp['nickname'] = result0['nickname']
            tmp.update(item)
            # 用户是否收藏过该问题
            has_collect = 0
            sql0 = "select *from `%s` where collecter_username='%s' and question_id=%s" % ("tb_question_collection",
                                                                                   username, question_id)
            cursor0 = db_manager.conn_r.cursor()
            cursor0.execute(sql0)
            result_119 = cursor0.fetchone()
            cursor0.close()
            if result_119:
                has_collect = 1
            tmp['has_collect'] = has_collect

            cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            sql0 = "select count(*) as counts from `%s` where question_id='%s'" % ("tb_answer", question_id)
            cursor0.execute(sql0)
            result0 = cursor0.fetchone()
            cursor0.close()
            counter = 0
            if result0:
                counter = result0['counts']
            tmp['answer_counts'] = counter
            question_list.append(tmp)
    db_manager.close()
    return True, question_list, counts


def post_question(username, grade, subject, question_content, question_score=0, options=None):
    """
    用户提问
    :param username: 用户名
    :param grade: 年级
    :param subject: 学科
    :param question_content: 问题内容
    :param question_score: 悬赏积分
    :param options: 可变字段
    :return:
    """
    db_manager = DBManager()
    # 判断用户是否有权限提问
    sql0 = "select *from `%s` where username='%s'" % ("tb_user", username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0 is None:
        return False
    identifier = result0['identifier']
    if identifier != 0:
        return False
    # 客户端提交的问题内容为空
    if question_content is None or question_content == '':
        # 获取随机问题内容 (随机数的上限取决于后期配置的模板表的大小)
        # 拿到模板表的大小
        template_size = 0
        sql0 = "select count(*) as counts from `%s`" % "tb_question_content_template"
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        if result0:
            template_size = result0['counts']
        if template_size < 1:
            return False
        r_index = randint(1, template_size)
        sql0 = "select *from `%s` where content_id=%s" % ("tb_question_content_template", r_index)
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        if result0:
            question_content = result0['content_value']

    # 拿到插入的数据
    props = dict()
    props['question_username'] = username
    props['question_content'] = question_content
    props['question_score'] = question_score
    props['question_grade'] = grade
    props['question_subject'] = subject
    props['question_time'] = time_now_str()
    props['question_status'] = 0

    if options:
        assert isinstance(options, dict)
        props.update(options)

    sql = forEachPlusInsertProps("tb_question", props)
    msg = "[in post_question] sql=" + sql
    logging.info(msg)
    cursor = db_manager.conn_r.cursor()
    try:
        cursor.execute(sql)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
        raise Exception
    # 提问成功, 更新积分
    # 更新用户积分
    user_operation_type = 2
    sql2 = "select score_points from `%s` where user_operation_type=%s" % ("tb_score_rule_template", user_operation_type)
    cursor2 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor2.execute(sql2)
    result2 = cursor2.fetchone()
    point_value = result2['score_points'] - question_score
    if point_value >= 0:
        sql_0 = "insert into `%s` (username, point_type, point_value) values ('%s', %s, %s) ON DUPLICATE KEY UPDATE" \
                " point_value=point_value+VALUES(point_value)" % ("tb_user_points", username, user_operation_type,
                                                                  point_value)
    else:
        # 查询是否存在记录
        sql_110 = "select *from `%s` where username='%s' and point_type=%s" % ("tb_user_points", username,
                                                                               user_operation_type)
        cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor_0.execute(sql_110)
        result_110 = cursor_0.fetchone()
        cursor_0.close()
        if result_110:
            point_value += result_110['point_value']
            sql_0 = "update `%s` set point_value=%s where username='%s' and point_type=%s" % \
                    ("tb_user_points", point_value, username, user_operation_type)
        else:
            sql_0 = "insert into `%s` (username, point_type, point_value) values ('%s', %s, %s)" % \
                    ("tb_user_points", username, user_operation_type, point_value)
    msg_110 = "[in post_question refresh user points] sql_0=" + sql_0
    logging.info(msg_110)
    try:
        cursor2 = db_manager.conn_r.cursor()
        cursor2.execute(sql_0)
        db_manager.conn_r.commit()
        cursor2.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor2.close()
        db_manager.close()
        raise Exception
        return False
    db_manager.close()
    return True


def connect_question(username, question_id):
    """
    收藏问题
    :param username: 用户名
    :param question_id: 问题ID
    :return:
    """
    db_manager = DBManager()
    # 问题是否存在
    sql0 = "select *from `%s` where question_id=%s" % ("tb_question", question_id)
    cursor0 = db_manager.conn_r.cursor()
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0 is None:
        return False, "问题不存在"
    # 查询是否收藏过该问题
    sql0 = "select *from `%s` where collecter_username='%s' and question_id=%s" % ("tb_question_collection",
                                                                                   username, question_id)
    cursor0 = db_manager.conn_r.cursor()
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0 is not None:
        return False, "已收藏过该问题"
    sql = "insert into `%s` (question_id, collecter_username, collect_time) values (%s, '%s', '%s')" % ("tb_question_collection",
                                                                                    question_id, username, time_now_str())
    msg = "[in connect_question] sql=" + sql
    logging.info(msg)
    cursor = db_manager.conn_r.cursor()
    try:
        cursor.execute(sql)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
        raise Exception
    db_manager.close()
    return True, ""


def query_collect_question_list(username, cur_page, page_size):
    """
    请求用户收藏的问题列表
    :param username: 用户名
    :param cur_page: 当前数据分页
    :param page_size: 每页显示数据条数
    :return:
    """
    db_manager = DBManager()
    question_list = []
    # 获取总页数
    sql_0 = "select count(*) as counts from `%s` where collecter_username='%s'" % ("tb_question_collection", username)
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor_0.execute(sql_0)
    tmp = cursor_0.fetchone()
    cursor_0.close()
    if tmp is None or len(tmp) == 0:
        return True, question_list, 0
    counts = tmp['counts']
    sql0 = "select *from `%s` where collecter_username='%s' order by collect_time limit %s,%s" % \
           ("tb_question_collection", username, (cur_page - 1) * page_size, page_size)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    results = cursor0.fetchall()
    cursor0.close()
    for t in results:
        # 拿到用户信息
        tmp = dict()
        tmp_username = t['collecter_username']
        sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", tmp_username)
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        tmp['avatar_url'] = result0['avatar_url']
        tmp['nickname'] = result0['nickname']

        # 拿到问题信息
        tmp_question_id = t['question_id']
        sql0 = "select *from `%s` where question_id=%s" % ("tb_question", tmp_question_id)
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        if result0 is None:
            continue
        tmp.update(result0)

        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        sql0 = "select count(*) as counts from `%s` where question_id=%s" % ("tb_answer", tmp_question_id)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        counter = 0
        if result0:
            counter = result0['counts']
        tmp['has_collect'] = 1
        tmp['answer_counts'] = counter
        question_list.append(tmp)
    db_manager.close()
    return True, question_list, counts


def query_user_question_or_answer_list(username, identifier, is_part, cur_page, page_size):
    """
    请求用户的问题列表或者回答列表
    :param username: 用户名
    :param identifier: 身份标志 (0: 学生 1: 教师)
    :param is_part: 按照条件搜索 (学生: 问题完成数 教师： 回答采纳数)
    :param cur_page: 当前数据分页
    :param page_size: 每页显示数据条数
    :return:
    """
    db_manager = DBManager()
    order_key = 'question_time'
    table_name = 'tb_question'
    question_list = []
    counts = 0
    # 学生
    if identifier == 0:
        # 全部搜索
        if is_part == 0:
            query_str = FormatCondition(props={
                "question_username": username
            })
        # 部分搜索
        elif is_part == 1:
            query_str = FormatCondition(props={
                "question_username": username,
                "question_status": 1
            })
        # 拿到总条数
        sql = "select count(*) as counts from `%s` where %s" % (table_name, query_str)
        cursor = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        if result is None or len(result) == 0:
            return True, question_list, 0
        counts = result['counts']
        sql0 = "select *from `%s` where %s order by %s limit %s,%s" % \
               (table_name, query_str, order_key, (cur_page - 1) * page_size, page_size)
    # 教师
    elif identifier == 1:
        # 全部搜索
        if is_part == 0:
            query_str = FormatCondition(props={
                "answer_username": username
            })
        # 部分搜索
        elif is_part == 1:
            query_str = FormatCondition(props={
                "answer_username": username,
                "is_accepted": 1
            })
        # 拿到总条数
        sql = "select count(question_id) as counts from `tb_answer` where %s and question_id not in (select ask_question_id from " \
              "`tb_ask` where be_asked_username='%s')" % (query_str, username)
        cursor = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        if result is None or len(result) == 0:
            return True, question_list, 0
        counts = result['counts']
        sql0 = "select *from `%s` where question_id in (select question_id from `tb_answer` where " \
               "%s and question_id not in (select ask_question_id from `tb_ask` where be_asked_username='%s')) order by " \
               "%s limit %s,%s" % (table_name, query_str, username, order_key, (cur_page - 1) * page_size,
                                        page_size)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    results = cursor0.fetchall()
    cursor0.close()
    for t in results:
        # 拿到用户信息
        tmp = dict()
        tmp_username = t['question_username']
        tmp_question_id = t['question_id']
        sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", tmp_username)
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        tmp['avatar_url'] = result0['avatar_url']
        tmp['nickname'] = result0['nickname']

        # 用户是否收藏过该问题
        has_collect = 0
        sql0 = "select *from `%s` where collecter_username='%s' and question_id=%s" % ("tb_question_collection",
                                                                                       username, tmp_question_id)
        cursor0 = db_manager.conn_r.cursor()
        cursor0.execute(sql0)
        result_120 = cursor0.fetchone()
        cursor0.close()
        if result_120:
            has_collect = 1
        tmp['has_collect'] = has_collect

        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        sql0 = "select count(*) as counts from `%s` where question_id=%s" % ("tb_answer", tmp_question_id)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        counter = 0
        if result0:
            counter = result0['counts']
        tmp['answer_counts'] = counter
        question_list.append(tmp)
    db_manager.close()
    return True, question_list, counts


def search_question(username, question_content, cur_page, page_size, grade=None, subject=None):
    """
    搜索问题 (按照问题内容搜索)
    :param username: 用户名
    :param question_content: 问题内容
    :param grade: 年级
    :param subject: 科目
    :return:
    """
    db_manager = DBManager()
    question_list = []
    condition_props = dict()
    if grade is not None:
        condition_props['question_grade'] = grade
    if subject is not None:
        condition_props['question_subject'] = subject
    # 默认搜索文字
    con_str = FormatCondition(condition_props)
    # 拿到总条数
    signal = False
    if con_str is not None and len(con_str) > 0:
        signal = True
        sql_1 = "select count(*) as counts from `%s` where %s and question_content like '%s%s%s'" % \
                ("tb_question", con_str, '%', question_content, '%')
    else:
        sql_1 = "select count(*) as counts from `%s` where question_content like '%s%s%s'" % \
                ("tb_question", '%', question_content, '%')
    msg0 = "[in search_question] sql_1=" + sql_1
    logging.info(msg0)
    cursor_1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor_1.execute(sql_1)
    tmp = cursor_1.fetchone()
    cursor_1.close()
    if tmp is None or len(tmp) == 0:
        return True, question_list, 0
    counts = tmp['counts']
    if signal:
        sql = "select *from `%s` where %s and question_content like '%s%s%s' order by question_time desc limit %s,%s " % \
              ("tb_question", con_str, '%', question_content, '%', (cur_page - 1) * page_size, page_size)
    else:
        sql = "select *from `%s` where question_content like '%s%s%s' order by question_time desc limit %s,%s " % \
              ("tb_question", '%', question_content, '%', (cur_page - 1) * page_size, page_size)
    msg = '[in search_question] sql=' + sql
    logging.info(msg)
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor_0.execute(sql)
    result = cursor_0.fetchall()
    cursor_0.close()
    logging.info(result)
    if result:
        for item in result:
            tmp = item.copy()
            question_id = item['question_id']
            tmp_username = item['question_username']
            # 拿到用户信息
            sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", tmp_username)
            cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            cursor0.execute(sql0)
            result0 = cursor0.fetchone()
            cursor0.close()
            tmp['avatar_url'] = result0['avatar_url']
            tmp['nickname'] = result0['nickname']

            # 用户是否收藏过该问题
            has_collect = 0
            sql0 = "select *from `%s` where collecter_username='%s' and question_id=%s" % ("tb_question_collection",
                                                                                   username, question_id)
            cursor0 = db_manager.conn_r.cursor()
            cursor0.execute(sql0)
            result_121 = cursor0.fetchone()
            cursor0.close()
            if result_121:
                has_collect = 1
            tmp['has_collect'] = has_collect

            cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            sql0 = "select count(*) as counts from `%s` where question_id=%s" % ("tb_answer", question_id)
            cursor0.execute(sql0)
            result0 = cursor0.fetchone()
            cursor0.close()
            counter = 0
            if result0:
                counter = result0['counts']
            tmp['answer_counts'] = counter
            question_list.append(tmp)
    db_manager.close()
    return True, question_list, counts


def answer_question(username, question_id, answer_content, is_original_answer, options=None):
    """
    回答问题
    :param username: 用户名
    :param question_id: 问题ID
    :param answer_content: 回答内容
    :param is_original_answer: 是否是原回答(1: 原回答 0: 追答)
    :return:
    """
    db_manager = DBManager()
    # 判断用户是否有权限回答问题
    sql0 = "select *from `%s` where username='%s'" % ("tb_user", username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0 is None:
        return False, "用户不存在"
    identifier = result0['identifier']
    if identifier != 1:
        return False, "没有回答权限"
    original_question_id = question_id
    # 如果是追答
    if is_original_answer == 0:
        # 拿到问题原始ID
        sql_0 = "select original_question_id from `%s` where ask_question_id=%s" % ("tb_ask", question_id)
        cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor_0.execute(sql_0)
        result_0 = cursor_0.fetchone()
        cursor_0.close()
        if result_0 is None:
            return False, "问题不存在"
        original_question_id = result_0['original_question_id']
    # 问题是否已经被解决
    sql_0 = "select question_status from `%s` where question_id=%s" % ("tb_question", original_question_id)
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor_0.execute(sql_0)
    result_0 = cursor_0.fetchone()
    cursor_0.close()
    if result_0 is None:
        return False, "问题不存在"
    question_status = result_0['question_status']
    # 问题已经被解决
    if question_status == 1:
        return False, "问题已经被解决"

    props = dict()
    props['answer_username'] = username
    props['answer_time'] = time_now_str()
    props['question_id'] = question_id
    props['is_accepted'] = 0
    props['answer_content'] = answer_content

    if options:
        assert isinstance(options, dict)
        props.update(options)

    sql = forEachPlusInsertProps("tb_answer", props)
    msg = "[in answer_question] sql=" + sql
    logging.info(msg)
    cursor = db_manager.conn_r.cursor()
    try:
        cursor.execute(sql)
        db_manager.conn_r.commit()
        cursor.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor.close()
        db_manager.close()
        raise Exception
    # 更新用户积分 (只有原始问题的回答加分, 追答不加分)
    if is_original_answer == 1:
        user_operation_type = 4
        sql2 = "select score_points from `%s` where user_operation_type=%s" % ("tb_score_rule_template", user_operation_type)
        cursor2 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor2.execute(sql2)
        result2 = cursor2.fetchone()
        point_value = result2['score_points']
        sql_0 = "insert into `%s` (username, point_type, point_value) values ('%s', %s, %s) ON DUPLICATE KEY UPDATE" \
                " point_value=point_value+VALUES(point_value)" % ("tb_user_points", username, user_operation_type,
                                                                  point_value)
        msg_110 = "[in answer_question refresh user points] sql_0=" + sql_0
        logging.info(msg_110)
        try:
            cursor2 = db_manager.conn_r.cursor()
            cursor2.execute(sql_0)
            db_manager.conn_r.commit()
            cursor2.close()
        except Exception:
            db_manager.conn_r.rollback()
            cursor2.close()
            db_manager.close()
            raise Exception
            return False
    db_manager.close()
    return True, "回答成功"


def query_user_question_detail(username, question_id):
    """
    请求用户的问题详情
    :param username: 用户名
    :param question_id: 问题ID
    :return:
    """
    db_manager = DBManager()
    sql0 = "SELECT tq.question_id, question_username, avatar_url, nickname, question_grade, question_subject, " \
           "question_content, question_pic_url, question_sound_url, question_time, question_status, question_score from `tb_question` as tq inner join `tb_user` as tu on " \
           "tq.question_username=tu.username and tq.question_id=%s and tq.question_username='%s';" % (question_id,
                                                                                                      username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    # 没有该问题
    if result0 is None or len(result0) == 0:
        return False, None
    data = dict()
    answer_list = []
    # 用户是否收藏过该问题
    has_collect = 0
    sql0 = "select *from `%s` where collecter_username='%s' and question_id=%s" % ("tb_question_collection",
                                                                                   username, question_id)
    cursor0 = db_manager.conn_r.cursor()
    cursor0.execute(sql0)
    result_110 = cursor0.fetchone()
    cursor0.close()
    if result_110:
        has_collect = 1
    result0['has_collect'] = has_collect
    sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result_150 = cursor0.fetchone()
    cursor0.close()

    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    sql0 = "select count(*) as counts from `%s` where question_id=%s" % ("tb_answer", question_id)
    cursor0.execute(sql0)
    result_1000 = cursor0.fetchone()
    cursor0.close()
    counter = 0
    if result_1000:
        counter = result_1000['counts']
    result0['answer_counts'] = counter

    result0['avatar_url'] = result_150['avatar_url']
    result0['nickname'] = result_150['nickname']

    data['question_info'] = result0
    data['answers_info'] = answer_list
    # 找出回答列表(根据回答时间排序)
    sql1 = "select *from `tb_answer` where question_id=%s order by answer_time" % question_id
    msg0 = "[in query_user_question_detail] sql1=" + sql1
    logging.info(msg0)
    cursor1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor1.execute(sql1)
    answers = cursor1.fetchall()
    cursor1.close()
    # 没有回答
    if answers is None or len(answers) == 0:
        return True, data
    for a_answer in answers:
        t_username = a_answer['answer_username']
        # 添加回答信息
        tmp_dict = a_answer.copy()
        # 拿到回答者信息
        sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", t_username)
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        tmp_dict['avatar_url'] = result0['avatar_url']
        tmp_dict['nickname'] = result0['nickname']
        # 是否有追问
        sql2 = "select *from (select *from `tb_ask` where be_asked_username='%s' and original_question_id=%s and answer_id=%s) as ta left join `tb_answer` as tb on ta.ask_question_id=" \
               "tb.question_id and ta.be_asked_username=tb.answer_username" % (t_username, question_id,
                                                                               a_answer['answer_id'])
        cursor2 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor2.execute(sql2)
        results = cursor2.fetchall()
        cursor2.close()
        if results is None or len(results) == 0:
            # 没有追问
            tmp_dict['counts'] = 1
            answer_list.append(tmp_dict)
            continue
        counts = 0
        ask_question_id = 0
        for t in results:
            tmp_ask_question_id = t['ask_question_id']
            if ask_question_id != tmp_ask_question_id:
                counts += 1
                ask_question_id = tmp_ask_question_id
            # 是否有回答
            if t['question_id']:
                counts += 1
        tmp_dict['counts'] = counts
        answer_list.append(tmp_dict)
    db_manager.close()
    return True, data


def ask_question(username, answer_id, ask_content, original_question_id, be_asked_username, options=None):
    """
    用户追问
    :param username: 用户名
    :param answer_id: 回答的ID
    :param ask_content: 追问内容
    :param original_question_id: 原问题ID
    :param be_asked_username: 被追问的用户
    :return:
    """
    db_manager = DBManager()
    # 问题是否已经被解决
    sql_0 = "select question_status from `%s` where question_id=%s" % ("tb_question", original_question_id)
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor_0.execute(sql_0)
    result_0 = cursor_0.fetchone()
    cursor_0.close()
    if result_0 is None:
        return False, "问题不存在"
    question_status = result_0['question_status']
    # 问题已经被解决
    if question_status == 1:
        return False, "问题已经被解决"
    # 检验被提问的用户是否回答过该问题
    sql_0 = "select *from `tb_answer` where answer_username='%s' and question_id=%s" % (be_asked_username,
                                                                                        original_question_id)
    cursor_0 = db_manager.conn_r.cursor()
    cursor_0.execute(sql_0)
    result_0 = cursor_0.fetchone()
    cursor_0.close()
    if result_0 is None or len(result_0) == 0:
        return False, "没有回答该问题"

    # 拿到追问顺序ask_order
    sql_1 = "select max(ask_order) as ask_order0 from `tb_ask` where be_asked_username='%s' and original_question_id=" \
            "%s" % (be_asked_username, original_question_id)
    cursor_1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor_1.execute(sql_1)
    result_1 = cursor_1.fetchone()
    cursor_1.close()
    if result_1 is None or len(result_1) == 0:
        ask_order = 0
    else:
        ask_order = result_1['ask_order0'] if result_1['ask_order0'] else 0
    # 添加一条追问记录
    props = dict()
    props['ask_content'] = ask_content
    props['ask_time'] = time_now_str()
    props['original_question_id'] = original_question_id
    props['be_asked_username'] = be_asked_username
    props['ask_order'] = ask_order + 1
    props['answer_id'] = answer_id

    if options:
        assert isinstance(options, dict)
        props.update(options)

    insert_sql = forEachPlusInsertProps("tb_ask", props)
    msg0 = "[in ask_question] insert_sql=" + insert_sql
    logging.info(msg0)
    cursor_2 = db_manager.conn_r.cursor()
    try:
        cursor_2.execute(insert_sql)
        db_manager.conn_r.commit()
        cursor_2.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor_2.close()
        db_manager.close()
        raise Exception
    db_manager.close()
    return True, ""


def adopt_answer(username, question_id, answer_id, answer_username):
    """
    采纳回答
    :param username: 用户名
    :param question_id: 原问题ID
    :param answer_id: 回答的ID
    :param answer_username: 回答者的用户名
    :return:
    """
    db_manager = DBManager()
    # 判断用户是否有权限采纳答案
    sql0 = "select *from `%s` where username='%s'" % ("tb_user", username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0 is None:
        return False, "用户不存在"
    identifier = result0['identifier']
    if identifier != 0:
        return False, "没有采纳权限"
    # 问题是否已经被解决
    sql_0 = "select question_status, question_score from `%s` where question_id=%s" % ("tb_question", question_id)
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor_0.execute(sql_0)
    result_0 = cursor_0.fetchone()
    cursor_0.close()
    if result_0 is None:
        return False, "问题不存在"
    question_status = result_0['question_status']
    question_score = result_0['question_score']
    # 问题已经被解决
    if question_status == 1:
        return False, "问题已经被解决"
    # 关闭问题
    update_prop = dict()
    update_prop['question_status'] = 1
    update_sql_0 = FormatUpdateStr(update_prop)
    sql0 = "update `%s` set %s where question_id=%s" % ("tb_question", update_sql_0, question_id)
    cursor0 = db_manager.conn_r.cursor()
    try:
        cursor0.execute(sql0)
        db_manager.conn_r.commit()
        cursor0.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor0.close()
        db_manager.close()
        raise Exception
        return False
    # 更新回答的状态
    update_prop = dict()
    update_prop['is_accepted'] = 1
    update_sql_0 = FormatUpdateStr(update_prop)
    sql0 = "update `%s` set %s where answer_id=%s" % ("tb_answer", update_sql_0, answer_id)
    cursor0 = db_manager.conn_r.cursor()
    try:
        cursor0.execute(sql0)
        db_manager.conn_r.commit()
        cursor0.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor0.close()
        db_manager.close()
        raise Exception
        return False
    # 更新教师积分
    user_operation_type = 3
    sql2 = "select score_points from `%s` where user_operation_type=%s" % ("tb_score_rule_template", user_operation_type)
    cursor2 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor2.execute(sql2)
    result2 = cursor2.fetchone()
    cursor2.close()
    point_value = result2['score_points'] + question_score
    sql_0 = "insert into `%s` (username, point_type, point_value) values ('%s', %s, %s) ON DUPLICATE KEY UPDATE" \
            " point_value=point_value+VALUES(point_value)" % ("tb_user_points", answer_username, user_operation_type,
                                                              point_value)
    msg_120 = "[in adopt_answer fresh_user_points] sql_0=" + sql_0
    logging.info(msg_120)
    cursor2 = db_manager.conn_r.cursor()
    try:
        cursor2.execute(sql_0)
        db_manager.conn_r.commit()
        cursor2.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor2.close()
        db_manager.close()
        raise Exception
        return False
    db_manager.close()
    return True, ""


def query_ask_and_answer_page(answer_id):
    """
    获取某个问题的追问追答列表
    :param answer_id: 回答的ID
    :return:
    """
    db_manager = DBManager()
    sql0 = "select *from `tb_answer` where answer_id=%s" % answer_id
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    answer = cursor0.fetchone()
    cursor0.close()
    if answer is None or len(answer) == 0:
        return False, "没有该回答"
    # 拿到问题信息
    question_id = answer['question_id']
    sql0 = "select *from `tb_question` where question_id=%s" % question_id
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    data = dict()
    answer_list = []
    question_username = result0['question_username']

    # 用户是否收藏过该问题
    has_collect = 0
    sql0 = "select *from `%s` where collecter_username='%s' and question_id=%s" % ("tb_question_collection",
                                                                                   question_username, question_id)
    cursor0 = db_manager.conn_r.cursor()
    cursor0.execute(sql0)
    result_112 = cursor0.fetchone()
    cursor0.close()
    if result_112:
        has_collect = 1
    result0['has_collect'] = has_collect
    # 拿到提问者的信息
    sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", question_username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result_150 = cursor0.fetchone()
    cursor0.close()
    result0['avatar_url'] = result_150['avatar_url']
    result0['nickname'] = result_150['nickname']

    data['question_info'] = result0
    data['answers_info'] = answer_list

    t_username = answer['answer_username']
    # 添加回答信息
    tmp_dict = answer.copy()
    # 拿到回答者信息
    sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", t_username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    tmp_dict['avatar_url'] = result0['avatar_url']
    tmp_dict['nickname'] = result0['nickname']
    # 原始问题的回答
    tmp_dict['type'] = 0
    answer_list.append(tmp_dict)

    # 是否有追问
    sql2 = "select *from (select *from `tb_ask` where be_asked_username='%s' and original_question_id=%s and answer_id=%s) as ta left join `tb_answer` as tb on ta.ask_question_id=" \
           "tb.question_id and ta.be_asked_username=tb.answer_username " % (t_username, question_id, answer_id)
    cursor2 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor2.execute(sql2)
    results = cursor2.fetchall()
    cursor2.close()
    if results is None or len(results) == 0:
        return True, data

    # 去重
    ask_question_id = 0
    need_sort_list = []
    # 记录需要排序的数据段
    start_index = 1
    end_index = 1
    for t in results:
        tmp_ask_dict = dict()
        tmp_ask_question_id = t['ask_question_id']
        # logging.info("ZZZ###")
        # msg = str(tmp_ask_question_id) + "," + str(t['ask_question_id']) + ", " + str(start_index) + "," + str(end_index)
        # logging.info(msg)
        # 拿到追问者的信息
        if ask_question_id != tmp_ask_question_id:
            # 更新游标
            ask_question_id = tmp_ask_question_id
            # 记录需要排序的数据区间
            if end_index - start_index >= 1:
                t_list = [start_index, end_index]
                need_sort_list.append(t_list)
            end_index += 1
            start_index = end_index
            # 拿到提问者的信息
            tmp_ask_dict['avatar_url'] = result_150['avatar_url']
            tmp_ask_dict['nickname'] = result_150['nickname']
            # 追问
            tmp_ask_dict['type'] = 1
            old_keys = ['answer_id', 'be_asked_username', 'ask_time', 'ask_question_id', 'ask_content',
                        'ask_pic_url', 'ask_sound_url']
            new_keys = ["answer_id", "answer_username", "answer_time", "question_id", "answer_content",
                        "answer_pic_url", "answer_sound_url"]
            tmp_ask_dict['is_accepted'] = 0
            copy_dict_by_keys_with_new_keys(old_keys, new_keys, t, tmp_ask_dict)
            answer_list.append(tmp_ask_dict)
        else:
            # 处理多个追答的情形
            end_index += 1
        if t['question_id'] is None:
            if end_index - start_index >= 1:
                need_sort_list.append([start_index, end_index])
            start_index = end_index
        else:
            tmp_answer_dict = dict()
            # 拿到回答者的信息
            tmp_username = t['answer_username']
            sql0 = "select avatar_url, nickname from `%s` where username='%s'" % ("tb_user", tmp_username)
            cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            cursor0.execute(sql0)
            result0 = cursor0.fetchone()
            cursor0.close()
            tmp_answer_dict['avatar_url'] = result0['avatar_url']
            tmp_answer_dict['nickname'] = result0['nickname']
            # 追答
            tmp_answer_dict['type'] = 2
            copy_dict_by_keys(['answer_username', 'answer_time', 'question_id', 'is_accepted', 'answer_content',
                               'answer_pic_url', 'answer_sound_url', 'answer_id'], t, tmp_answer_dict)
            answer_list.append(tmp_answer_dict)
    if end_index - start_index >= 1:
        need_sort_list.append([start_index, end_index])
    # logging.info('########start')
    # logging.info(answer_list)
    # 进行数据排序 (维度选择answer_time)
    if need_sort_list and answer_list:
        # logging.info('to sort')
        logging.info(need_sort_list)
        for v in need_sort_list:
            # logging.info("hhhh")
            # logging.info(v)
            for i in xrange(v[0], v[1]):
                for j in xrange(v[0], v[1]-i):
                    if answer_list[j]['answer_time'] > answer_list[j+1]['answer_time']:
                        # test swap
                        # logging.info("before swap####")
                        t_data = answer_list[j+1]
                        logging.info(t_data)
                        answer_list[j+1] = answer_list[j]
                        answer_list[j] = t_data
                        logging.info(answer_list[j+1])
    # logging.info('########end')
    logging.info(answer_list)
    db_manager.close()
    return True, data


def get_latest_id(table_name):
    """
    根据用户名获取数据表对应主键ID
    :param table_name: 数据表名
    :return:
    """
    db_manager = DBManager()
    sql1 = "SELECT Auto_increment FROM information_schema.tables WHERE table_schema = 'Question_Answer_Platform' " \
           "and table_name='%s'" % table_name
    msg = "[in get_latest_id(dbQuestion)] sql1=" + sql1
    logging.info(msg)
    cursor1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor1.execute(sql1)
    result1 = cursor1.fetchone()
    cursor1.close()
    db_manager.close()
    return result1['Auto_increment']

