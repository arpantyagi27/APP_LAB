t1 = (11, 2, 3, 14)
t2 = (13, 5, 22, 10)
t3 = (12, 2, 3, 10)
sum = tuple(map(lambda i, j, k: i + j + k, t1,t2,t3))
print(sum)