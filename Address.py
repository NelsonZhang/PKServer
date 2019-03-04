# -*- coding:utf-8 -*-
from MyDatabase import MyDatabase


class Address():
    myDatabase = MyDatabase()

    def getAddress(self, data):
        return self.myDatabase.getAddress(data['user_ID'])

    def insertAddress(self, data):
        from Entity import Address
        address = Address(user_ID=data['user_ID'], address=data['address'], add_ID=data['add_ID'])
        return self.myDatabase.insertAddress(address)

    def updataAddress(self, data):
        return self.myDatabase.updataAddress(data)

    def deleteAddress(self, data):
        return self.myDatabase.deleteAddress(data)
