class P:
    def __init__(self):
        self.total=0
    def accu(self,**kwargs):
        for i in kwargs:
            #self.total=self.total+sum(int(kwargs[i]))
            #print(self.total)
            print(i,kwargs[i])
class C1(P): pass

c1=C1()
c1.accu(n=1,b=5)
print (c1.__dict__)
