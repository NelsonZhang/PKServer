# -*- coding:utf-8 -*-


class Indent():
    def getIndent(self, data, myDatabase):
        return myDatabase.getIndent(data['user_ID'])

    def insertIndent(self, data, myDatabase):
        from Entity import Indent
        indent = Indent(user_ID=data['user_ID'], product_ID=data['product_ID'], state=data['state'], time=data['time'],
                        number=data['number'], my_price=data['my_price'])
        return myDatabase.insertIndent(indent)

    def updataIndent(self, data, myDatabase):
        return myDatabase.updataIndent(data)
