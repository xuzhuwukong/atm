import os
import json
from model import account

# 检查用户名文件是否存在，存在返回account，不存在返回None
def login(name):
    j = read_json(name)
    if j:
        a = json.loads(j,object_hook=json_2_obj)
        return a
    else:
        return None

def obj_2_json(obj):
    return {
        "name": obj.name,
        "password": obj.password,
        "balance": obj.balance,
        "credit": obj.credit,
        "rate": obj.rate,
        "freeze":obj.freeze
    }

def valid(name):
    from cfgs import settings
    file_name = settings.DB_PATH+name+".json"
    if os.path.isfile(file_name):
        return True
    else:
        return False

def read_json(name):
    from cfgs import settings
    file_name = settings.DB_PATH+name+".json"
    print(file_name)
    if os.path.isfile(file_name):
        file = open(file_name, 'r', encoding='utf-8')
        info = json.load(file)  #dict
        #print(type(info))
        #info = json.dumps(info) #dict转str
    else:
        info = None
    return info

def write2json(info):
    from cfgs import settings
    from core import auth
    file_name = settings.DB_PATH + info.name+".json"
    file = open(file_name, 'w', encoding='utf-8')
    info = json.dumps(info, default=auth.obj_2_json)
    json.dump(info,file)

def json_2_obj(d):
    return account.account(d['name'],d['password'],d['balance'],d['credit'],d['rate'],d['freeze'])
