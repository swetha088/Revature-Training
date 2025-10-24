Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
5>=3
True
5!=2
True
5!=5
False
-6
-6
not 1
False
not 0
True
7&9
1
7/9
0.7777777777777778
7|9
15
7^9
14
5<<3
40
5>>2
1
3>>3
0
3>>6
0
3>>1
1
5>>2
1
5>>>2
SyntaxError: invalid syntax
4<<<2
SyntaxError: invalid syntax
num1=10
type()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
type (num1)
<class 'int'>
num1 is int
False
type(num1) is int
True
type(num1) is not int
False
type (num1) is not str
True
print()

print(2)
2
print(num1)
10
num1
10
print
<built-in function print>
print('hi')
hi
'hi"
SyntaxError: unterminated string literal (detected at line 1)
'hi'
'hi'
print('hi'+'hello')
hihello
print(num1+10)
20
Traceback (most recent call last):
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('hi'+10)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print('hi'+10)
TypeError: can only concatenate str (not "int") to str
print(10+'hello')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(10+'hello')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('10'+'hi')
10hi
print('Sum: ' + num1+10)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print('Sum: ' + num1+10)
TypeError: can only concatenate str (not "int") to str
print('Sum : ' , num1+10)
Sum :  20
print('Sum : '  + '\n', num1+10)
Sum : 
 20
input()
5
'5'
input()
true
'true'
input()
True
'True'
input()
'True'
"'True'"
input('Enter a number')
Enter a number 5
' 5'
input('Enter a num:')
Enter a num:6
'6'
input('Enter a num:')
Enter a num:5436777019847442
'5436777019847442'
int(input('Enter a num:'))
Enter a num:5
5
float(input('Enter a num:'))
Enter a num:5
5.0
bool(input('Enter a num:'))
Enter a num:1
True
bool(input('Enter a num:'))
Enter a num:0
True
True
True
bool(input('Enter a num:'))
Enter a num: '1'
True
bool(input('Enter a num:'))
Enter anum:0
True
SyntaxError: multiple statements found while compiling a single statement

bool(input('Enter a num:'))
Enter a num:''
True
bool(input('Enter a num:'))
Enter a num:'0'
True
bool(input('Enter a num:'))
Enter a num:()
True
True
True
bool(input('Enter a num:'))
Enter a num:
False
bool(input(Enter a num))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
bool(input(,Enter a num))
SyntaxError: invalid syntax
int(input('Enter a num:'))
Enter a num:
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(input('Enter a num:'))
ValueError: invalid literal for int() with base 10: ''
bool(0)
False
"Swetha's house"
"Swetha's house"
str1='hello there !"
SyntaxError: unterminated string literal (detected at line 1)
dtr1="hello there !"
str1="hello there
SyntaxError: unterminated string literal (detected at line 1)
str1="hello there !"
str1
'hello there !'
len(str1)
13
str1[0]
'h'
str[-1]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    str[-1]
TypeError: type 'str' is not subscriptable
str1[10]
'e'
str1[-1]
'!'
str1[8]
'e'
str[:5]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    str[:5]
TypeError: type 'str' is not subscriptable
str1[5:]
' there !'
str1[0:12:6]
'ht'
str1[0::3]
'hltr!'
str1[::3]
'hltr!'
str[-3:-6]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    str[-3:-6]
TypeError: type 'str' is not subscriptable
str1[-3::-6]
'eo'
>>> str[-12:-2:-6]
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    str[-12:-2:-6]
TypeError: type 'str' is not subscriptable
>>> KeyboardInterrupt
>>> str1[-12:-2:-6]
''
>>> str1[2::0]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    str1[2::0]
ValueError: slice step cannot be zero
>>> str1[3::2]
'l hr '
>>> str1.capitalize()
'Hello there !'
>>> str1.upper()
'HELLO THERE !'
>>> str1.lower()
'hello there !'
>>> str1.casefold()
'hello there !'
>>> str1.count()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    str1.count()
TypeError: count expected at least 1 argument, got 0
>>> str1.count('r')
1
>>> str1.count(3)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    str1.count(3)
TypeError: count() argument 1 must be str, not int
>>> str1.count('e')
3
>>> str1.count('s')
0
>>> str1.count('z')
0
>>> str1.endswith('e')
False
>>> str1.endswith('!')
True

