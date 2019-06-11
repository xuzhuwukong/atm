from cfgs import settings
import json

def write_json(f, j_dict):
    with open(f, "w", encoding='utf-8') as f:
        # json.dump(new_dict, f)
        json.dump(j_dict, f, ensure_ascii=False)


class Goods(object):

    def list_goods(self):  # 返回商品列表
        with open(settings.DB_PATH + "\\goods.json", "r", encoding="utf-8") as f:
            goods_list = json.load(f)
        return goods_list

    def buy_goods(self, user, user_cart_dict, goods_list):
        print("商品目录：")
        good_id_list = []
        goods = []   # 商品列表
        selected_goods = []
        current_balance = user_cart_dict['balance'][-1]
        for i, good in enumerate(goods_list, start=1):
            print("编号：{0}，商品：{1}，价格{2}".format(i, good.get('name'), good.get('price')))
            good_id_list.append(i)
            goods.append([good.get('name'), good.get('price')]) # 商品表格goods[["美女",100],["手机
        while True:
            good_id = input("请输入\033[41;36m商品编号\033[0m，结账请按c，退出购物请按q:").strip()
            if good_id.isdigit() and int(good_id) in good_id_list:
                # print(goods[int(good_id)][1])
                if user_cart_dict['balance'][-1] < goods[int(good_id)][1]:
                    print("当前余额不足，请购买其它商品：")
                    continue
                current_balance = current_balance - goods[int(good_id)][1]
                # cart_dict['cart_history']["2019-05-01 16:18:01"] = "test"
                selected_goods.append(goods[int(good_id)][0])
                print("\033[41;36m当前余额\033[0m:", current_balance)
                for i in selected_goods:
                    print("\033[41;36m已购商品\033[0m：", i)
            elif good_id == 'c':
                print("已结账")
                if len(selected_goods):
                    from collections import Counter
                    a = Counter(selected_goods)
                    di = {k: v for k, v in a.items()}
                    import datetime
                    str_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    user_cart_dict['cart_history'][str_time] = di
                    user_cart_dict['balance'].append(current_balance)
                continue
                #   cart[user][3] = cart[user][3] + 1
                # flag_continue = True
                # break
            elif good_id == 'q':
                print("退出购物！")
                if len(selected_goods):
                    write_json(settings.DB_PATH+"\\"+user+".cart", user_cart_dict)
                flag = True
                break
            elif not good_id.isdigit():
                print("输入编号不是整数,请重新输入：")
                continue
            else:
                print("输入编号不在商品编号中，请重新输入：")
                continue



if __name__ == '__main__':
    goods = Goods()
    print(goods.list_goods())
    from model import carts
    cart = carts.Carts()
    goods.buy_goods("lisi",cart.user_cart("lisi"),goods.list_goods())
