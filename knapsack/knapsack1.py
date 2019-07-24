
import math

import numpy as np
import pandas as pd
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.5f}'.format

items = pd.read_csv("items.csv", sep=",")
# 2 columns weight and value

items["values_per_weight"] = items["value"] / items["weight"]
items["orig_index"] = items.index
# ordine casuale e normalizzazione del valore

arr_items = items.to_numpy()
#print(arr_items[:3,:])




def knapstack(wmax,nmax,items):
    sorted_items = items[items[:,1].argsort()[::-1]]
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
    print("Tot. weight %s" % w)
    print("Tot. value %s" % v)
    print("Items: weight, value, index")
    print(out)
    w = 0
    v = 0
    for i in out:
        print("%s %s %s" % (items[i][0], items[i][1], i))
        w = w + items[i][0]
        v = v + items[i][1]
    print("Check weight %s and value %s" % (w,v))
    print("---------------------")
        
knapstack(15,6,arr_items)
knapstack(20,12,arr_items)
knapstack(20,50,arr_items)

