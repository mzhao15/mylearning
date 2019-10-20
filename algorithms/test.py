
#import pandas as pd

import sys
import os
import datetime
import numpy as np
import json


a = np.arange(15).reshape(3, 5)

arr = np.array([2,3,4])
b = np.array([(1.5,2,3), (4,5,6)])

# print(type(arr))
# print(arr.dtype)
print(np.random.random((2,3)))

dicts = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

dicts2 = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(dicts2[1]['bar'])
print(type(dicts2))

for i in range(10):
    print(i)