from flask import Flask, render_template ,request
import pymysql

# pip install requests



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/show/')
def show():
    conn = pymysql.connect(host='127.0.0.1',port=3306, user='root',passwd='passwd', db='note')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = 'select * from app'
    cursor.execute(sql)

    data_list = cursor.fetchall()

    cursor.close()
    conn.close()

    print(data_list)

    return render_template('show.html', data_list=data_list)

@app.route('/add/user/', methods=["GET", "POST"])
def adduser():
    if request.method == 'GET' :
        return render_template('add_user.html')
    
    print(request.form.get('user'));

    return "xxx"


if __name__ == '__main__':
    app.run()


