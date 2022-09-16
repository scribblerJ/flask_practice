from flask import Flask 

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is....'},
    {'id': 2, 'title': 'css', 'body': 'css is....'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is....'}
]
navigator = '<ol>'+''.join([f'<li><a href="/read/{topic["id"]}/">{topic["title"]}<a></li>' for topic in topics])+'</ol>'
header = '<h1><a href="/">WEB</a></h1>' + navigator

def template(title, body):
    return f'''<!doctype html>
    <html>
        <body>
           {header}
            <h2>{title}</h2>
            {body}
        </body>
    </html>
    '''

@app.route('/')         # 접속한 URI가 '/' 즉 root 라면
def index():            # 이하 함수를 실행한다
    return template('Welcome', 'Hello, Web')

@app.route('/read/<id>/')        # URL 중 변수로 받고 싶은 부분을 중괄호(<>)로 표기
def number_printer(id):          # 동명의 인자를 함수로 받아서 사용
    topic = [i for i in topics if i['id'] == int(id)][0]
    return template(topic['title'], topic['body'])

app.run(debug=True)

# https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)