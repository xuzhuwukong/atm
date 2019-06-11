
import os
from cfgs import settings
import logging
import traceback


def loggerInFile(filename):  # 带参数的装饰器需要2层装饰器实现,第一层传参数，第二层传函数，每层函数在上一层返回
    def decorator(func):
        def inner(*args, **kwargs):  # 1
            logFilePath = settings.LOG_PATH + filename
            logger = logging.getLogger()
            logger.setLevel(settings.LOG_LEVEL)
            # sh = logging.StreamHandler()
            handler = logging.FileHandler(logFilePath)
            handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))
            logger.addHandler(handler)
            try:
                #print("Arguments were: %s, %s" % (args, kwargs))
                # logger.info(args)
                logger.info(args)
                result = func(*args, **kwargs)  # 2
            except:
                logger.error(traceback.format_exc())

        return inner

    return decorator

class account(object):
    login_status = False

    def __init__(self, name, password, balance,credit,rate,freeze):
        self.name = name
        self.password = password
        self.balance = balance
        self.credit = credit
        self.rate = rate
        self.freeze = freeze
    @loggerInFile("transfer")
    def transfer(self, numb, ab):
        self.balance -= numb
        ab.balance += numb

    def withdraw(self,numb):
        self.balance -= numb*(1+self.rate)

    @loggerInFile("payback")
    def payback(self,numb):
        self.balance +=numb

    def status(self,i):
        if i == 1:
            self.login_status = True
        else:
            self.login_status = False

    def login_c(func):
        def wrapper(self, *args, **kwargs):
            if self.login_status:
                func(self, *args, **kwargs)
            else:
                print("没有操作权限，请登录")
        return wrapper

    @login_c
    def check(self):
        print("当前余额是:",self.balance)






if __name__ == '__main__':

    import logging
    logging.error("hello")
    """
    import json
    m = account("li","123",155,1111,0.5)
    print(json.dumps(m, default =obj_2_json))
    jm = json.dumps(m, default =obj_2_json)
    m = json.loads(jm,object_hook=json_2_obj)
    print(type(m))

"""

#