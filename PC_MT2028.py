#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np


# ### Write a simple, short program to calculate and print area of one of the biggest faces and volume of a rectangular cuboid with the dimensions given below. Use functions and loops if required(When length=30cm)

# In[2]:


l=30 #lenght
b=20 #breadth
h=15 #height
volume=l*b*h
a = l*b
b = b*h
c = h*l
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

print("Volume of the cuboid is ", volume,"cm3")
print("Area of one of the biggest faces is ", maximum(a, b, c),"cm²")


# ### Write a simple, short program to calculate and print area of one of the biggest faces and volume of a rectangular cuboid with the dimensions given below. Use functions and loops if required(When length=40cm)

# In[3]:


l=40 #lenght
b=20 #breadth
h=15 #height
volume=l*b*h
a = l*b
b = b*h
c = h*l
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

print("Volume of the cuboid is ", volume,"cm3")
print("Area of one of the biggest faces is ", maximum(a, b, c),"cm²")


# ### Write a simple, short program to calculate and print area of one of the biggest faces and volume of a rectangular cuboid with the dimensions given below. Use functions and loops if required(When length=50cm)

# In[4]:


l=50 #lenght
b=20 #breadth
h=15 #height
volume=l*b*h
a = l*b
b = b*h
c = h*l
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

print("Volume of the cuboid is ", volume,"cm3")
print("Area of one of the biggest faces is ", maximum(a, b, c),"cm²")


# ## Unit test
Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use. It determines and ascertains the quality of your code.
The unit test framework in Python is called unittest, which comes packaged with Python.

Unit testing makes your code future proof since you anticipate the cases where your code could potentially fail or produce a bug. Though you cannot predict all of the cases, you still address most of them.

You have just seen two types of tests:

An integration test checks that components in your application operate with each other.
A unit test checks a small component in your application.

Passing a test
Here’s a typical scenario for writing tests:

First you need to create a test file. Then import the unittest module, define the testing class that inherits from unittest.TestCase, and lastly, write a series of methods to test all the cases of your function’s behavior.

Failing a test
To show you what a failing test looks like I’m going to modify a  formatted_name() function by including a new middle name argument.

In the output you will see information that will tell you all you need to know where the test fails:

First item in the output is the Error telling you that at least one test in test case resulted in an error.
Next you’ll see the file and method in which the error occurred.
After that you will see the line in which the error occurred.
And what kind of error it is, in this case we are missing 1 argument “middle_name”.
You will also see the number of run tests, the time needed for the tests to  complete, and a textual message that represents the status of the tests with number of errors that occurred
# In[ ]:





# ## Profiling modules in Python 
Python provides many excellent modules to measure the statistics of a program. The first step toward a fast implementation of a program is profiling to find out where your code spends its time. The key point is to only optimize functions that are actually slow or are called extensively. Profilers can collect several types of information: timing, function calls, interruptions, cache faults… In our case, we are going to focus our attention on timing and function calls.

Types of profiling:

Deterministic Profiling: All events are monitored. It provides accurate information but has a big impact on performance. It means the code run slower under profiling. Its use in production systems is often impractical. This type of profiling is suitable for small functions.

Statistical profiling: Sampling the execution state at regular intervals to compute indicators. This method is less accurate, but it also reduces the overhead.

Python comes with two modules for deterministic profiling: cProfile and profile. Both are different implementations of the same interface. The former is a C extension with relatively small overhead, and the latter is a pure Python module. As the official documentation says, the module profile would be suitable when we want to extend the profiler in some way. Otherwise, cProfile is preferred for long-running programs. Unfortunately, there is no built-in module for statistical profiling, but we will see some external packages for it.