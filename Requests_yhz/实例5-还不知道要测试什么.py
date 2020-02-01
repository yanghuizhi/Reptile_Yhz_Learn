def gen_squares(num):
    for x in range(num):
        yield x ** 2

a=gen_squares(2)
print(a.__next__())
print(a.__next__())
print(next(a))