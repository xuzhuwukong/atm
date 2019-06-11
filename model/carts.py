from cfgs import settings
import json


class Carts(object):

    def user_cart(self,user):
        user_json = settings.DB_PATH + "\\" + user + ".cart"
        with open(user_json, "r", encoding="utf-8") as f:
            user_cart_dict = json.load(f)
        print("\033[41;36m您的余额\033[0m：", user_cart_dict['balance'][-1])
        # 打印消费记录
        print("您的消费记录：")
        for k, v in user_cart_dict['cart_history'].items():
            print("\033[41;36m已购商品\033[0m：", k, v)
            # 购物车有余额，可直接购买商品
        return user_cart_dict

if __name__ == '__main__':
    cart = Carts()
    print(cart.user_cart('lisi'))
