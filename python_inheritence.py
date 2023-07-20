#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Person:  #creating parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Aleena", "Mary")
x.printname()


# In[20]:


class Person:  #creating child class 
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Irin", "Figi")
x.printname()


# In[21]:


class Person:   #__init Function
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Bitty", "Shatto")
x.printname()


# In[22]:


class Person:  #super function
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Dona", "Thomas")
x.printname()


# In[24]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Aleena", "Mary")
print(x.graduationyear)


# In[25]:


class Person:  #add methods
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Maria", "Sober", 2019)
x.welcome()


# In[26]:


mytuple = ("Apple", "Strawberry", "Grapes")  #iterators
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# In[27]:


mytuple = ("Apple", "Strawberry", "Cherry")  #looping through an iterator

for x in mytuple:
  print(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




