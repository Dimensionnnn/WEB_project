from flask import Flask
from flask import Flask, jsonify, request, make_response, url_for, redirect, render_template, session
import datetime
import pymysql


app = Flask(__name__, static_url_path="")
app.config['SECRET_KEY'] = '123456'


@app.route('/')
def hello_world():
    return jsonify(data='ok')


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


# 读取新闻标题
@app.route('/news/outline', methods=['get', 'post'])
def get_news_outline():
    try:
        with DB() as db:
            sql = 'select * from news_outline order by id desc limit 20'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='suceess', errmsg='获取成功', data=data)
    except Exception as e:
        return jsonify(error='error', errmsg='获取失败', data=e)


@app.route('/news/outline/detail', methods=['get', 'post'])
def get_news_outline_detail():
    try:
        data = request.json
        id = data.get('id')
        with DB() as db:
            sql = "select * from news_outline where id=%d" % id
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='success', code=0, errmsg='获取成功', data=data)
    except Exception as e:
        return jsonify(errno='error', errmsg='获取失败', code=-1,  data=e)


# 读取新闻图片
@app.route('/header/banner', methods=['get', 'post'])
def get_header_banner():
    try:
        with DB() as db:
            sql = "select * from header_banner"
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='success', errmsg='获取成功', data=data)
    except Exception as e:
        return jsonify(error='error', errmsg='获取失败', data=e)


# 提供新闻轮播图、新闻标题显示
@app.route('/news/banner', methods=['get', 'post'])
def getimg():
    try:
        with DB() as db:
            sql = 'SELECT * FROM news'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 提供特别活动card的imgurl、text、content 图片、标题、简介
@app.route('/act', methods=['get', 'post'])
def getactcard():
    try:
        with DB() as db:
            sql = 'SELECT url,text,content FROM activity'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 积分，具体计算方法？
@app.route('/credit', methods=['get', 'post'])
def grade():
    # json_data = request.json                            # 获取页面输入的数据
    # id= json_data.get("id")
    id='1001'
    try:
        with DB() as db:
            sql = 'SELECT study_hour, act_hour, credit FROM user where userId="%s"' % id
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        print(e)
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


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
@app.route('/map', methods=['get', 'post'])
def map():
    try:
        with DB() as db:
            sql = 'SELECT * FROM diplomat'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 前辈寄语，以tag分类,tag编写需商讨
@app.route('/older', methods=['get', 'post'])
def older():
    try:
        with DB() as db:
            sql = 'SELECT * FROM model_people'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 优秀党支部图片及党支部名称,轮播图放
@app.route('/org', methods=['post', 'get'])
def getorg():
    try:
        with DB() as db:
            sql = 'SELECT * FROM model_party'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 提供党支部界面的新闻标题,以tag分类
@app.route('/orgnews', methods=['post', 'get'])
def getorgnews():
    try:
        with DB() as db:
            sql = 'SELECT * FROM model_party_news'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='ok', errmsg="获取成功", data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 获取优秀党员
@app.route('/partymember', methods=['get', 'post'])
def partymember():
    try:
        with DB() as db:
            sql = 'SELECT * FROM good_party_member'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='success', errmsg='获取成功', data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 获取优秀事迹
@app.route('/goodthing', methods=['get', 'post'])
def good_thing():
    try:
        with DB() as db:
            sql = 'SELECT * FROM good_thing'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='success', errmsg='获取成功', data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


@app.route('/goodthing/detail', methods=['post', 'get'])
def good_thing_detail():
    try:
        with DB() as db:
            data = request.json
            type = data.get('type')
            index = data.get('index')
            sql = 'select * from model_people where type=%d limit %d, 1;' % (type, index)
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='success', code=0, data=data)
    except Exception as e:
        return jsonify(errno='fail', code=-1,  data=e)


# 获取精选评论
@app.route('/party_comment', methods=['get', 'post'])
def party_commment():
    try:
        with DB() as db:
            sql = 'SELECT * FROM party_comment'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='success', errmsg='获取成功', data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 获取组织生活窗数据
@app.route('/window', methods=['get', 'post'])
def window():
    try:
        with DB() as db:
            sql = 'SELECT * FROM window_visit'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='success', errmsg='获取成功', data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 获取心得体会
@app.route('/share_think', methods=['get', 'post'])
def think_share():
    try:
        with DB() as db:
            sql = 'SELECT * FROM think_share order by time desc'
            db.execute(sql)
            data = db.fetchall()
            return jsonify(errno='success', errmsg='获取成功', data=data)
    except Exception as e:
        return jsonify(errno='notok', errmsg="用户数据读取失败", data=e)


# 提交心得体会
@app.route('/share_think_send', methods=['get', 'post'])
def think_share_send():
    data = request.json
    try:
        with DB() as db:
            sql = 'insert into think_share(name, content, time) values ("%s", "%s", "%s");' % \
                  (data.get('name'), data.get('content'), data.get('time'))
            db.execute(sql)
            return jsonify(message='success', code=0)
    except Exception as e:
        return jsonify(message='fail', code=-1, errmsg=e)


@app.route('/get_exam', methods=['get', 'post'])
def get_exam():
    try:
        with DB() as db:
            sql = "select * from exam_option where type=1"
            db.execute(sql)
            data = db.fetchall()
            return jsonify(message='success', code=0, data=data)
    except Exception as e:
        return jsonify(message='fail', code=-1, data=e)


@app.route('/get_else_exam', methods=['get', 'post'])
def get_else_exam():
    try:
        with DB() as db:
            sql = "select * from exam_option where type=2"
            db.execute(sql)
            data = db.fetchall()
            return jsonify(message='success', code=0, data=data)
    except Exception as e:
        return jsonify(message='fail', code=-1, data=e)

@app.route('/get_red_scene', methods=['get', 'post'])
def get_red_scenery():
    try:
        with DB() as db:
            sql = "select * from scene"
            db.execute(sql)
            data = db.fetchall()
            return jsonify(message='success', code=0, data=data)
    except Exception as e:
        return jsonify(message='fail', code=-1, data=e)


class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
                                    password="godj123!@#",
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
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
