# Write a Python program to sort a given dictionary by key
from collections import OrderedDict
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
print(OrderedDict(sorted(color_dict.items())))