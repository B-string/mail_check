from flask import Flask, request, render_template, url_for, redirect, session
from database import TrainingDatabase

app = Flask(__name__)
app.secret_key = 'Security'

@app.route('/', methods=['POST', 'GET'])
def main():
    
    # 세션 존재 여부 확인

    # 세션 존재 시 메인 화면으로 이동

    # 세션 없을 시 로그인 창으로 이동

    return render_template('layout.html')

# 관리자 등록
@app.route('/regist', methods=['POST', 'GET'])
def user_register():

    if request.method == 'POST':
        
        user_id = request.form.get('user_id')
        user_pwd = request.form.get('user_pwd')
        name = request.form.get('name')
        department = request.form.get('department')

        # td = TrainingDatabase()


        None        

    return render_template('reg/regist.html')

# 로그인 처리
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        user_pwd = request.form.get('user_pwd')
        
        td = TrainingDatabase()
        params = {
            'user_id' : user_id,
            'user_pwd' : user_pwd
        }
        
        user_data = td.read_user_data(params=params)
        
        # 데이터베이스 비교

        # 성공 시 메인 화면으로 이동

        # 실패 시 로그인 창으로 이동


    return render_template('auth/login.html')

# 열람형
@app.route('/open', methods=['POST', 'GET'])
def mail_open():
    if request.args != {}:
        target_id = request.args.get('id')
        target_email = request.args.get('email')
        td = TrainingDatabase()
        
        params = {
            'id' : target_id,
            'email' : target_email
        }

        target = td.read_target_data(params=params)

        if target != ():
            # no, id, name, department, ip, status, time
            client_ip = request.headers.get('X-Forwarded-For')
            params = {
                'id' : target['id'],
                'name' : target['name'],
                'department' : target['department'],
                'ip' : client_ip,
                'status' : 'mail_open',
            }
            
            td.insert_training_data(params=params)

    return 'mail_open'

# 링크형
@app.route('/link', methods=['POST', 'GET'])
def mail_link():
    if request.method == 'GET':
        target_id = request.args.get('id')
        target_email = request.args.get('email')
        td = TrainingDatabase()
        
        params = {
            'id' : target_id,
            'email' : target_email
        }

        target = td.read_target_data(params=params)

        if target != ():
            # no, id, name, department, ip, status, time
            client_ip = request.headers.get('X-Forwarded-For')
            params = {
                'id' : target['id'],
                'name' : target['name'],
                'department' : target['department'],
                'ip' : client_ip,
                'status' : 'mail_link',
            }
            
            td.insert_training_data(table='mail_log', params=params)

    return 'mail_link'

# 실행형
@app.route('/excute', methods=['POST', 'GET'])
def mail_execute():
    if request.method == 'GET':
        target_id = request.args.get('id')
        target_email = request.args.get('email')
        td = TrainingDatabase()
        
        params = {
            'id' : target_id,
            'email' : target_email
        }

        target = td.read_target_data(params=params)

        if target != ():
            # no, id, name, department, ip, status, time
            client_ip = request.headers.get('X-Forwarded-For')
            params = {
                'id' : target['id'],
                'name' : target['name'],
                'department' : target['department'],
                'ip' : client_ip,
                'status' : 'mail_execute',
            }
            
            td.insert_training_data(table='mail_log', params=params)

    return 'mail_execute'




if __name__ == '__main__':
    td = TrainingDatabase()
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(debug=True)
