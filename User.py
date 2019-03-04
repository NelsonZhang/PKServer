# -*- coding:utf-8 -*-
from MyDatabase import MyDatabase


class User():
    myDatabase = MyDatabase()

    def getUser(self, data):
        return self.myDatabase.getUserData(data['phone_number'])

    def addUser(self, data):
        from Entity import User
        user = User(name=data['name'], phone_number=data['phone_number'], password=data['password'],
                    avatar=data['avatar'])
        return self.myDatabase.insertUserData(user)

    def updataUser(self, data):
        return self.myDatabase.updataUserData(data)
