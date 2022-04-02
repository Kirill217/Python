src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
num_more = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0] # 2,5 часа чтб понять как это сделать
# и так и не понять до конца, спасибо интернету что помог
print(num_more)