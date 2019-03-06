# -*- coding:utf-8 -*-
import datetime
import random

import redis
import requests
from flask import Flask, request, json

from Address import Address
from Collect import Collect
from Entity import toJson
from Indent import Indent
from MyDatabase import MyDatabase
from Product import Product
from User import User

app = Flask(__name__)

myDatabase = MyDatabase()
my_redis = redis.Redis(host='120.79.87.68', port=6379, password='123')
user = User()
product = Product()
collect = Collect()
indent = Indent()
address = Address()


def form_user():
    data = dict()
    data["phone_number"] = request.form["phone_number"]
    data["name"] = request.form.get("name", default=None)
    data["password"] = request.form.get("password", default=None)
    data["avatar"] = request.form.get("avatar", default=None)
    return data


def form_product():
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    data = dict()
    data['ID'] = request.form.get('ID', default=nowTime)
    data['user_ID'] = request.form.get('user_ID', default=None)
    data['name'] = request.form.get('name', default=None)
    data['picture'] = request.form.get('picture', default=None)
    data['information'] = request.form.get('information', default=None)
    data['start_price'] = request.form.get('start_price', default=0.00)
    data['current_price'] = request.form.get('current_price', default=0.00)
    data['time'] = request.form.get('time', default=nowTime)
    data['state'] = request.form.get('state', default=0)
    data['catalog'] = request.form.get('catalog', default='未分类')
    return data


def form_indent():
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    data = dict()
    data['product_ID'] = request.form.get('product_ID', default=None)
    data['user_ID'] = request.form.get('user_ID', default=None)
    data['time'] = request.form.get('time', default=nowTime)
    data['state'] = request.form.get('state', default='未发货')
    data['number'] = request.form.get('number', default=1)
    return data


def form_address():
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    data = dict()
    data['user_ID'] = request.form.get('user_ID', default=None)
    data['address'] = request.form.get('address', default=None)
    data['add_ID'] = request.form.get('add_ID', default=nowTime)
    return data


def form_collect():
    data = dict()
    data['product_ID'] = request.form.get('product_ID', default=None)
    data['user_ID'] = request.form.get('user_ID', default=None)
    return data


def return_message(data):
    temp = dict()
    if data is not None and data is not 'null':
        if data is not 1:
            temp['data'] = json.loads(data)
        temp['message'] = 'success'
        temp['code'] = 1
    else:
        temp['message'] = 'fail'
        temp['code'] = 0
    return json.dumps(temp, encoding='utf8')


def verCode(phone_number):
    temp = str(random.randint(1000, 9999))
    my_redis.set(phone_number, temp, ex=300)
    data = dict()
    data['sid'] = '385e85924cfcd6a848f389396dfee5b0'
    data['token'] = 'a70188b07093e33e7cdb56815b7307dd'
    data['appid'] = '8f104e488fdf4e34b97365348128d08a'
    data['templateid'] = '438269'
    data['param'] = temp + ',300'
    data['mobile'] = phone_number
    return data


@app.route("/getUser", methods=['POST'])
def getUser():
    data = user.getUser(form_user(), myDatabase)
    return return_message(data)


@app.route('/insertUser', methods=['POST'])
def insertUser():
    temp = form_user()
    if my_redis.get(temp['phone_number']) == request.form['check_number']:
        data = user.addUser(temp, myDatabase)
        return return_message(data)
    return return_message(None)


@app.route('/updataUser', methods=['POST'])
def updataUser():
    data = user.updataUser(form_user(), myDatabase)
    return return_message(data)


@app.route('/login', methods=['POST'])
def login():
    temp = form_user()
    data = json.loads(user.getUser(temp, myDatabase))
    if data is None:
        return return_message(None)
    if temp['password'] == data['password']:
        return return_message(1)
    return return_message(None)


@app.route('/getVerCode', methods=['POST'])
def getVerCode():
    phone_number = request.form["phone_number"]
    data = verCode(phone_number)
    header = {'content-type': 'application/json'}
    response = requests.post(url='https://open.ucpaas.com/ol/sms/sendsms', data=json.dumps(data), headers=header)
    response = response.json()
    if response['msg'] == 'OK':
        return return_message(1)
    return return_message(None)


@app.route('/getProduct', methods=['POST'])
def getProduct():
    data = product.getProduct(form_product(), myDatabase)
    return return_message(data)


@app.route('/insertProduct', methods=['POST'])
def insertProduct():
    data = product.insertProduct(form_product(), myDatabase)
    return return_message(data)


@app.route('/deleteProduct', methods=['POST'])
def deleteProduct():
    data = product.deleteProduct(form_product(), myDatabase)
    return return_message(data)


@app.route('/getBanner', methods=['GET'])
def getBanner():
    data = product.getBanner(myDatabase)
    return return_message(data)


@app.route('/getPageProduct', methods=['POST'])
def getPageProduct():
    page = request.form['page']
    return return_message(product.getPageProduct(page, myDatabase))


@app.route('/getAddress', methods=['POST'])
def getAddress():
    return return_message(address.getAddress(form_address(), myDatabase))


@app.route('/insertAddress', methods=['POST'])
def insertAddress():
    return return_message(address.insertAddress(form_address(), myDatabase))


@app.route('/updataAddress', methods=['POST'])
def updataAddress():
    return return_message(address.updataAddress(form_address(), myDatabase))


@app.route('/deleteAddress', methods=['POST'])
def deleteAddress():
    return return_message(address.deleteAddress(form_address(), myDatabase))


@app.route('/insertIndent', methods=['POST'])
def insertIndent():
    return return_message(indent.insertIndent(form_indent(), myDatabase))


@app.route('/updataIndent', methods=['POST'])
def updataIndent():
    return return_message(indent.updataIndent(form_indent(), myDatabase))


@app.route('/getIndent', methods=['POST'])
def getIndent():
    datas = indent.getIndent(form_indent(), myDatabase)
    datas = json.loads(datas)
    if len(datas):
        temps = []
        for data in datas:
            temp = {}
            pro = myDatabase.getProduct(data['product_ID'])
            pro = json.loads(pro)
            temp['product_name'] = pro['name']
            temp['price'] = pro['current_price']
            temp['picture'] = pro['picture']
            temp['information'] = pro['information']
            temp = dict(temp, **data)
            temps.append(temp)
        return return_message(toJson(temps))
    return return_message(None)


@app.route('/insertCollect', methods=['POST'])
def insertCollect():
    return return_message(collect.insertCollect(form_collect(), myDatabase))


@app.route('/deleteCollect', methods=['POST'])
def deleteCollect():
    return return_message(collect.deleteCollect(form_collect(), myDatabase))


@app.route('/getCollect', methods=['POST'])
def getCollect():
    datas = collect.getCollect(form_collect(), myDatabase)
    datas = json.loads(datas)
    if len(datas):
        temps = []
        for data in datas:
            temp = {}
            pro = myDatabase.getProduct(data['product_ID'])
            pro = json.loads(pro)
            temp['product_name'] = pro['name']
            temp['price'] = pro['current_price']
            temp['picture'] = pro['picture']
            temp['information'] = pro['information']
            temp = dict(temp, **data)
            temps.append(temp)
        return return_message(toJson(temps))
    return return_message(None)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='localhost', port=5000)
