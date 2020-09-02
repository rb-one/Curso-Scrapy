my_list = [1,2,3,4,5]

## Normalmente usamos un for para recorrer la lista
# for element in my_list:
#     print(element)

## veamos que hay debajo
my_iter = iter(my_list)

print(type(my_iter))

#Extraer los elementos
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
