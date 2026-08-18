import numpy as np

arr=np.array([1,2,np.nan,4,np.nan,np.nan,6])

print(np.isnan(arr))

#note
print(np.nan==np.nan)