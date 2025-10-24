Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
str1='hello'
str1
'hello'
id(str1)
2409026861408
str1='india'
id(str1)
2409059048240
num=[10,20,30]
num
[10, 20, 30]
id(num)
2409058921984
num.append(80)
num
[10, 20, 30, 80]
id(num)
2409058921984
num[3]=
SyntaxError: invalid syntax
num[3] =100
num
[10, 20, 30, 100]
num.count(100)
1
num.append(50)
num
[10, 20, 30, 100, 50]
num.count(40)
0
num.index(4, 500)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    num.index(4, 500)
ValueError: list.index(x): x not in list
num.insert(4, 500)
num
[10, 20, 30, 100, 500, 50]
num.remove(0)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    num.remove(0)
ValueError: list.remove(x): x not in list
num.remove(400)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    num.remove(400)
ValueError: list.remove(x): x not in list
num.remove(40)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    num.remove(40)
ValueError: list.remove(x): x not in list
num.remove(30)
num
[10, 20, 100, 500, 50]
num.pop()
50
num
[10, 20, 100, 500]
num.pop(-3)
20
num
[10, 100, 500]
num.reverse()
num
[500, 100, 10]
num.sort()
num
[10, 100, 500]
num.sort(reverse = True )
num
[500, 100, 10]
nums= num.copy()
nums
[500, 100, 10]
id(nums)
2409059020160
id(num)
2409058921984
nums1=num
id(nums1)
2409058921984
num.extend(nums)
num
[500, 100, 10, 500, 100, 10]
num.clear()
num
[]
num
[]
del(num)
num
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    num
NameError: name 'num' is not defined. Did you mean: 'nums'?
tup1=(10,20,30)
tup1
(10, 20, 30)
tup1[3]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    tup1[3]
IndexError: tuple index out of range
tup1[2]
30
tup1.count()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    tup1.count()
TypeError: tuple.count() takes exactly one argument (0 given)
tup1.count(20)
1
tup1.clear()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    tup1.clear()
AttributeError: 'tuple' object has no attribute 'clear'
tup1.index)20)
SyntaxError: unmatched ')'
tup1.index(20)
1
tup1.
SyntaxError: invalid syntax
set1={22,11,33,55,99,9,7}
set1
{33, 99, 55, 22, 7, 9, 11}
set1
{33, 99, 55, 22, 7, 9, 11}
tup2=(2,10,1,8,7,3,4)
tup2
(2, 10, 1, 8, 7, 3, 4)
set1
{33, 99, 55, 22, 7, 9, 11}
set{2}
SyntaxError: invalid syntax
set1.add(43)
set1
{33, 99, 55, 22, 7, 9, 11, 43}
set1.sort()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    set1.sort()
AttributeError: 'set' object has no attribute 'sort'
set2={100,200,300}
set2
{100, 300, 200}
set1.union(set2)
{33, 99, 100, 7, 200, 9, 11, 43, 300, 22, 55}
set3.intersection(set2)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    set3.intersection(set2)
NameError: name 'set3' is not defined. Did you mean: 'set1'?
set3=set1.union(set2)
set3
{33, 99, 100, 7, 200, 9, 11, 43, 300, 22, 55}
set3.intersection(set2)
{200, 100, 300}
set4=set3.intersection(set2)
set4
{200, 100, 300}
set5=set1.difference(set4)
set5
{33, 99, 7, 9, 11, 43, 22, 55}
dict1={1:10, 2:20}
dict1
{1: 10, 2: 20}
dict1[2]
20
dict1[3]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dict1[3]
KeyError: 3

dict1[1]
10
dict1[0]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    dict1[0]
KeyError: 0
dict1[2]
20
>>> dict2={'rno':,'123','name': 'AAA'}
SyntaxError: expression expected after dictionary key and ':'
>>> dict2={'rno':'123','name': 'AAA'}
>>> dict2
{'rno': '123', 'name': 'AAA'}
>>> dict2['rno']=123
>>> dict2['rno']
123
>>> dict2
{'rno': 123, 'name': 'AAA'}
>>> dict2['name']=AAA
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    dict2['name']=AAA
NameError: name 'AAA' is not defined
>>> dict2['ph']= 1234589750
>>> dict2
{'rno': 123, 'name': 'AAA', 'ph': 1234589750}
>>> dict2['ph']
1234589750
>>> dict1.get('ph')
>>> ph=dict2.get('ph')
>>> ph
1234589750
>>> dict2.keys()
dict_keys(['rno', 'name', 'ph'])
>>> dict2.values()
dict_values([123, 'AAA', 1234589750])
>>> dict2.pop(2)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    dict2.pop(2)
KeyError: 2
>>> dict2
{'rno': 123, 'name': 'AAA', 'ph': 1234589750}
>>> dict1.pop(2)
20
>>> dict1
{1: 10}
