# encoding=utf-8
import numpy
from scipy import stats
import matplotlib.pyplot

s = [20, 25, 30, 35, 35]

x = numpy.mean(s)  # 平均数‘
y = numpy.median(s)  # 中位数
z = stats.mode(s)  # 众数
c = numpy.std(s)  # 标准差
v = numpy.var(s)  # 方差
b=numpy.random.uniform(5,10,100)

print(x)
print(y)
print(z)
print(c)
print(v)
print(b)

matplotlib.pyplot.hist(b, 5)
matplotlib.pyplot.show()

print(type(v))
print(type(1))
print(5.830951894845301 * 5.830951894845301)
