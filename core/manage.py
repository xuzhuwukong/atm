from model import account
from core import auth


def add_account():
    user = input("请输入用户名：").strip()
    if auth.valid(user):
        print("用户名已存在")
    else:
        a = account.account(user,"111111",0,15000,0.0005,0)
        auth.write2json(a)
        print("账户创建成功")


def freeze_account():
    user = input("请输入用户名：").strip()
    if not auth.valid(user):
        print("用户名不存在")
    else:
        a = auth.read_json(user)
        print(a)
        a = auth.json_2_obj(eval(a))
        a.freeze = 1
        auth.write2json(a)
        print("账户已冻结")


if __name__ == "__main__":
    freeze_account()
