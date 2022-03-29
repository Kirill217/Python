given_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
'была', '+5', 'градусов']


# print(given_list)
# new_str = ' '.join(given_list)

out_1 = given_list.pop(1) # уже является строкой
out_2 = given_list.pop(2)
out_3 = given_list.pop(6)

# print(given_list)
# print(out_1 , out_2, out_3)

# print(type(out_1))
# print(type(given_list))

# print(out_3.isdigit())

if out_3.isdigit() == True:
    out_3_1 = out_3     #если строка состоит из чисел то то вывести его
    # print(out_3_1)
else:
    out_3_1 = out_3[1:]    # если строка состои не из чисел то сделать срез знака перед числом
    # print(out_3_1)

# out_1_1 = f'"{int(out_1):02}"'
# out_2_1 = f'"{int(out_2):03}"'  # вижу проблему в том, что если число не двухзначное то будет лишний ноль!
# sign = out_3[:1] # верну знак, что был в начале
# out_3_1_1 = f'"{sign}{int(out_3_1):02}"' # но теперь нужно вернуть необходимый знак

out_1_1 = f'"0{out_1}"'
if int(out_2) < 10:
    out_2_1 = f'"0{out_2}"'
else:
    out_2_1 = f'"{out_2}"'# вот тут вроде как такой проблемы быть не должно, но мне кажется это ужас какие костыли

sign = out_3[:1] # верну знак, что был в начале
if int(out_3_1) < 10:
    out_3_1_1 = f'"{sign}0{out_3_1}"'
else:
    out_3_1_1 = f'"{sign}{out_3_1}"' # но теперь нужно вернуть необходимый знак (сделал)


# print(out_1_1)
# print(out_2_1)
# print(out_3_1_1)

given_list.insert(1, out_1_1)
given_list.insert(3, out_2_1)
given_list.insert(8, out_3_1_1)

new_str = ' '.join(given_list)

print(new_str)