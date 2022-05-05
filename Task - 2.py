import collections
import random
import numpy as np
import pandas as pd
from cmath import sqrt

data = []
for i in range(100):
    x = random.randint(0,1000)
    data.append(x)

def mean(data):
    sum = 0
    for i in range(len(data)):
        sum = sum + data[i]
    mean = sum / len(data)
    return mean


def median(data):
    length = len(data)
    data.sort()

    if length % 2 == 0:
        median1 = data[length // 2]
        median2 = data[length // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = data[length // 2]

    return median


def mode(data):
    data = collections.Counter(data)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(data):
        print("No mode in the list")
    else:
        return mode_val
    return -1


def Value_from_percentile(a):
    return np.percentile(data,a)

mean = mean(data)
median = median(data)
mode = mode(data)

df1 = pd.DataFrame(data, columns =['Original'])
df1['QuantileRank']= pd.qcut(df1['Original'],q = 4, labels = False)
df1['DecileRank'] = pd.qcut(df1['Original'], q = 10, labels = False)
df1['Percentile'] = pd.qcut(df1['Original'], q = 100, labels = False)
print(df1)

print("\nOriginal Value : ",Value_from_percentile(100))
print("Mean of Population : ", mean, "\nMedian of Population : ", median, "\nMode of Population : ", *mode)