# -*- coding:utf-8 -*-
from MyDatabase import MyDatabase


class Product():
    myDatabase = MyDatabase()

    def getProduct(self, data):
        return self.myDatabase.getProduct(data['ID'])

    def insertProduct(self, data):
        from Entity import Product
        product = Product(name=data['name'], ID=data['ID'], user_ID=data['user_ID'], picture=data['picture'],
                          start_price=data['start_price'], current_price=data['current_price'], time=data['time'],
                          state=data['state'], information=data['information'])
        return self.myDatabase.insertProduct(product)

    def deleteProduct(self, data):
        return self.myDatabase.deleteProduct(data['ID'])
