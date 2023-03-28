#!/usr/bin/env python
# coding: utf-8

# In[58]:


class Node:
    def __init__(self, value=None,next=None):
        self.value=value
        self.next=next
def found( valueX ):
    kekW=first_node
    while kekW.value!=None:
        if kekW.value==valueX:
            return True
        else:
            kekW=kekW.next
    return False

a=input().split() #ввод данных через пробел
b=input()         #элемент который хотим найти
        
first_node = Node() 
lulW = first_node

for i in range(len(a)): #преобразование в односвязный список
    lulW.value=a[i]
    lulW.next=Node()
    lulW=lulW.next

print(found(b))


# In[ ]:




