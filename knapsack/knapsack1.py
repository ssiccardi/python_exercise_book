
import math
import time
import numpy as np
import pandas as pd

pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.5f}'.format

items = pd.read_csv("items.csv", sep=",")
# 2 columns weight and value

#items["values_per_weight"] = items["value"] / items["weight"]
#items["orig_index"] = items.index

arr_items = items.to_numpy()
#print(arr_items[:3,:])




def knapstack(wmax,nmax,items):
    items1 = np.c_[items, np.zeros(items.shape[0]),np.zeros(items.shape[0])]
    for i in range(items.shape[0]):
        items1[i][2] = items1[i][1]/items1[i][0]
        items1[i][3] = i
    sorted_items = items1[items1[:,1].argsort()[::-1]]
    #print(sorted_items[:3,:])
    w = 0
    v = 0
    n = 0
    out = []
    i = 0
    while True:
        if n == nmax:
            break
        if w+sorted_items[i][0] < wmax:
            out.append(int(sorted_items[i][3]))
            w = w+sorted_items[i][0]
            v = v + sorted_items[i][1]
            n = n + 1
        i = i+1
        if i>=sorted_items.shape[0]:
            break
#    print("Tot. weight %s" % w)
#    print("Tot. value %s" % v)
#    print(out)

    sorted_items1 = items1[items1[:,2].argsort()[::-1]]
    #print(sorted_items[:3,:])
    w1 = 0
    v1 = 0
    n1 = 0
    out1 = []
    i = 0
    while True:
        if n1 == nmax:
            break
        if w1+sorted_items1[i][0] < wmax:
            out1.append(int(sorted_items1[i][3]))
            w1 = w1+sorted_items1[i][0]
            v1 = v1 + sorted_items1[i][1]
            n1 = n1 + 1
        i = i+1
        if i>=sorted_items1.shape[0]:
            break
#   print("Tot. weight %s" % w1)
#   print("Tot. value %s" % v1)
#    print(out1)
    if v>v1:
        return out
    else:
        return out1
        
t1 = time.time()        
out = knapstack(15,6,arr_items)
t2 = time.time()-t1
print("Elapsed %s" % t2)

w = 0
v = 0
#print("Items: weight, value, index")
for i in out:
#    print("%s %s %s" % (arr_items[i][0], arr_items[i][1], i))
    w = w + arr_items[i][0]
    v = v + arr_items[i][1]
print("Check weight %s and value %s" % (w,v))
print("---------------------")

t1 = time.time()        
out = knapstack(20,12,arr_items)
t2 = time.time()-t1
print("Elapsed %s" % t2)

w = 0
v = 0
#print("Items: weight, value, index")
for i in out:
#    print("%s %s %s" % (arr_items[i][0], arr_items[i][1], i))
    w = w + arr_items[i][0]
    v = v + arr_items[i][1]
print("Check weight %s and value %s" % (w,v))
print("---------------------")

t1 = time.time()        
out = knapstack(20,50,arr_items)
t2 = time.time()-t1
print("Elapsed %s" % t2)

w = 0
v = 0
#print("Items: weight, value, index")
for i in out:
#    print("%s %s %s" % (arr_items[i][0], arr_items[i][1], i))
    w = w + arr_items[i][0]
    v = v + arr_items[i][1]
print("Check weight %s and value %s" % (w,v))
print("---------------------")

