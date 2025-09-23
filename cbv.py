def fn(a):
    print(id(a))
    a=a+1
    print(id(a))
a=10
print(id(a))
fn(a)
print(id(a))