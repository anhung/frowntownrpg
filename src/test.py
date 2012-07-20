'''
Created on Jul 19, 2012

@author: Annabel
'''

fp = open('../maps/walled_field.txt')

for a in fp.readlines():
    for b in range(len(a)):
        print a[b]