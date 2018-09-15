class P:
  def foo(self):
    print("foo\n")

class C1(P):
    def foo(self):
      print("c1foo\n")
      P.foo(self)

class C2(P):
    def foo(self):
        print("c2foo\n")
        super().__init__()
p=P()
c1=C1()
c2=C2()

p.foo()
c1.foo()
c2.foo()
