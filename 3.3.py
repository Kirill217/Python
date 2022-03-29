# name_list = ["Кирилл", "Иван", "Алсу", "Драгаш", "Лиза"]


def names_dict(*names):
    end_dick = dict()
    for name in names:
        end_dick.setdefault(name[0], [])
        end_dick[name[0]].append(name)
    return end_dick

print(names_dict("Кирилл", "Иван", "Алсу", "Драгаш", "Лиза"))
# пытался сначала через списокв принтсделать, но понял что это нужно отдельнобрать индекс еще и для каждого элемента списка.