from flask import Flask, session

# python flast session exam
app = Flask(__name__)

#secret_key 설정 : session 을 사용하기 위해서 필요, 설정안하면 에러
app.secret_key = '1234qwer'

@app.route('/')
def index():
    if 'name' in session:
        return '%s' % escape(session['name'])
    return 'nolog'

@app.route('/login', methods=['POST', 'GET']) 
def login(): 
    if request.method == 'POST': 
        # Post 요청일 경우
        session['name'] = request.form['name'] 
        return redirect(url_for('index')) 
    # Get 요청일 경우
    return ''