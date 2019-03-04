# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Entity import toJson, User, Product, Address, Indent, Collect

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class MyDatabase():
    session = None

    def __init__(self):  # 初始化，连接数据库
        engine = create_engine('mysql+mysqldb://root:123@120.79.87.68:3306/kp?charset=utf8')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def __del__(self):
        self.session.close()

    def getUserData(self, user_ID):  # 将对应用户的信息返回
        try:
            data = self.session.query(User).filter_by(phone_number=user_ID).first()
            return toJson(data)
        except:
            return None  # 无法获取用户信息

    def insertUserData(self, user):  # 插入新的用户信息
        try:
            self.session.add(user)
            self.session.commit()
        except:
            return 1  # 数据插入失败

    def updataUserData(self, user):
        try:
            u = self.session.query(User).filter_by(phone_number=user['phone_number']).first()
            if user['name'] is not None:
                u.name = user['name']
            if user['password'] is not None:
                u.password = user['password']
            if user['avatar'] is not None:
                u.avatar = user['avatar']
            self.session.commit()
        except:
            return 1  # 数据更新失败

    def getProduct(self, id):
        try:
            data = self.session.query(Product).filter_by(ID=id).first()
            return toJson(data)
        except:
            return 1  # 查询商品失败

    def insertProduct(self, product):
        try:
            self.session.add(product)
            self.session.commit()
        except:
            return 1  # 添加商品失败

    def deleteProduct(self, id):
        try:
            data = self.session.query(Product).filter_by(ID=id).first()
            self.session.delete(data)
            self.session.commit()
        except:
            return 1  # 删除数据失败

    def getAddress(self, id):
        try:
            data = self.session.query(Address).filter_by(user_ID=id).all()  # 匹配所有的地址返回
            return toJson(data)
        except:
            return 1  # 查询地址失败

    def insertAddress(self, address):
        try:
            self.session.add(address)
            self.session.commit()
        except:
            return 1  # 插入数据失败

    def updataAddress(self, addr):
        try:
            data = self.session.query(Address).filter_by(add_ID=addr['add_ID']).first()
            data.address = addr['address']
            self.session.commit()
        except:
            return 1  # 更新数据失败

    def deleteAddress(self, address):
        try:
            data = self.session.query(Address).filter_by(add_ID=address['add_ID']).first()
            self.session.delete(data)
            self.session.commit()
        except:
            return 1  # 删除地址失败

    def getIndent(self, user_ID):
        try:
            data = self.session.query(Indent).filter_by(user_ID=user_ID).all()
            return toJson(data)
        except:
            return 1  # 获取订单失败

    def insertIndent(self, indent):
        try:
            self.session.add(indent)
            self.session.commit()
        except:
            return 1  # 插入订单失败

    def updataIndent(self, indent):
        try:
            data = self.session.query(Indent).filter_by(user_ID=indent['user_ID'],
                                                        product_ID=indent['product_ID']).first()
            data.state = indent['state']
            self.session.commit()
        except:
            return 1  # 更新订单失败

    def getCollect(self, user_ID):
        try:
            data = self.session.query(Collect).filter_by(user_ID=user_ID).all()
            return toJson(data)
        except:
            return 1  # 获取收藏信息失败

    def insertCollect(self, collect):
        try:
            self.session.add(collect)
            self.session.commit()
        except:
            return 1  # 插入数据失败

    def deleteCollect(self, collect):
        try:
            data = self.session.query(Collect).filter_by(user_ID=collect['user_ID'],
                                                         product_ID=collect['product_ID']).first()
            self.session.delete(data)
            self.session.commit()
        except:
            return 1  # 删除收藏失败