# coding:utf8

from numbers import Number


def forEachPlusInsertProps(tablename, props):
    """
    生成插入语句
    :param tablename:
    :param props:
    :return:
    """
    assert isinstance(props, dict)
    pkeysstr = str(tuple([str(key) for key in props.keys()])).replace('\'', '`')
    pvaluesstr = []
    for val in props.values():
        temp = "NULL,"
        if isinstance(val, Number):
            temp = "%s," % val
        elif val is None:
            temp = "NULL,"
        else:
            temp = "'%s'," % val.replace("'", "\\'")
        pvaluesstr.append(temp)

    pvaluesstr = ''.join(pvaluesstr)[:-1]
    sqlstr = """INSERT INTO `%s` %s values (%s);"""%(tablename,pkeysstr,pvaluesstr)
    return sqlstr


def FormatItem(key, value):
    sqlstr = ""
    if isinstance(value, Number):
        sqlstr = " `%s`=%s " % (key, value)
    else:
        sqlstr = " `%s`='%s'  " % (key, value.replace("'", "\\'"))
    return sqlstr


def FormatCondition(props):
    """
    生成查询条件字符串
    """
    items = props.items()
    itemstrlist = []
    for _item in items:
        if isinstance(_item[1],Number):
            sqlstr = " `%s`=%s AND"% _item
        else:
            sqlstr = " `%s`='%s' AND "%(_item[0], _item[1].replace("'", "\\'"))
        itemstrlist.append(sqlstr)
    sqlstr = ''.join(itemstrlist)
    return sqlstr[:-4]


def FormatUpdateStr(props):
    """
    生成更新语句
    """
    items = props.items()
    itemstrlist = []
    for _item in items:
        if isinstance(_item[1],Number):
            sqlstr = " `%s`=%s,"% _item
        elif _item[1] is None:
            sqlstr = " `%s`= NULL ,"% (_item[0])
        else:
            sqlstr = " `%s`='%s',"% (_item[0], _item[1].replace("'", "\\'"))
        itemstrlist.append(sqlstr)
    sqlstr = ''.join(itemstrlist)
    return sqlstr[:-1]


def forEachUpdateProps(tablename,props,prere):
    """
    遍历所要修改的属性，以生成sql语句
    """
    assert isinstance(props, dict)
    pro = FormatUpdateStr(props)
    pre = FormatCondition(prere)
    sqlstr = """UPDATE `%s` SET %s WHERE %s;"""% (tablename,pro,pre)
    return sqlstr


def EachQueryProps(props):
    """
    遍历字段列表生成sql语句
    """
    sqlstr = ""
    if props == '*':
        return '*'
    elif type(props) == type([0]):
        for prop in props:
            sqlstr = sqlstr + prop +','
        sqlstr = sqlstr[:-1]
        return sqlstr
    else:
        raise Exception('props to query must be dict')
        return


def forEachQueryProps(sqlstr, props):
    """
    遍历所要查询属性，以生成sql语句
    :param sqlstr:
    :param props:
    :return:
    """
    if props == '*':
        sqlstr += ' *'
    elif type(props) == type([0]):
        i = 0
        for prop in props:
            if(i == 0):
                sqlstr += ' ' + prop
            else:
                sqlstr += ', ' + prop
            i += 1
    else:
        raise Exception('props to query must be list')
        return
    return sqlstr
