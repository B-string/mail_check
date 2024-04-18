import pymysql
from consts.db import CONST

# CRUD
# create    mail_log
# read      user_info
# update    mail_log
# delete

class TrainingDatabase :

    # singleton
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.HOST = CONST.HOST
        self.USER = CONST.USER
        self.PWD = CONST.PWD
        self.DB = CONST.DATABASE

    def db_connect(self):
        return pymysql.connect(host=self.HOST, user=self.USER, password=self.PWD, database=self.DB)

    # 로그인 처리
    def read_user_data(self, params: dict):
        db_conn = self.db_connect()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)

        message = {}

        if params != {}:
            sql = f'select * from users where %s=%s and %s=%s;'
            cursor.execute(sql, [
                'user_id', 
                params['user_id'], 
                'user_pwd', 
                params['user_pwd']
                ])

            message = {'Message' : 'Success'}
        else:
            message = {'Message' : 'Error'}

        db_conn.close()
        return message

    # 세션 저장
    def insert_session_data(self, params : dict):
        None


    # 훈련대상 정보 읽어오기
    def read_target_data(self, params : dict):
        db_conn = self.db_connect()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)

        message = {}

        if params !={}:
            sql = f'select * from target_list where %s=%s and %s=%s;'
            cursor.execute(sql, [
                'id', 
                params['id'], 
                'email', 
                params['email']
                ])
        
            message = {'Message' : 'Success'}
        else:
            message = {'Message' : 'Error'}

        db_conn.close()
        return message
    

    # 훈련 기록 입력
    def insert_training_data(self, params : dict):
        db_conn = self.db_connect()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)

        message = {}
        if params != {}:
            # no, id, name, department, ip, status, time
            sql = f'INSERT INTO mail_log(%s, %s, %s, %s, %s, time) values(%s, %s, %s, %s, %s, now());'
            
            columns = []
            values = []
            for key, val in params.items():
                columns.append(key)
                values.append(val)
            cursor.execute(sql, columns + values)

            message = {'Message' : 'Success'}
        else:
            message = {'Message' : 'Error'}
        
        db_conn.commit()
        db_conn.close()
        
        return message


