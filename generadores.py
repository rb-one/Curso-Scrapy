def my_gen():
    a = 1
    yield a

    a= 2 
    yield a

    a = 3
    yield a


my_first_gen = my_gen()

print(next(my_first_gen))
print(next(my_first_gen))
print(next(my_first_gen))

