# -*- coding:utf-8 -*-
from Product import Product
from User import User
from MyDatabase import MyDatabase

mydatabase = MyDatabase()
product = Product()
data = {"phone_number": "15736506524"}
print  product.getPageProduct(1, mydatabase)

# data = {"information": None, "user_ID": "15736506524\r\n", "name": "头发",
#         "picture": "http://img4.imgtn.bdimg.com/it/u=2430963138,1300578556&fm=23&gp=0.jpg", "start_price": 1200.0,
#         "state": 0, "time": "2019-03-05 11:55:39", "current_price": 1200.0, "ID": "006"}


# print mydatabase.getUserData(data)
