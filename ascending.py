#!/usr/bin/python3
temp=input('Enter words separated by comma: ')
string=temp.split(',')
string.sort()
print(','.join(string))
