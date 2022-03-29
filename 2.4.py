my_list = ["инженер-конструктор Игорь", "главный бухгалтер МАРиНа", "токарь высшего разряда нИКОЛАй", "директор аэлита"]
#
# for i in range(len(my_list)):
#     new_list = []
#     new1_list = i
#     list_my = list(reversed(new1_list.split(' ')))
#     list_my_1 = list_my[0]
#     list_my_1.append(new_list)
#     i = i + 1
#
# print(new_list)


# пытался что-то сделать, но у меня не получилось, запутался с форматом строки и инта


my_list_name_1 = my_list[0]
print(type(my_list_name_1))
my_list_name_2 = my_list[1]
# print(my_list_name_2.split(' '))
my_list_name_3 = my_list[2]
# print(my_list_name_3.split(' '))

# my_list_name_1_2 = my_list_name_1[1]
# print(type(my_list_name_1_2))

# my_list_name_1_2 = my_list_name_1.split(' ')
my_list_name_1_3 = list(reversed(my_list_name_1.split(' ')))
print(type(my_list_name_1_3))
my_str_1 = my_list_name_1_3[0]
print('Привет' , my_str_1.title())

# my_list_name_1_2 = my_list_name_1.split(' ')
# my_list_name_1_3 = list(reversed(my_list_name_1_2))
# # print(my_list_name_1_3)
# my_str_1 = my_list_name_1_3[0]
# print('Привет' , my_str_1.title())

my_list_name_2_2 = my_list_name_2.split(' ')
my_list_name_2_3 = list(reversed(my_list_name_2_2))
# print(my_list_name_2_3)
my_str_2 = my_list_name_2_3[0]
print('Привет' , my_str_2.title())

my_list_name_3_2 = my_list_name_3.split(' ')
my_list_name_3_3 = list(reversed(my_list_name_3_2))
# print(my_list_name_3_3)
my_str_3 = my_list_name_3_3[0]
print('Привет' , my_str_3.title())

