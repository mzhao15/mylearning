
#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
#myvalues = np.array(values)

plt.figure(1)
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
#plt.show()

plt.figure(2)
plt.bar(names, values)
plt.bar(names, [num*2 for num in values])
plt.show()

'''
plt.figure(2)

line = plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

#print(plt.setp(line))

plt.close()
'''