#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = David
# email:
from core import auth
from core import control

def login_run():
    print("欢迎登陆ATM")
    username = input("请输入用户名：").strip()
    password = input("请输入密码：").strip()
    a = auth.login(username)
    if a:
        if a.password == password:
            print("登陆成功，请输入您的操作：")
            """操作控制"""
            a.status(1)
            control.entrance(a)
        else:
            print("密码错误，请重新登录")
    else:
        print("用户名不存在")


def manage_run():
    from core import manage
    func_list = ["添加账户", "修改额度", "冻结账户"]
    print("请输入相应功能数字,输入任意字母退出")
    for k, v in enumerate(func_list, 1):
        print(k, v)
    i = input("请输入操作数字：")
    if int(i) == 1:
        manage.add_account()
    if int(i) == 2:
        print("修改额度")
    if int(i) == 3:
        manage.freeze_account()

if __name__ == "__main__":
    while True:
        # 用户登录
        role = input("欢迎使用ATM,登录请输入login，管理请输入manage").strip()
        if role == "login":
            login_run()
        if role == "manage":
            manage_run()


