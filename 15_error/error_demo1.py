def model_exception(x,y):
    try:
        b=name
        a=x/y
    except(ZeroDivisionError,NameError,TypeError):
        print("one of error happend")

model_exception(2,0)
