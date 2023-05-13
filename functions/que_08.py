#Write a Python function that takes a list and 
# returns a new list with distinct elements from the first list.
def new(lst):
    c=[i for i in set(lst)]
    return c
lst=['pillai','pillai','kerla','nikhil']
print(new(lst))
    