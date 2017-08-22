l1 = [1, 2, 3]
l2 = ['a', 'b']
l3 = ['+', '-']
res = [(i, j, k) for i in l1 for j in l2 for k in l3 if i > 1 and j == 'a']
print(res)
