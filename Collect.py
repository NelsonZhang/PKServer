# -*- coding:utf-8 -*-


class Collect():
    def getCollect(self, data, myDatabase):
        return myDatabase.getCollect(data['user_ID'])

    def insertCollect(self, data, myDatabase):
        from Entity import Collect
        collect = Collect(user_ID=data['user_ID'], product_ID=data['product_ID'])
        return myDatabase.insertCollect(collect)

    def deleteCollect(self, data, myDatabase):
        return myDatabase.deleteCollect(data)
