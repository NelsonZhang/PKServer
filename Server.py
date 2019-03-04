# -*- coding:utf-8 -*-
from flask import Flask, request

from Address import Address
from Collect import Collect
from Indent import Indent
from Product import Product
from User import User

app = Flask(__name__)

user = User()
product = Product()
collect = Collect()
indent = Indent()
address = Address()


def form_user():
    data = dict()
    data['phone_number'] = request.form['phone_number']
    data['name'] = request.form.get('name', default=None)
    data['password'] = request.form.get('password', default=None)
    data['avatar'] = request.form.get('avatar', default=None)
    return data


def form_product():
    data = dict()
    data['ID'] = request.form['ID']
    data['user_ID'] = request.form.get('user_ID', default=None)
    data['name'] = request.form.get('name', default=None)
    data['picture'] = request.form.get('picture', default=None)
    data['information'] = request.form.get('information', default=None)
    data['start_price'] = request.form.get('start_price', default=None)
    data['current_price'] = request.form.get('current_price', default=None)
    data['time'] = request.form.get('time', default=None)
    data['state'] = request.form.get('state', default=0)
    return data


@app.route("/getUser", methods=['POST'])
def getUser():
    if user.getUser(form_user()) is not None:
        return user.getUser(form_user())
    return '查询失败'


@app.route('/insertUser', methods=['POST'])
def insertUser():
    if user.addUser(form_user()) is None:
        return '插入成功'
    return '插入失败'


@app.route('/updataUser', methods=['POST'])
def updataUser():
    if user.updataUser(form_user()) is None:
        return '更新成功'
    return '更新失败'


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='localhost', port=5000)
