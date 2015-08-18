# -*- coding: UTF-8 -*-
# 增加datetime.datetime的序列化操作
import json
import datetime
import decimal
import time
import traceback


class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.timedelta):
            return str(obj)
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class SmartResponse():
    def __init__(self):
        pass

    @classmethod
    def jsonwrap(cls, obj):
        """
        将JSON对象转成合适的字符串返回(处理datetime,并且以utf8的格式返回)
        :param msg:
        :return:
        """
        msg = json.dumps(obj, cls=MyJsonEncoder, ensure_ascii=False)

        if isinstance(msg, unicode):
            msg = msg.encode("utf8")
        return msg

    @classmethod
    def strwrap(cls, msg):
        if isinstance(msg, unicode):
            msg = msg.encode("utf8")

        return msg


class MyStrAList():
    """
    list与str互转
    """
    def __init__(self):
        pass

    @classmethod
    def str_to_list(cls, s_str, sep=' '):
        """
        str => list
        :param s_str: 源字符串
        :param sep: 分隔符, 默认为空白符
        :return:
        """
        if not s_str or len(s_str) == 0:
            return []
        return s_str.split(sep)

    @classmethod
    def list_to_str(cls, s_list, sep=' '):
        """
        list = > str
        :param s_list: 源列表
        :param sep: 分隔符, 默认为空白符
        :return:
        """
        if not s_list or len(s_list) == 0:
            return ''
        t_str = sep.join(['%s']*len(s_list)) % tuple(s_list)
        return t_str

time_formate_str = "%Y-%m-%d %H:%M:%S"

def time_now_str():
    return time.strftime(time_formate_str, time.localtime())


def copy_dict_by_keys(keys, source_dict, to_dict):
    for key in keys:
        if key in source_dict.keys():
            to_dict[key] = source_dict[key]
        else:
            print key , 'not in ', source_dict
            assert 0

def add_dict_by_keys(dict_1, dict_2, keys=None):
    if not keys:
        keys = dict_2.keys()

    for key in keys:
        if key in dict_2.keys():
            if key in dict_1.keys():
                dict_1[key] += dict_2[key]
            else:
                dict_1[key] = dict_2[key]


def minus_dict_by_keys(dict_1, dict_2, keys=None):
    if not keys:
        keys = dict_2.keys()

    for key in keys:
        if key in dict_2.keys():
            if key in dict_1.keys():
                dict_1[key] -= dict_2[key]


def fill_dict_by_path(paths, target_dict, value):
    if len(paths) > 1:
        no_last = paths[:-1]
        temp_dict = target_dict
        for path in no_last:
            if path not in temp_dict.keys():
                temp_dict[path] = {}
            temp_dict = temp_dict[path]
        temp_dict[paths[-1]] = value
    else:
        key = paths
        if isinstance(paths, list):
            key = paths[0]
        target_dict[key] = value


def get_dict_value_by_path(paths, source_dict):
    if len(paths) > 1:
        no_last = paths[:-1]
        temp_dict = source_dict
        for path in no_last:
            if path in temp_dict.keys():
                temp_dict = temp_dict[path]
            else:
                return None
        return temp_dict.get(paths[-1])
    else:
        key = paths
        if isinstance(paths, list):
            key = paths[0]
        return source_dict.get(key)


def safe_str_to_int(value):
    try:
        if isinstance(value, int):
                return value
        if value:
                return int(value)
        else:
            return None
    except Exception, e:
        print traceback.format_exc()
        return 0


def safe_str_to_list(value):
    try:
        if isinstance(value, list):
            return value
        if value:
            return eval(value)
        else:
            return None
    except Exception, e:
        print traceback.format_exc()
        return []


def safe_list_to_str(value):
    try:
        if isinstance(value, str):
            return value
        if value:
            return repr(value)
        else:
            return None
    except Exception, e:
        print traceback.format_exc()
        return '[]'


def safe_str_to_dict(value):
    try:
        if isinstance(value, dict):
            return value
        if value:
            return eval(value)
        else:
            return None
    except Exception, e:
        print traceback.format_exc()
        return {}


#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime(time_formate_str)

#把字符串转成datetime
def string_toDatetime(string):
    return datetime.datetime.strptime(string, time_formate_str)

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

#把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime(time_formate_str, time.localtime(stamp))

#把datetime类型转成时间戳形式
def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())


def is_datetime_equal(a_date_time, b_date_time):
    if a_date_time.year == b_date_time.year and a_date_time.month == b_date_time.month \
            and a_date_time.day == b_date_time.day:
        return True
    return False


def time_delta_toString(timeDelta):
    return '{:02}:{:02}:{:02}'.format(timeDelta.seconds // 3600, timeDelta.seconds % 3600 // 60, timeDelta.seconds % 60)