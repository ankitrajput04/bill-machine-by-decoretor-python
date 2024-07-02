def smartbill(fun):
    def inner(u,r):
        if(u>200):
            u = u-200
        
        return fun(u,r)
    return inner

@smartbill
def ebill(u,r):
    bill = u*r
    print(bill)

ebill(300,12)