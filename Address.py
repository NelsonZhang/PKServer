# -*- coding:utf-8 -*-


class Address():
    def getAddress(self, data, myDatabase):
        return myDatabase.getAddress(data['user_ID'])

    def insertAddress(self, data, myDatabase):
        from Entity import Address
        address = Address(user_ID=data['user_ID'], address=data['address'], add_ID=data['add_ID'])
        return myDatabase.insertAddress(address)

    def updataAddress(self, data, myDatabase):
        return myDatabase.updataAddress(data)

    def deleteAddress(self, data, myDatabase):
        return myDatabase.deleteAddress(data)
