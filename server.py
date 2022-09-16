from flask import Flask, request, redirect

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is....'},
    {'id': 2, 'title': 'css', 'body': 'css is....'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is....'}
]
next_topic_id = 4


def template(title, body):
    navigator = '<ol>'+''.join([f'<li><a href="/read/{topic["id"]}/">{topic["title"]}<a></li>' for topic in topics])+'</ol>'
    return f'''<!doctype html>
    <html>
        <body>
           <h1><a href="/">WEB</a></h1>
            {navigator}
            <h2>{title}</h2>
            {body}
        </body>
        <footer>
            <a href="/create/">create</a>
        </footer>
    </html>
    '''

@app.route('/')         # 접속한 URI가 '/' 즉 root 라면
def index():            # 이하 함수를 실행한다
    return template('Welcome', 'Hello, Web')

@app.route('/read/<int:id>/')        # URL 중 변수로 받고 싶은 부분을 중괄호(<>)로 표기 (형식 지정 필요)
def read(id):                       # 동명의 인자를 함수로 받아서 사용
    topic = [i for i in topics if i['id'] == int(id)][0]
    update_btn = f'<p><a href="/update/{id}/">update</a></p>'
    delete_btn = f'<p><a href="/delete/{id}/">delete</a></p>'
    return template(topic['title'], topic['body']+update_btn+delete_btn)

@app.route('/delete/<int:id>/')
def delete(id):
    topic_idx= topics.index([i for i in topics if i['id'] == int(id)][0])
    del topics[topic_idx]
    return redirect('/')


@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    topic = [i for i in topics if i['id'] == int(id)][0]
    if request.method == 'GET':
        content = f'''
                <form action="/update/{id}/" method="POST">
                    <p><input type="text" name="title" placeholder="title">{topic['title']}</p>
                    <p><textarea name="body" placeholder="body">{topic['body']}</textarea></p>
                    <p><input type="submit" value="update"><p>
                </form>
            '''
        return template('update', content)
    else:
        topic = [i for i in topics if i['id'] == int(id)][0]
        title = request.form['title'] if request.form['title'] != '' else topic['title']
        body = request.form['body'] if request.form['body'] != '' else topic['body']
        topics[topics.index(topic)] = {'id': id, 'title': title, 'body': body}
        return redirect(f'/read/{id}/')
        
    

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"><p>
            </form>
        '''
        return template('create', content)
    else:
        global next_topic_id
        topics.append({'id': next_topic_id, 'title': request.form['title'], 'body': request.form['body']})
        next_topic_id += 1
        return redirect(f'/read/{str(next_topic_id-1)}/')

app.run(debug=True)

# https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)