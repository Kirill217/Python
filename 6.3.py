# -*- coding: utf8 -*-

f = open('users.txt', 'w', encoding='utf-8')
f.writelines('Иванов,Иван,Иванович\nПетров,Петр,Петрович')
f.close()

f = open('hobby.txt', 'w', encoding='utf-8')
f.writelines('скалолазание,охота\nгорные лыжи')
f.close()

from itertools import zip_longest
import json

dict_user_hobby = {}

with open('users.txt', encoding='utf-8') as users:
    with open('hobby.txt', encoding='utf-8') as hobby:
        line_users = sum(1 for line in users)
        line_hobby = sum(1 for line in hobby)

        if line_users < line_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for users_line, line_user_hobby in zip_longest(users, hobby):
            dict_user_hobby[users_line.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

# with open('task3.json', 'w', encoding='utf-8') as f:
#     json.dump(dict_user_hobby, f, ensure_ascii=False)
print(dict_user_hobby)

