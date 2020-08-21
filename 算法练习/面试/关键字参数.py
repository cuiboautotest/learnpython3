def demo(args_f,*args_v):
    print(args_f)
    for x in args_v:
        print(x)
    print(args_v)

demo('a','b','c','d')