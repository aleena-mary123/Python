#!/usr/bin/env python
# coding: utf-8

# In[5]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)


# In[9]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase9")


# In[10]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# In[11]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Aleena", "Trichur")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[12]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Aliya", "Ernamkulam")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[13]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Anand", "Kozhikodu")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[14]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
 ('Peter', 'Lowstreet 4'),
 ('Hannah', 'Mountain 21'),
 ('Michael', 'Valley 345'),
 ('Sandy', 'Ocean blvd 2'),
 ('Richard', 'Sky st 331'),
 ('Susan', 'One way 98'),
 ('Vicky', 'Yellow Garden 2'),
 ('Ben', 'Park Lane 38')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")


# In[16]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'canon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


# In[17]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


# In[18]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Ernakulam' WHERE address = 'Ernamkulam'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


# In[2]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Diljith", "abc")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[3]:


import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor=mydb.cursor()

sql="INSERT INTO customers (name,address) VALUES (%s,%s)"
val=("Bitty","Tcr")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record inserted.")


# In[4]:


import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase9"
)

mycursor=mydb.cursor()

sql="DELETE FROM customers WHERE address='one way 98'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record(s) deleted.")


# In[7]:


import mysql.connector
mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="mydatabase9"
)

mycursor=mydb.cursor()

sql="UPDATE customers SET address='Tsr' WHERE address='Tcr'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record(s) affected.")


# In[9]:


import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase9"
)

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE student (sname VARCHAR(250),scourse VARCHAR(250))")


# In[12]:


import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase9"
)

mycursor=mydb.cursor()

sql="INSERT INTO student (sname,scourse) VALUES (%s,%s)"
val=[
    ('Arnav','MBA'),
    ('April','Bcom'),
    ('Sidarth','MCA'),
    ('Susan','MCOM')
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,"record(s) inserted.")


# In[13]:


import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase9"
)

mycursor=mydb.cursor()

sql="DELETE FROM student WHERE scourse='MCOM'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record(s) deleted.")


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




