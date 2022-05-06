a = (2 and 3 in range(1,6))
print("a é",a)

b = (2 and 6 in range(1,6))
print("b é",b)

c = (((1 and 6) or (5 and 6)) in range(1,6))
print("c é",c)

d = ((1 and 6) or (5 and 6)) in range(1,6)
print("d é",d)

e = (10 or 2) in range(1,6)
print("e é",e)

f = (2 or 20) in range(1,6)
print("f é",f)