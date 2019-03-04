# -*- coding:utf-8 -*-
# 将数据库表格实体化
import json

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from AlchemyJsonEncoder import new_alchemy_encoder

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    name = Column(String(128))
    phone_number = Column(String(128), primary_key=True)
    password = Column(String(128))
    avatar = Column(String(128))


class Product(Base):
    __tablename__ = 'product'
    ID = Column(String(128), primary_key=True)
    name = Column(String(128))
    user_ID = Column(String(128), ForeignKey("user.phone_number", ondelete="CASCADE"), primary_key=True)
    picture = Column(String(128))
    information = Column(String(128))
    start_price = Column(String(128))
    current_price = Column(String(128))
    time = Column(String(128))
    state = Column(String(128))


class Indent(Base):
    __tablename__ = 'indent'
    product_ID = Column(String(128), ForeignKey("product.ID", ondelete="CASCADE"), primary_key=True)
    user_ID = Column(String(128), ForeignKey("user.phone_number", ondelete="CASCADE"), primary_key=True)
    time = Column(String(128))
    state = Column(String(128))


class Collect(Base):
    __tablename__ = 'collect'
    product_ID = Column(String(128), ForeignKey("product.ID", ondelete="CASCADE"), primary_key=True)
    user_ID = Column(String(128), ForeignKey("user.phone_number", ondelete="CASCADE"), primary_key=True)


class Address(Base):
    __tablename__ = 'address'
    user_ID = Column(String(128), ForeignKey("user.phone_number", ondelete="CASCADE"))
    address = Column(String(128))
    add_ID = Column(String(128), primary_key=True)


# 对象转json
def toJson(objs):
    if isinstance(objs, list):  # 判断对象是否为list
        obj_list = []
        for obj in objs:
            obj_list.append(obj)
        return json.dumps(obj_list, cls=new_alchemy_encoder(), check_circular=False, ensure_ascii=False)
    else:
        return json.dumps(objs, cls=new_alchemy_encoder(), check_circular=False, ensure_ascii=False)
