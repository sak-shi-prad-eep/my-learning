import numpy as np

array=np.array(input().split(),dtype=int)
odd=array[array%2!=0]
print(odd)