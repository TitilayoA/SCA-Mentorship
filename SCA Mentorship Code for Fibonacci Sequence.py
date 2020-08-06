#!/usr/bin/env python
# coding: utf-8

# ## Python code for generating a Fibonacci sequence
# #### This notobook cover 3 different methods that can be used to generate a Fibonacci Sequence

# In[1]:


#Method 1
#We started by creating a function that will house the sequence
def F(n):
    a,b = 0,1 #Assign 0 to a variable 'a' and  1 to variable b which will be 1st and 2nd number number in the sequence
    for i in range(n):
        print(a) #using the print keyword to return variable "a" as the first number in the output
        a,b = b, a+b #this is the fibonacci generator expression
i = F(10)


# In[2]:


#Method 2, this is quite similar to Method 1, but uses the yield keyword
def F_ab(n):
    a,b = 0,1
    for i in range(n):
        yield a #using the yield keyword as the generator function
        c=a+b #assigning into a variable
        a,b = b, c #this is the fibonacci generator expression


# In[3]:


for i in F_ab(10): #A command line to print the first 10 numbers in the fibonacci sequence
    print(i)


# In[4]:


#putting the sequence in a list
list(F_ab(10))


# In[1]:


# Method 3 
#This is a user friendly method that include a prompt which allows the user determine the amount of number to be generated
#We started by creating a function that will house the sequence
def Fibonacci_function(n):
    d = [] 
    a,b = 0,1
    for i in range(n):
        print(a)
        c= a+b
        a,b = b, c
    return d
d = int(input("How many numbers would you like to display ")) #prompt statement
for i in Fibonacci_function(d):
    print(i)


# In[ ]:





# In[ ]:




