import yaml
import os

curpath=os.path.dirname(os.path.realpath(__file__))
yamlpath=os.path.join(curpath,'cfg.yaml')
print(yamlpath)

#open方法直接读出来
f=open(yamlpath,'r',encoding='utf-8')
cfg=f.read()
print(cfg)
print(type(cfg))#读出来是字符串

d=yaml.load(cfg,Loader=yaml.FullLoader)#load方法转为字典,要加上loader参数
print(d)
print(type(d))


