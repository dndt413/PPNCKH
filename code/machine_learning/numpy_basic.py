# define an array 
import numpy as np
mylist = [1, 2, 3] 
myarray = np.array(mylist) 
print(myarray) 
print(myarray.shape)


# Access values 
mylist1 = [[1, 2, 3], [3, 4, 5]] 
myarray = np.array(mylist1) 
print(myarray) 
print(myarray.shape) 
print(f"First row: {myarray[0]}")
print(f"Last row: {myarray[-1]}")
print(f"Specific row and col: {myarray[0,2]}")
print(f"Whole col: {myarray[:, 2]}")

# arithmetic 
myarray1 = np.array([2, 2, 2]) 
myarray2 = np.array([3, 3, 3]) 
print(f"Addition: {myarray1 + myarray2}")
print(f"Multiplication: {myarray1 * myarray2}")