import collections
from math import sqrt
import pandas as pd
import random

dataset = pd.read_csv("E:/Downloads/archive/Used_fiat_500_in_Italy_dataset.csv")
clm = dataset["price"]

sample = clm.iloc[0:20]

def mean(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    mean = sum / len(lst)
    return mean


def median(lst):
    lst = list(lst)
    length = len(lst)
    for i in range(1, length):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

    if length % 2 == 0:
        median1 = lst[length // 2]
        median2 = lst[length // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = lst[length // 2]
    return median


def mode(lst):
    data = collections.Counter(lst)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(lst):
        print("No mode in the list")
    else:
        return mode_val
    return -1


def standard_Deviation(lst, mean):
    length = len(lst)
    SUM = 0
    for i in lst:
        SUM += (i - mean) ** 2
    stdev = sqrt(SUM / (length - 1))

    return stdev


def variance(lst, mean):
    length = len(lst)
    sum2 = 0
    for i in range(length):
        sum2 = sum2 + (lst[i] - mean) ** 2
    myvar = sum2 / length

    return myvar


# mean = mean(clm)
# median = median(clm)
# mode = mode(clm)
# standard_deviation = standard_Deviation(clm, mean)
# variance = variance(clm, mean)
mean_sample = mean(sample)
median_sample = median(sample)
mode_sample = mode(sample)
standard_deviation_sample = standard_Deviation(sample, mean_sample)
variance_sample = variance(sample, mean_sample)

# print("Mean of Population : ", mean, "\nMeadian of Population : ", median, "\nMode of Population : ", mode,
#       "\nStandard Deviation of Population : ", standard_deviation, "\nVariance of Population : ", variance,"Range of Population : ",max(clm)-min(clm))
print("Mean of Sample : ",mean_sample,"\nMedian of Sample : ", median_sample, "\nMode of Sample : ", mode_sample,"\nStandard Deviation of Sample : ",standard_deviation_sample,"\nVariance of Sample : ",variance_sample,"\nRange of Sample : ",max(sample)-min(sample))
