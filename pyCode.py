import numpy as np
a = np.array([[1,-3],[1,1]])
b = np.array([[0],[100]])
x = np.linalg.solve(a, b)
print(x) 
print('price of the small fish: ',x[0])
print('price of the big fish: ',x[1])