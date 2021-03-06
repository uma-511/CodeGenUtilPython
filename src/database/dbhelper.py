#!python3
import pymysql.cursors


class DBHelper:
    __ip = '39.108.99.240'
    __port = 45036
    __userName = 'dev'
    __password = 'Dev@2019'
    __databaseName = 'deepbrief'
    __connection = None

    def get_connection(self):
        self.__connection = pymysql.connect(
            host=self.__ip,
            port=self.__port,
            user=self.__userName,
            password=self.__password,
            db=self.__databaseName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    def get_table_meta(self, table_name):
        with self.__connection.cursor() as cursor:
            cursor.execute(
                "select column_name,data_type,column_key,column_comment from information_schema.columns "
                "where table_name = %s AND table_schema = %s",
                (table_name, self.__databaseName))
            result = cursor.fetchall()
        return result

    def close_connection(self):
        self.__connection.close()
