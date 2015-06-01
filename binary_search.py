#!/usr/bin/env python

import sys

def bin_search(lst, key, first, last):
    if first > last:
        return False
    index = (first + last) / 2
    print "index is {0}".format(index)
    if key == lst[index]:
        print "found it: {0}".format(index)
        return True 
    if key < lst[index]:
        print "key is less {0}".format(index)
        bin_search(lst, key, first, index - 1)
    else:
        print "key is more {0}".format(index)
        bin_search(lst, key, index + 1, last)
    return index

def bin_search_iter(lst, key, first, last):
    if not last:
        last = len(lst)
    while True:
        if first > last:
            return False
        index = (first + last) / 2
        if lst[index] == key:
            print "found key @ index {0}".format(lst[index])
            return
        elif key < lst[index]:
           print "key is less, diff 1 on index @ {0}".format(lst[index])
           last = lst[index] - 1
        else:
           print "key is more, plus 1 to index @ {0}".format(lst[index])
           first = lst[index] + 1


lst = range(0, 100000)
key = 10 
print "key is {0}".format(key)
bin_search_iter(lst, key, 0, len(lst))
