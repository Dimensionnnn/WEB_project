from flask import Flask
from flask import Flask, jsonify, request, make_response, url_for, redirect, render_template, session
import datetime
import pymysql


app = Flask(__name__, static_url_path = "")
app.config['SECRET_KEY'] = '123456'

@app.route('/')
def hello_world():
    try:
        with DB() as db:
            sql = 'SELECT * FROM map'
            db.execute(sql)
            data = db.fetchall()
            print(type(data))
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


# 增加了一个不知道会不会用到的登录函数
@app.route('/login', methods=['get', 'post'])
def login():
    json_data = request.json                            # 获取页面输入的数据
    id= json_data.get("id")
    pswd = json_data.get("pswd")
    try:
        with DB() as db:
            sql = 'SELECT password FROM user WHERE id = "%s"' % id
            db.execute(sql)
            data = db.fetchone()
        if data:
            if pswd == data[0]:
                return jsonify(errno='ok', errmsg="登录成功")
            else:
                return jsonify(errno='notok', errmsg="用户名或密码错误")
        else:
            return jsonify(errno='notok', errmsg="用户名或密码错误")
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")



# 提供新闻轮播图、新闻标题显示
@app.route('/news/banner', methods=['get','post'])
def getimg():
    try:
        with DB() as db:
            sql = 'SELECT imgurl,title FROM news'
            db.execute(sql)
            data = db.fetchall()
            print(data)
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


#  提供高层动态新闻梗概
@app.route('/news/outline', methods=['get', 'post'])
def getoutline():
    try:
        with DB() as db:
            sql = 'SELECT outline FROM news'
            db.execute(sql)
            data = db.fetchall()
            print(data)
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


# 提供特别活动card的imgurl、text、content 图片、标题、简介
@app.route('/act', methods=['get', 'post'])
def getactcard():
    try:
        with DB() as db:
            sql = 'SELECT imgurl,title,content FROM activity'
            db.execute(sql)
            data = db.fetchall()
            print(data)
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


# 积分，具体计算方法？
@app.route('/grade')
def grade():
    json_data = request.json                            # 获取页面输入的数据
    id= json_data.get("id")
    try:
        with DB() as db:
            sql = 'SELECT activity_hours,study_hours FROM user WHERE id = %s' % id
            db.execute(sql)
            data = db.fetchone()
            print(data)
            grade = data[0]*2+data[1]*3
            return jsonify(errno='ok', errmsg="获取成功", data=data, grade=grade)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


# #  从党建网爬取新闻录入数据库,未完善,需讨论。按tag分类四个。
# @app.route('/organization')
# def sendData():
#     imgurl = "http://dangjian.people.com.cn/"
#     #print(getHTMLText(imgurl))
#     soup = BeautifulSoup(getHTMLText(imgurl), "html.parser")
#     titlelist = getData(soup)
#
    # try:
    #     with DB() as db:
    #         for i in titlelist:
    #             sql = 'INSERT INTO '
    #             db.execute(sql)
    #         data = db.fetchall()
    #
    #         print(data)
    #         return jsonify(errno='ok', errmsg="获取成功", data=data)
    # except Exception as e:
    #     print(e)
#
# def getHTMLText(imgurl):
#     try:
#         r = requests.get(imgurl,timeout=15)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
#
# def getData(soup):
#     allData = list()
#     # soup=soup.find('div class="clearfix w1000 p3_con')
#     titlelist=[]
#     centerData=soup.select('ul')
#     for tr in centerData:
#         tdData = tr.find_all('li')
#         for td in tdData:
#             if td.string!=None and len(titlelist)<26:
#                 titlelist.append(td.string)
#     print(titlelist)
#     return titlelist

# 外交足迹页面 提供城市名称、经纬度
@app.route('/map', methods=['get','post'])
def map():
    try:
        with DB() as db:
            sql = 'SELECT * FROM map'
            db.execute(sql)
            data = db.fetchall()
            print(data)
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


# 前辈寄语，以tag分类,tag编写需商讨
@app.route('/older',methods=['get','post'])
def older():
    try:
        with DB() as db:
            sql = 'SELECT * FROM older'
            db.execute(sql)
            data = db.fetchall()
            print(data)
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


# 优秀党支部图片及党支部名称,轮播图放
@app.route('/org',methods=['post','get'])
def getorg():
    try:
        with DB() as db:
            sql = 'SELECT * FROM org'
            db.execute(sql)
            data = db.fetchall()
            print(data)
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


# 提供党支部界面的新闻标题,以tag分类
@app.route('/orgnews', methods=['post','get'])
def getorgnews():
    try:
        with DB() as db:
            sql = 'SELECT title,tag FROM orgnews'
            db.execute(sql)
            data = db.fetchall()
            print(data)
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")


# 点击获取具体内容
@app.route('/orgnews/in',methods=['post','get'])
def getcontent():
    json_data = request.json                            # 获取页面输入的数据
    id= json_data.get("newsid")
    try:
        with DB() as db:
            sql = 'SELECT * FROM orgnews WHERE newsid = %s ' % id
            db.execute(sql)
            data = db.fetchone()
            print(data)
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败")






class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(host="cdb-evw36b72.cd.tencentcdb.com", port=10071, user="root",
                                    password="wf1999wf",
                                    database="godj")
        self.cursor = self.conn.cursor()
        # self.num = self.cos.execute()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    app.run()
