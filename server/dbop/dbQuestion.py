# coding: utf8

"""
负责与问题数据表交互
"""

from datetime import datetime
from random import randint
from MySQLdb.cursors import DictCursor

from db.dbmanager import DBManager


def query_user_question_list(username):
    """
    查询用户问题列表
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    sql = "select *from `%s` where username='%s'" % ("tb_user", username)
    cursor = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    question_list = []
    if result is None or len(result) == 0:
        return question_list
    identifier = result['identifier']
    grade = result['grade']
    if identifier == 0:
        sql1 = "select *from `%s` where question_grade='%s' order by question_time desc" % ("tb_question", grade)
    elif identifier == 1:
        subject = result['subject']
        sql1 = "select *from `%s` where question_grade='%s' and question_subject = '%s' order by question_time desc" % \
               ("tb_question", username, subject)
    cursor1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor1.execute(sql1)
    result1 = cursor1.fetchall()
    cursor1.close()
    if result1:
        for item in result1:
            tmp = item.copy()
            question_id = item['question_id']
            cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            sql0 = "select count(*) from `%s` where question_id='%s'" % ("tb_answer", question_id)
            cursor0.execute(sql0)
            result0 = cursor0.fetchone()
            cursor0.close()
            counter = 0
            if result0:
                counter = result0[0][0]
            tmp['answer_counts'] = counter
            question_list.append(tmp)
    db_manager.close()
    return question_list


def post_question(username, grade, subject, content_type, question_content, question_score=0):
    """
    用户提问
    :param username: 用户名
    :param grade: 年级
    :param subject: 学科
    :param content_type: 问题内容类型
    :param question_content: 问题内容
    :param question_score: 悬赏积分
    :return:
    """
    db_manager = DBManager()
    header_id = 0
    # 获取随机问题头部 (随机数的上限取决于后期配置的模板表的大小)
    r_index = randint(0, 0)
    if r_index > 0:
        sql0 = "select *from `%s` where id='%s'" % ("tb_question_header_template", r_index)
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        if result0:
            header_id = result0['header_id']
    sql = "insert into `%s` (question_username, question_head, content_type, question_content, question_score, " \
          "question_grade, question_subject, question_time, question_status) values ('%s', '%s', '%s', '%s', '%s', " \
          "'%s', '%s', '%s', '%s')" % ("tb_question", username, header_id, content_type, question_content,
                                       question_score, grade, subject, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 0)
    cursor = db_manager.conn_r.cursor()
    try:
        cursor.execute(sql)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
        raise Exception
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
    # 查询是否收藏过该问题
    sql0 = "select *from `%s` where collector_username='%s' and question_id='%s'" % ("tb_question_collection",
                                                                                     username, question_id)
    cursor0 = db_manager.conn_r.cursor()
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0 is not None:
        return False
    sql = "insert into `%s` (question_id, collector_username) values ('%s', '%s')" % ("tb_question_collection",
                                                                                      question_id, username)
    cursor = db_manager.conn_r.cursor()
    try:
        cursor.execute(sql)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
        raise Exception
    db_manager.close()
    return True


def search_question(username, question_content):
    """
    搜索问题 (按照问题内容搜索)
    :param username: 用户名
    :param question_content: 问题内容
    :return:
    """
    db_manager = DBManager()
    question_list = []
    # 默认搜索文字
    sql = "select *from `%s` where content_type='%s' and question_content like '%s' order by question_time desc" % \
          ("tb_question", 1, question_content)
    cursor = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    if result:
        for item in result:
            tmp = item.copy()
            question_id = item['question_id']
            cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            sql0 = "select count(*) as counts from `%s` where question_id='%s'" % ("tb_answer", question_id)
            cursor0.execute(sql0)
            result0 = cursor0.fetchone()
            cursor0.close()
            counter = 0
            if result0:
                print 'zzz###', result0, type(result0)
                counter = result0['counts']
            tmp['answer_counts'] = counter
            question_list.append(tmp)
    db_manager.close()
    return question_list


def answer_question(username, question_id, content_type, answer_content):
    """
    回答问题
    :param username: 用户名
    :param question_id: 问题ID
    :param content_type: 回答内容类型
    :param answer_content: 回答内容
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
        return False
    identifier = result0['identifier']
    if identifier != 1:
        return False
    sql = "insert into `%s` (answer_username, answer_time, question_id, is_accepted, answer_content, content_type) " \
          "values ('%s', '%s', '%s', '%s', '%s', '%s')" % ("tb_answer", username,
                                                           datetime.now().strftime('%Y-%m-%d %H:%M:%S'), question_id,
                                                           0, answer_content, content_type)
    cursor = db_manager.conn_r.cursor()
    cursor.execute(sql)
    try:
        cursor.execute(sql)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
        raise Exception
    db_manager.close()
    return True
