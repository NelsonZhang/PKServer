# -*- coding:utf-8 -*-


class User():
    def getUser(self, data, myDatabase):
        return myDatabase.getUserData(data['phone_number'])

    def addUser(self, data, myDatabase):
        from Entity import User
        user = User(name=data['name'], phone_number=data['phone_number'], password=data['password'],
                    avatar=data['avatar'], userSig=data['userSig'])
        return myDatabase.insertUserData(user)

    def updataUser(self, data, myDatabase):
        return myDatabase.updataUserData(data)
