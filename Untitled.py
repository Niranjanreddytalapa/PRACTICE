#!/usr/bin/env python
# coding: utf-8

# In[1]:


s1 = """Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Wikipedia"""


# In[3]:


s1 = """Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Wikipedia"""
    
    


# In[4]:


print(len(s1))


# In[2]:


print(s1([0])


# In[6]:


print(s1[0])


# In[7]:


print(s1[0: 6])


# In[9]:


print(s1[0:186])


# In[10]:


print(s1[-100])


# In[11]:


print(s1[:])


# In[13]:


print(s1[0:120:3])


# In[15]:


print(s1[-10: :2])


# In[16]:


print(s1[:: -1])


# In[17]:


print(s1[:: -2])


# In[18]:


s = 'upsc is not so easy'
print(s.upper())


# In[19]:


print(s.lower())


# In[20]:


print(s.swapcase())


# In[24]:


su= 'Niranjan Reddy'
s1= 'Python'
s2= '9963023794


print(su.isupper(),s1.islower)'


# In[25]:


### validating indian mobile number


- +91
- 10 digits
- 9,8,7,6


# In[30]:


n1 = '+919381990849'
n2 = '9963023794'
n3 = '+915441285280'


if n1[0] == '+':
    if n1[1:3] == '91'and len(n1[3: ]) == 10 and n1[3] in '9876':
        print(n1, 'is valid indian mobile number')
    else:
        print(n1,'is not indain valid number')
elif len(n1) == 10 and n1[0] in '9876':
    print(n1, 'is valid indian mobile number')
else:
    print(n1, 'is not valid indian mobile number')


# In[32]:


rollNo = "182U1A04G5"

print(rollNo.startswith('18'))


# In[33]:


email = 'talapareddyniranjanreddy@gmail.com'
email2 = 'aha42808@gmail.com'


# In[34]:


print(email.endswith('@gmail.com'))


# In[35]:


print(email2.endswith('.com'))


# In[36]:


email = 'talapareddyniranjanreddy@gmail.com'
email2 = 'aha42808@gmail.com'
print(email.index('@'))


# In[37]:


print(email[0:24])


# In[38]:


print(email2[0:email2.index('@')])


# In[39]:


email = 'talapareddyniranjanreddy@gmail.com'
email2 = 'aha42808@gmail.com'
email3 = 'jjj22222@yahoo.com'


print(email2[email2.index('@') + 1: email3.index('.')])


# In[40]:


help(str.index)


# In[42]:


email = 'nj@gmail@in'

print(email.index('@'))


# In[43]:


email = 'nj@gmail@in'

print(email.index('@', 5))


# In[44]:


len(email)


# In[45]:


print(email.count('@'))


# In[46]:


print(email.count('nj'))


# In[50]:


s = '((((APSSDc python))))'


print(s.lstrip('('),s.rstrip(')'),s.strip('()'))


# In[51]:


s1 = """"Python was named after the BBC TV show Monty Python's Flying Circus. Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode. However, the most important change was to the development process itself, with a shift to a more transparent and community-backed process."""


# In[52]:


print(s1.title())


# In[53]:


print(s1.istitle())


# In[54]:


s1 = """Python Was Named After The Bbc Tv Show Monty Python'S Flying Circus. Python 2.0 Was Released On October 16, 2000, With Many Major New Features, Including A Cycle-Detecting Garbage Collector (In Addition To Reference Counting) For Memory Management And Support For Unicode. However, The Most Important Change Was To The Development Process Itself, With A Shift To A More Transparent And Community-Backed Process."""


# In[55]:


print(s1.istitle())


# In[58]:


certificate = "i'm certify that {} from geethanjali institue ,on program,from date".format('Niranjan')

print(certificate)


# In[59]:


s = 'asdfg'
s2 = 'asd456'

print(s.isalpha(),s2.isalnum)


# In[60]:


s1 =  """"Python was named after the BBC TV show Monty Python's Flying Circus. Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode. However, the most important change was to the development process itself, with a shift to a more transparent and community-backed process."""


# In[61]:


for char in s1:
    
    print(char)


# In[62]:


""""Python was named after the BBC TV show Monty Python's Flying Circus. Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode. However, the most important change was to the development process itself, with a shift to a more transparent and 2001community-backed process."""


# In[63]:


s1 = """"Python was named after the BBC TV show Monty Python's Flying Circus. Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode. However, the most important change was to the development process itself, with a shift to a more 0028transparent and community-backed process."""


# In[66]:


for char in s1:
    if char.isalpha():
        print(char,end = '\t') 


# In[68]:


for char in s1:
    if char.isdigit():
        print(char,end = '\t')


# In[72]:


ac =0
nc=0
sc=0

for char in s1:
    if char.isalpha():
        ac+=0
    elif char.isdigit():
        nc+=0
    else:
        sc+=0
print('Alpha',ac,'Digits',nc'Special Charac',sc)


# In[ ]:


### lists

it is used to store the non homogenous group of valid datatypes in python

###properties
- list mutable data type
-list is an ordered data
-It is iterable
it is declared as []


# In[73]:


list1 = [1,22,1]
list2 = [22,5,2,4]


# In[74]:


print(list1 and list2 )


# In[75]:


print(append.list1 and list2)


# In[76]:


li =[]
li2 = list()


# In[77]:


print(type(li),type(li2))


# In[ ]:


li = [5,5.5,5+6j]

