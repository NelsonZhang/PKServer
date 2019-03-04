# -*- coding:utf-8 -*-
from MyDatabase import MyDatabase


class Collect():
    myDatabase = MyDatabase()

    def getCollect(self, data):
        return self.myDatabase.getCollect(data['user_ID'])

    def insertCollect(self, data):
        from Entity import Collect
        collect = Collect(user_ID=data['user_ID'], product_ID=data['product_ID'])
        return self.myDatabase.insertCollect(collect)

    def deleteCollect(self, data):
        return self.myDatabase.deleteCollect(data)
