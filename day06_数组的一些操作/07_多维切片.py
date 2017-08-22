# l = [i for i in range(10)]
# a, b = l[0:3, 4:5]
# print(a+b)
# 得出结论，多维切片在内置序列中不能用

# 多维切片在numpy中使用
import numpy
# l1 = numpy.ndarray(1, 2, 3)
l2 = numpy.array([i for i in range(10)])
a = l2[0:3]
print(a)
