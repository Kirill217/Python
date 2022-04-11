def createGenerator() :
    mylist = range(16)
    for i in mylist:
       yield i

my_generator = createGenerator() # создаём генератор
print(my_generator)
for num in my_generator:
    print(num)