from re import L


def Depends(arg):
    print('DEPENDS')
    return arg


def hello(arg = Depends('1234')):
    print(arg)


hello()
