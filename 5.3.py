tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

my_gen = ((tutol, klasse) for tutol, klasse in zip(tutors, klasses)) # ох как же долго я патылся понять что запись именно такая,
# а не такая (tutors, klasses) for tutors, klasses
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


