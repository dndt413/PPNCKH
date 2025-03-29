#series
import numpy
import pandas

myarray = numpy.array([1,2,3])
rownames = ["a", "b", "c"]
myseries = pandas.Series(myarray, index = rownames)

print(myseries)

print(myseries["a"])
# print(myseries[0])
# Đoạn code comment ở trên có thể bị lỗi ở 1 số version. 
# Tốt nhất để truy xuất theo vị trí thì nên dùng iloc
print(myseries.iloc[0])