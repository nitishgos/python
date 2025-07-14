class A:
    a=10
class B(A):
    b=20
class C(B):
    c=30
a=A()
b=B()
c=C()
print(a.a)
print(b.a,b.b)
print(c.a,c.b,c.c)