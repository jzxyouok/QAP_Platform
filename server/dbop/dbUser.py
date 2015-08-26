# coding: utf8

"""
负责与用户数据表交互
"""

import logging

import hashlib
from MySQLdb.cursors import DictCursor

from db.dbmanager import DBManager
from db.util import forEachPlusInsertProps, forEachUpdateProps, FormatUpdateStr
from tool.util import string_toDatetime, time_now_str


def login(username, password, identifier):
    """
    用户登录 (学生, 教师登录入口)
    :param username: 用户名
    :param password: 密码
    :return:
    """
    password = hashlib.sha224(password).hexdigest()
    db_manager = DBManager()
    sql = "select *from `tb_account` as ta inner join `tb_user` as tu on ta.username=tu.username and ta.username='%s'" \
          " and ta.password='%s' and tu.identifier=%s" % (username, password, identifier)
    cursor_0 = db_manager.conn_r.cursor()
    cursor_0.execute(sql)
    result = cursor_0.fetchone()
    cursor_0.close()
    is_ok = False
    data = None
    if result:
        # 是否为新用户登录
        is_new_user = False
        sql = "select *from `%s` where username='%s'" % ("tb_user_log", username)
        cursor_0 = db_manager.conn_r.cursor()
        cursor_0.execute(sql)
        result_0 = cursor_0.fetchone()
        cursor_0.close()
        if result_0 is None:
            is_new_user = True
        cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
        sql0 = "select *from `%s` where username='%s'" % ("tb_user", username)
        cursor0.execute(sql0)
        result0 = cursor0.fetchone()
        cursor0.close()
        is_ok = True
        data = result0
        # 拿到签到数据
        sql1 = "select *from `%s` where username='%s' and to_days(sign_time)=to_days(now())" % ("tb_sign", username)
        cursor1 = db_manager.conn_r.cursor()
        cursor1.execute(sql1)
        result1 = cursor1.fetchone()
        cursor1.close()
        has_sign_today = 0
        if result1 is not None:
            has_sign_today = 1
        data['has_sign_today'] = has_sign_today
        # 如果是新用户登录, 更新积分
        if is_new_user:
            user_operation_type = 1
            sql2 = "select score_points from `%s` where user_operation_type=%s" % ("tb_score_rule_template",
                                                                                   user_operation_type)
            cursor2 = db_manager.conn_r.cursor(cursorclass=DictCursor)
            cursor2.execute(sql2)
            result2 = cursor2.fetchone()
            point_value = result2['score_points']
            sql_0 = "insert into `%s` (username, point_type, point_value) values ('%s', %s, %s) ON DUPLICATE KEY UPDATE" \
                    " point_value=point_value+VALUES(point_value)" % ("tb_user_points", username, user_operation_type,
                                                                      point_value)
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
        # 记录用户登录日志
        sql_0 = "insert into `%s` (username, login_time) values ('%s', '%s') ON DUPLICATE KEY UPDATE" \
            " login_time=login_time" % ("tb_user_log", username, time_now_str())
        cursor1 = db_manager.conn_r.cursor()
        try:
            cursor1.execute(sql_0)
            db_manager.conn_r.commit()
            cursor1.close()
        except Exception:
            db_manager.conn_r.rollback()
            cursor1.close()
            db_manager.close()
            raise Exception
    db_manager.close()
    return is_ok, data


def register(username, password, grade, identifier, nickname, subject, serial_number, options=None):
    """
    用户注册 (用户获取登录账户的唯一途径)
    1. 学生注册: username, password, grade为必填项, invitation_code为选填项
    2. 教师注册: username, password, grade, subject, serial_number为必填项
    :param username: 用户名 (需要检查唯一性)
    :param password: 密码
    :param grade: 年级
    :param identifier: 用户类型 (0: 学生 1: 教师)
    :param subject: 科目 (教师才有该选项)
    :param serial_number: 教师证 (教师才有)
    :param options: 可变参数 (由user_type决定)
    :return:
    """
    db_manager = DBManager()
    cursor_0 = db_manager.conn_r.cursor()
    # 判断用户名是否存在
    sql = "select * from `%s` where username='%s'" % ("tb_account", username)
    cursor_0.execute(sql)
    result = cursor_0.fetchone()
    cursor_0.close()
    if result:
        db_manager.close()
        return False

    # 键值对
    prop_dict = dict()
    prop_dict['username'] = username
    prop_dict['identifier'] = identifier
    prop_dict['grade'] = grade
    prop_dict['nickname'] = nickname
    if subject is not None:
        prop_dict['subject'] = subject
    if serial_number is not None:
        prop_dict['serial_number'] = serial_number
    if options:
        assert isinstance(options, dict)
        prop_dict.update(options)
    insert_sql = forEachPlusInsertProps('tb_user', prop_dict)
    msg0 = "[in register] insert_sql=" + insert_sql
    logging.info(msg0)
    cursor1 = db_manager.conn_r.cursor()
    try:
        cursor1.execute(insert_sql)
        db_manager.conn_r.commit()
        cursor1.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor1.close()
        db_manager.close()
        raise Exception

    password = hashlib.sha224(password).hexdigest()
    sql0 = "insert into `%s` (%s, %s) values ('%s', '%s')" % ("tb_account", "username", "password", username, password)
    msg = "[in register] sql=" + sql0
    logging.info(msg)
    cursor0 = db_manager.conn_r.cursor()
    try:
        cursor0.execute(sql0)
        db_manager.conn_r.commit()
        cursor0.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor0.close()
        db_manager.close()
    db_manager.close()
    return True


def change_password(username, old_password, new_password):
    """
    修改密码
    :param username: 用户名
    :param old_password: 旧密码
    :param new_password: 新密码
    :return:
    """
    db_manager = DBManager()
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    # 判断用户是否合法
    sql = "select password from `%s` where username='%s'" % ("tb_account", username)
    cursor_0.execute(sql)
    result = cursor_0.fetchone()
    cursor_0.close()
    if result is None:
        return False, "用户不存在"
    tmp_password = result['password']
    password = hashlib.sha224(old_password).hexdigest()
    if tmp_password != password:
        return False, "原密码错误"
    props = dict()
    prere = dict()
    props['password'] = hashlib.sha224(new_password).hexdigest()
    prere['username'] = username
    sql0 = forEachUpdateProps("tb_account", props, prere)
    try:
        cursor0 = db_manager.conn_r.cursor()
        cursor0.execute(sql0)
        db_manager.conn_r.commit()
    except Exception:
        db_manager.conn_r.rollback()
        cursor0.close()
        db_manager.close()
        raise Exception
    db_manager.close()
    return True, "修改密码成功"


def about_us(username):
    """
    关于我们
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    sql = "select content from `%s`" % "tb_about_us_template"
    cursor_0.execute(sql)
    result = cursor_0.fetchone()
    cursor_0.close()
    db_manager.close()
    if result is None:
        return False, ""
    return True, result


def feedback(username, content, feed_time):
    """
    意见反馈
    :param username: 用户名
    :param content: 反馈内容
    :param feed_time: 提交反馈的时间
    :return:
    """
    db_manager = DBManager()
    props = dict()
    props['username'] = username
    props['content'] = content
    props['feed_time'] = feed_time
    sql = forEachPlusInsertProps("tb_feedback", props)
    try:
        cursor_0 = db_manager.conn_r.cursor()
        cursor_0.execute(sql)
        db_manager.conn_r.commit()
        cursor_0.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor_0.close()
        db_manager.close()
        raise Exception
        return False
    return True


def sign_up(username, sign_time):
    """
    每日签到
    :param username: 用户名
    :param sign_time: 签到时间
    :return:
    """
    db_manager = DBManager()
    # 验证用户当天是否已经签到过
    sql0 = "select *from `%s` where username='%s' and to_days(sign_time)=to_days('%s')" % ("tb_sign", username,
                                                                                           string_toDatetime(sign_time))
    cursor0 = db_manager.conn_r.cursor()
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0 is not None:
        return False, "今天已签到过", None

    props = dict()
    props['username'] = username
    props['sign_time'] = sign_time
    sql1 = forEachPlusInsertProps("tb_sign", props)
    try:
        cursor1 = db_manager.conn_r.cursor()
        cursor1.execute(sql1)
        db_manager.conn_r.commit()
        cursor1.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor1.close()
        db_manager.close()
        raise Exception
        return False, "签到失败", None
    # 获取系统赠送的积分
    user_operation_type = 6
    sql2 = "select score_points from `%s` where user_operation_type=%s" % ("tb_score_rule_template", user_operation_type)
    cursor2 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor2.execute(sql2)
    result2 = cursor2.fetchone()
    point_value = result2['score_points']
    sql_0 = "insert into `%s` (username, point_type, point_value) values ('%s', %s, %s) ON DUPLICATE KEY UPDATE" \
            " point_value=point_value+VALUES(point_value)" % ("tb_user_points", username, user_operation_type,
                                                              point_value)
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
        return False, "签到失败", None
    db_manager.close()
    msg0 = "[in sign_up] sql_0=" + sql_0
    logging.info(msg0)
    return True, "签到成功", point_value


def query_user_points_detail(username):
    """
    请求用户积分详情
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    # 拿到模板数据
    sql0 = "select *from `%s` where username='%s'" % ("tb_user", username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0 is None or len(result0) == 0:
        return False, None
    identifier = result0['identifier']
    if identifier == 0:
        score_rule_list = [1, 2, 6, 7]
    elif identifier == 1:
        score_rule_list = [3, 4, 6, 7]
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    sql = "select user_operation_type, user_operation_desc, point_value from `%s` as u right " \
          "join `%s` as s on u.point_type=s.user_operation_type and username='%s'" % ("tb_user_points",
                                                                                      "tb_score_rule_template",
                                                                                      username)
    msg = "[in query_user_points_detail] sql=" + sql
    logging.info(msg)
    cursor_0.execute(sql)
    result = cursor_0.fetchall()
    cursor_0.close()
    db_manager.close()
    if result is None:
        return False, None
    data = []
    total_points = 0
    for item in result:
        tmp = dict()
        if item['point_value'] is None and item['user_operation_type'] in score_rule_list:
            tmp['point_type'] = item['user_operation_type']
            tmp['point_desc'] = item['user_operation_desc']
            tmp['point_value'] = 0
            data.append(tmp)
        elif item['point_value'] is not None:
            tmp['point_type'] = item['user_operation_type']
            tmp['point_desc'] = item['user_operation_desc']
            tmp['point_value'] = item['point_value']
            total_points += tmp['point_value']
            data.append(tmp)

    return True, {
        "total_points": total_points,
        "point_detail": data
    }


def follow_other(username, other_username):
    """
    关注某人
    :param username: 用户名
    :param other_username: 其他的用户名
    :return:
    """
    db_manager = DBManager()
    # 校验两者关系
    sql0 = "select *from `%s` where (username='%s' and other_username='%s' and relation_type=0) or (username='%s' " \
           "and other_username='%s' and relation_type=1)" % ("tb_relation", username, other_username, other_username,
                                                             username)
    msg = "[in follow_other] sql0=" + sql0
    logging.info(msg)
    cursor0 = db_manager.conn_r.cursor()
    result0 = cursor0.execute(sql0)
    cursor0.close()
    logging.info(result0)
    if result0 is not None and result0 != 0:
        return False
    props = dict()
    props['username'] = username
    props['other_username'] = other_username
    props['relation_type'] = 0
    sql = forEachPlusInsertProps("tb_relation", props)
    try:
        cursor_0 = db_manager.conn_r.cursor()
        cursor_0.execute(sql)
        db_manager.conn_r.commit()
        cursor_0.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor_0.close()
        db_manager.close()
        raise Exception
        return False
    # 插入反向关系
    props = dict()
    props['username'] = other_username
    props['other_username'] = username
    props['relation_type'] = 1
    sql = forEachPlusInsertProps("tb_relation", props)
    try:
        cursor_0 = db_manager.conn_r.cursor()
        cursor_0.execute(sql)
        db_manager.conn_r.commit()
        cursor_0.close()
    except Exception:
        db_manager.conn_r.rollback()
        cursor_0.close()
        db_manager.close()
        raise Exception
        return False
    db_manager.close()
    return True


def query_followers(username):
    """
    请求关注/粉丝数量
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    cursor_0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    sql = "select count(*) as follows from `%s` where username='%s' and relation_type=0" % ("tb_relation", username)
    cursor_0.execute(sql)
    result = cursor_0.fetchone()
    cursor_0.close()
    if result is None:
        follows_num = 0
    else:
        follows_num = result['follows']

    cursor_1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    sql1 = "select count(*) as fans from `%s` where other_username='%s' and relation_type=0" % ("tb_relation", username)
    cursor_1.execute(sql1)
    result1 = cursor_1.fetchone()
    cursor_1.close()
    if result1 is None:
        fans_num = 0
    else:
        fans_num = result1['fans']

    db_manager.close()
    return True, follows_num, fans_num


def query_collection_question_list(username):
    """
    请求用户收藏问题列表
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    sql = "select tc.question_id, tq.question_content, tq.question_pic_url, tq.question_sound_url, (select count(*) from `tb_answer` where " \
          "question_id=tc.question_id) as counts from `tb_question_collection` as tc inner join `tb_question` as tq on " \
          "tc.question_id=tq.question_id and tc.collecter_username='%s';" % username

    cursor = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    db_manager.close()
    if results is None or len(results) == 0:
        return False, None
    return True, results


def modify_personal_information(username, props=None, options=None):
    """
    更新个人信息
    :param username: 用户名
    :param props: 更新的数据域
    :return:
    """
    if props:
        assert isinstance(props, dict)
        if options:
            assert isinstance(options, dict)
            props.update(options)
        update_str = FormatUpdateStr(props)
        sql0 = "update `%s` set %s where username='%s'" % ("tb_user", update_str, username)
        msg = "[in modify_personal_information] sql0=" + sql0
        logging.info(msg)
        try:
            db_manager = DBManager()
            cursor_0 = db_manager.conn_r.cursor()
            cursor_0.execute(sql0)
            db_manager.conn_r.commit()
            cursor_0.close()
        except Exception:
            db_manager.conn_r.rollback()
            cursor_0.close()
            db_manager.close()
            raise Exception
            return False
        db_manager.close()
        return True
    return False


def get_latest_id(username):
    """
    根据用户名获取tb_account中对应主键ID
    :param username: 用户名
    :return:
    """
    db_manager = DBManager()
    sql0 = "select id from `%s` where username='%s'" % ("tb_account", username)
    cursor0 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor0.execute(sql0)
    result0 = cursor0.fetchone()
    cursor0.close()
    if result0:
        return result0['id']

    sql1 = "SHOW TABLE STATUS LIKE `%s`" % "tb_account"
    cursor1 = db_manager.conn_r.cursor(cursorclass=DictCursor)
    cursor1.execute(sql1)
    result1 = cursor0.fetchone()
    return result1['Auto_increment']

