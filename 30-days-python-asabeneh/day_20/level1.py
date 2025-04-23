import os
import json
from statistics import median
from pathlib import Path
import requests
import math
from itertools import filterfalse
# used to remove false values
# from day_19 import level2
# res=requests.get()
# print(level2.find_most_common_words_url("https://www.gutenberg.org/cache/epub/1112/pg1112.txt"))

# TypeError: write() argument must be str, not list, not set, not dict, not Counter, nor tuple
# also need to import requests,re externally on terminal
#  Also on terminal we have to recursively exit terminal after making changes in imported files
import numpy as np
# from day_05 import level2
# Initialize a dictionary with numeric values
data = requests.get('https://api.thecatapi.com/v1/breeds')

# print("Original dictionary with numeric values:",data.json())
list_main = data.json()
# print(type(list_main))
dict=list_main
dict2={}
dict2['data']={}
for n in range(len(list_main)-1):
        str=dict[n].get('weight',0)# for first {'imperial': '12 - 18', 'metric': '5 - 8'}1
        str=str['imperial'].replace(' ','')
        str=str.split('-')
        #print(str)
        str=[int(i) for i in str]
        dict[n]['weight']=sum(str)/len(str)
        dict2['data'][n]=dict[n]['weight']

def bsort(processed_dict):
    for n in range(len(processed_dict)-1,0,-1):
        for i in range(n):
            if(processed_dict[i]>processed_dict[i+1]):#TypeError: '>' not supported between instances of 
# 'dict' and 'dict' vb ??remove ['weight]
                temp=processed_dict[i+1]
                processed_dict[i+1]=processed_dict[i]
                processed_dict[i]=temp
    return processed_dict
sorted_dict=bsort(dict2['data'])
med=median(sorted_dict)
print(f'Minimum value is {sorted_dict[0]}')
print(f'Maximum value is {sorted_dict[len(sorted_dict)-1]}')
sum=0
for item in sorted_dict:
     sum=sum+math.pow(item-med,2)/len(sorted_dict)
print(f'Mean value is {sum/len(sorted_dict)}')
# Convert the dictionary values to a NumPy array
# numpy_array = np.array(list(list_main.values()))
# print("\nDictionary values to a NumPy array")

# # Print the NumPy array
# print(numpy_array)
# print(type(numpy_array))


# print(bsort(ages))