from flask import Flask
import random

app = Flask(__name__)

@app.route('/')         # 접속한 URI가 '/' 즉 root 라면
def index():            # 이하 함수를 실행한다
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/number/<num>/')        # URL 중 변수로 받고 싶은 부분을 중괄호(<>)로 표기
def number_printer(num):            # 동명의 인자를 함수로 받아서 사용
    return 'The number is '+ num

app.run(debug=True)

# https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)