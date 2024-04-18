from flask import Flask, request, render_template, url_for, redirect, session
from database import TrainingDatabase

app = Flask(__name__)
app.secret_key = 'Security'

@app.route('/', methods=['POST', 'GET'])
def main():
    

    return render_template('layout.html')

# 로그인 처리
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(request.form.get('user_id'))
        print(request.form.get('user_pwd'))
        
        

        

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
    # td = TrainingDatabase()
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(debug=True)
