def my_generator(num):
    for i in range(num):
        x= i+1
        yield x
    return x

iter = my_generator(10)

print(next(iter))
print(next(iter))
def genr(num):
    for i in range(num):
        if i%2==0:
            x=i
            yield x
    print(type(x))
    return x

returned = genr(10)
print(type(returned))
for j in returned:
    print(j)



