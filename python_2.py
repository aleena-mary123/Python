#!/usr/bin/env python
# coding: utf-8

# In[3]:


for i in range(5,16):
    print(i)


# In[4]:


x=lambda a:a+10
print(x(4))


# In[2]:


def myfun(a:a+10):
    myfun(4)


# In[13]:



fruits=["apple","strawberry","grapes"]
print(type(fruits))


# In[16]:


import numpy as np
a=np.array(["apple","banana"])
print(a)
print(type(a))


# In[31]:


import random 
a=random.random()
print(a)


# In[26]:


from numpy import random
i=random.randint([5,20,21,3,5])
print(i)
print(type(i))


# In[36]:


class Myclass:      #class class_name
    x=5
m1=Myclass()
print(m1.x)
    


# In[46]:


class student:
    def __init__(s,x,y):  #def __init__(self,x,y)
        s.name=x
        s.age=y
s1=student("Aleena",22)
print(s1.name)
print(s1.age)
    


# In[48]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Aleena", 22)
p1.myfunc()

