def info(*args,**kwargs):
    print(args)    #('alex', 18, 'male')
    print(kwargs)   #{'hight': 175, 'job': 'it'}

info('alex',18,'male',job = 'it',hight = 175)  #无名的放前面,有名的放后面
'''
.函数不定长参数*args和**kwargs只能放在形参的末尾，顺序不能错
'''