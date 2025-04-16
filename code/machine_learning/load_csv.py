# Load CSV Using Python Standard Library 
import csv 
import numpy 
filename = '../../data/machine_learning/pima-indians-diabetes.data.csv' 
raw_data = open(filename, 'r') 
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE) 
x = list(reader) 
data = numpy.array(x).astype('float') 
print(data.shape)