#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = 33
b = 200
if(b>a):
    print("b is greater")


# In[ ]:





# In[2]:


a=input("Enter first number:")
b=input("Enter second number:")
c=int(a)+int(b);
print(c)


# In[18]:


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=input("enter the operator")
result=0
if c=='+':
    result=a+b
    print(result)
elif c=='-':
    result= a-b
    print(result)
else:
    result=a*b
    print(result)

    


# In[21]:


import random
print(random.randrange(1,61))


# In[49]:


name = "Aleena Mary V S"
#for x in name:
print("Mary" in name) #check
print(name[0])
print(name[7:11]) #slicing
print(name[:6])
print(name[1:])
print(name[-6:-1]) #negative slicing
print(name.upper()) #modify strings
print(name.lower())
print(name.strip()) #white space remove
print(name.split()) #splitting,return type is list
print(name.replace('A','J')) #replacing


# In[15]:


fruits=["apple","grapes","strawberry"]
print(fruits[1])
fruits.append("blueberry") #added list item
fruits.append(1) #added list item
print(fruits)
print(fruits[1:3]) #accessing list items
fruits.insert(2,"banana") #inserting value to the list
print(fruits)
fruits.extend("mango")#extending to list
print(fruits)
print(len(fruits)) #length of the list
fruits.remove("banana") #removing data from list
print(fruits)
fruits.pop(9)#removing data from list
print(fruits)
del fruits[0]#removing data from list
print(fruits)


# In[17]:


a=[1,2,3]
a.clear()
a


# In[33]:


thislist = ["apple", "grapes", "cherry"] #for loop
for x in thislist:
    print(x)


# In[20]:


thislist = ["apple", "grapes", "cherry"] #for loop with range
for i in range(len(thislist)):
    print(thislist[i])


# In[40]:


fruits=["apple","grapes","strawberry","kiwi"] #list comprehension
newlist=[x for x in fruits if "a" in x]
print(newlist)


# In[46]:


thislist=["orange", "Mango", "kiwi", "pineapple", "Banana"]
thislist.sort()
print(thislist)


# In[47]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# In[50]:


def my_function():
    print("HELLO FROM A FUNCTION")
my_function()


# In[59]:


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Aleena", "Mary")


# In[60]:


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# In[66]:


def my_function(*kids):
    print(kids[1])

my_function("Aleena", "Mary")


# In[67]:


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# In[68]:


def my_function(country = "Norway"): #default parameter value
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# In[71]:


def my_function(food): #Passing a List as an Argument
    for x in food:
        print(x)
        
fruit=["apple","grapes"]
    
my_function(fruit)


# In[3]:


def my_fun(food):  #passing a list as argument
    for x in food:
        print(x)
fruit=["strawberry","grapes"]
my_fun(fruit)


# In[ ]:


def tri_rec(k):
    if(k>0):
        result=k+tri_rec(k-1)
        print (result)
    else:
        result=0
        return result


# In[4]:


def myfunc(n): #customize sort function
    return abs(n-50)

thislist=[100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)


# In[8]:


list1=["a","b","c"] #just referencing
list1.append(1)
list2=list1
print(list2)
print(list1)


# In[9]:


list1=["apple","grapes"] #copy list
list2=list1.copy()
print(list2)


# In[10]:


list1 = ["a", "b", "c"] #join list
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[12]:


list1=["a","b","c"]
list2=[1,2,3,3,3,3,4,3]
list3=list1+list2
print(list3)
list3.count(3)


# In[34]:


thislist = ["apple", "grapes", "strawberry"]  #while loop
i = 0
while i<len(thislist):
    print(thislist[i])
    i=i+1


# In[35]:


thislist=["apple","grapes","strawberry"] #list comprehension
[print(x) for x in thislist]


# In[52]:


a="Aleena"
b="Mary"
c="VS"
d=a+b+c
print(d)


# In[18]:


a = 10.0
b = 10
c = "Aleena"
d = True
e = 3 + 5j
f = None
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# In[26]:


cars =["HONDA","HONDA","BMW","VOLVO","SUSUKI"]
print(cars)
print(type(cars))
print(cars[0])
print(cars[0-2]) #excluding 2
print(cars[0:2])
cars.append("Tesla")
print(cars)


# In[33]:


cars= ("honda","BMW","SUZUKI","honda")
print(cars)
print(type(cars))
#cars.append("volvo")
print(cars[0])


# In[52]:


#cars= {1,5,20,4,3,11,9,10,5}
cars= {"Honda","BMW","SUZUKI","honda"}
print(cars)
print(type(cars))


# In[53]:


fruits = {"Tropical":["Apple","Grapes","Orange"],
         "Rate":["150","80","70"]}
print(fruits)
print(type(fruits))
print(fruits)


# In[1]:


thistuple = ("apple", "banana", "cherry")  #access tuple
print(thistuple[1])


# In[7]:


thisdict={"A":1,"a":1} #dict case sensitive
print(thisdict)
print(len(thisdict)) #length of dictionary


# In[23]:


cars={
    "brand":["ford","suzuki","Honda","Benz"],
    "models":["Ecosport","wagonar","Amaze","A3"],
    "price":[100000,250000,450000,500000]
}
print(cars)
x=cars["models"]
print(x)

x=cars.get("models")  #get()
print(x)

x=cars.values()  #values()
print(x)

x=cars.keys()  #keys()
print(x)

if "price" in cars: #in keyword
    print("yes")
else:
    print("no")
    
if "price" not in cars:  #not in keyword
    print("yes")
else:
    print("no")


# In[33]:


thisdict={ 
    "animal":["lion","cat","dog","tiger"], #list
    "wild":("lion","tiger"), #tuple
    "domestic":{"dog","cat"}, #set
    "boolean":("true") #boolean
    }
print(thisdict)


# In[38]:


thisdict={
    "dict":{"a":("mango","apple"), #tuple
           "b":{1,2},  #set
           "c":["lion","dog"],  #list
            "d":(None)
           }
}
print(thisdict)


# In[55]:


cars={
    "brand":["ford","suzuki","Honda","Benz"],
    "models":["Ecosport","wagonar","Amaze","A3"],
    "price":[100000,250000,450000,500000]
}

cars["price"][0]=5000000
print(cars)

del cars["price"][3]
print(cars)
  
cars.popitem()
print(cars)
    
del cars["brand"][1]
print(cars)
    
#cars["price"]=450000
#print(cars)
#cars.update("price"[]: 20020)
#print(cars)


# In[59]:


cars={
    "brand":["ford","suzuki","Honda","Benz"],
    "models":["Ecosport","wagonar","Amaze","A3"],
    "price":[100000,250000,450000,500000]
}

for x in cars["brand"]:
    print(x)


# In[61]:


cars={
    "brand":["ford","suzuki","Honda","Benz"],
    "models":["Ecosport","wagonar","Amaze","A3"],
    "price":[100000,250000,450000,500000]
}

mydict = cars.copy()
print(mydict)


# In[66]:


family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
     "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(family)


# In[ ]:


i = 1
while i < 6:
    print(i)
i += 1


# In[ ]:


for i in range(5):
    print(i)


# In[ ]:




