# -*- coding:utf-8 -*-
from MyDatabase import MyDatabase


class Indent():
    myDatabase = MyDatabase()

    def getIndent(self, data):
        return self.myDatabase.getIndent(data['user_ID'])

    def insertIndent(self, data):
        from Entity import Indent
        indent = Indent(user_ID=data['user_ID'], product_ID=data['product_ID'], state=data['state'], time=data['time'])
        return self.myDatabase.insertIndent(indent)

    def updataIndent(self, data):
        return self.myDatabase.updataIndent(data)
