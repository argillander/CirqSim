
def func2(*args):
    testfunc(*args)

def testfunc(*args):
    for c in args:
        print(c)


func2(1,2,3,4,5)