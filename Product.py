# -*- coding:utf-8 -*-

class Product():
    def getProduct(self, data, myDatabase):
        return myDatabase.getProduct(data['ID'])

    def insertProduct(self, data, myDatabase):
        from Entity import Product
        product = Product(name=data['name'], ID=data['ID'], user_ID=data['user_ID'], picture=data['picture'],
                          start_price=data['start_price'], current_price=data['current_price'], time=data['time'],
                          state=data['state'], information=data['information'])
        return myDatabase.insertProduct(product)

    def deleteProduct(self, data, myDatabase):
        return myDatabase.deleteProduct(data['ID'])

    def getBanner(self, myDatabse):
        return myDatabse.getBanner()

    def getPageProduct(self, page, myDatabasse):
        return myDatabasse.getPageProduct(page)
