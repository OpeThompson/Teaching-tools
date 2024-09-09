Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> x = 10
>>> 
>>> y = 20
>>> 
>>> import numpy as np

>>> 
>>> x < 8 and x > 15
False
>>> 
>>> a = [1,2,3,4,5,6,7,8,9]
>>> b = [3,4,5,6,7,8,9,1,2]
>>> 
>>> a_np = np.array(a)
>>> b_np = np.array(b)
>>> 
>>> 
>>> np.logical_and(a > 3, a < 6)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    np.logical_and(a > 3, a < 6)
TypeError: '>' not supported between instances of 'list' and 'int'
>>> 
>>> 
>>> np.logical_and(a_np > 3, a_np < 6)
array([False, False, False,  True,  True, False, False, False, False])
>>> 
>>> 
>>> np.logical_and(a_np > 3, b_np < 6)
array([False, False, False, False, False, False, False,  True,  True])
>>> 
>>> 
>>> 
