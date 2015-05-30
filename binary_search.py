#!/usr/bin/env python

def bin_search(lst, key, frm, to):
    if not to:
        to = len(lst)
    if not frm:
        frm = 0
    mid = ((frm + to) / 2) 
    if key > lst[mid]:
        bin_search(lst, key, lst[mid]+1, len(lst))
    elif key < lst[mid]:
        bin_search(lst, key, 0, lst[mid]-1)
    else:
        print "found it => {0}".format(key) 


lst = range(0,20)
key = 15 
bin_search(lst, key, 0, len(lst))
