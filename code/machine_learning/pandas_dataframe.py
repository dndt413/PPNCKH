# Data frame
import numpy
import pandas

myarray = numpy.array([[1,2,3], [4,5,6]])

rownames = ["a", "b"]
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
print("method 1:") 
print(f"one column: {mydataframe['one']}")
print("method 2:") 
print(f"one column: {mydataframe.one}")