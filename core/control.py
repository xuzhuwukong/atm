#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = David
# email:

from core import auth

func_list=["转账","提款","还款","查询","购物"]

def entrance(acc):
    from core import auth
    while True:
        print("请输入相应功能数字,输入任意字母退出")
        for k,v in enumerate(func_list,1):
            print(k,v)
        a = input("输入：").strip()
        if a.isdigit():
            a = int(a)
            if a == 1:
                num = input("请输入转账金额：").strip()
                b = input("请输入对方用户名：").strip()
                if num.isdigit() and auth.valid(b):
                    jb = auth.read_json(b)
                    b = auth.json_2_obj(eval(jb))
                    acc.transfer(float(num),b)
                    print(b.balance,b.name)
                    auth.write2json(b)
                else:
                    print("输入错误")
            elif a ==2:
                num = input("请输入提款金额：").strip()
                if num.isdigit():
                    acc.withdraw(float(num))
                else:
                    print("输入错误")
            elif a ==3:
                num = input("请输入还款金额：").strip()
                if num.isdigit():
                    acc.payback(float(num))
                else:
                    print("输入错误")
            elif a==4:
                acc.check()
            elif a==5:
                from model import goods
                goods = goods.Goods()
                goods_list = goods.list_goods()
                from model import carts
                cart = carts.Carts()
                goods.buy_goods(acc.name, cart.user_cart(acc.name), goods.list_goods())
            else:
                print("数字错误，请重新输入数字")
        else:
            acc.status = False
            auth.write2json(acc)
            break
if __name__ == "__main__":
    entrance()