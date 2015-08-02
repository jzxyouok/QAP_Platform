# coding: utf-8

import MySQLdb
from conf.cm import ConfigManager


class DBManager:
    def __init__(self):
        cm = ConfigManager()
        db_config = cm.get_dbconfig()
        self.conn_r = MySQLdb.connect(
            host=db_config['host'],
            user=db_config['user'],
            passwd=db_config['passwd'],
            db=db_config['db'],
            charset=db_config['charset']
        )

    def close(self):
        self.conn_r.close()

    def save(self, sql_data_insert, data=None):
        # 保存数据
        rows = 0
        cursor = self.conn_r.cursor()
        if not data:
            if len(data) == 0:
                print '数据为空'
                return False, 0
            rows = cursor.execute(sql_data_insert)
            cursor.close()
            if rows > 0:
                print '数据保存成功'
                return True, rows
            else:
                print '数据保存失败'
                return False, rows
        size = len(data)
        if size > 1:
            rows = cursor.executemany(sql_data_insert, data)
        else:
            rows = cursor.execute(sql_data_insert, data[0])
        cursor.close()
        if rows < size:
            print '数据保存失败'
            return False, rows
        else:
            print '数据保存成功'
            return True, rows

    def update(self, sql_data_update):
        cursor = self.conn_r.cursor()
        cursor.execute(sql_data_update)
        cursor.close()
        print '数据更新成功'

    def delete(self, sql_data_delete):
        cursor = self.conn_r.cursor()
        cursor.execute(sql_data_delete)
        cursor.close()
        print '数据删除成功'

    def query(self, sql_data_query, targets=None):
        cursor = self.conn_r.cursor()
        if not targets:
            cursor.execute(sql_data_query)
        else:
            cursor.execute(sql_data_query, targets)
        data = cursor.fetchall()
        cursor.close()
        return data

    def query_table_exist_with_name(self, table_name):
        # 支持模糊匹配表名, 无法自定义sql语句
        sql_query_table = "show tables like %s"
        cursor = self.conn_r.cursor()
        size = cursor.execute(sql_query_table, (table_name, ))
        cursor.close()
        if size == 0:
            return False
        else:
            return True

    def query_table_exist_with_sql(self, sql):
        # 自定义sql语句
        cursor = self.conn_r.cursor()
        size = cursor.execute(sql)
        cursor.close()
        if size == 0:
            return False
        else:
            return True

    def get_latest_data(self, sql_data_query_latest):
        # 获取表最新一条数据
        cursor = self.conn_r.cursor()
        cursor.execute(sql_data_query_latest)
        data = cursor.fetchone()
        cursor.close()
        return data

    def create_table(self, sql_table_create):
        # sql语句创建表
        cursor = self.conn_r.cursor()
        cursor.execute(sql_table_create)
        cursor.close()
