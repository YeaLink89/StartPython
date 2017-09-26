# coding=utf-8
import decimal
import math

print ("hello world")

# print同样适用于整数
print 4

print ("-----------------分割线------------------")
# 打印类型
print type('Hello, World!')
print type(3)
print type(3.14)

print ("-----------------分割线------------------")
# 变量赋值
message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931
print pi
print message
print n
print ("-----------------分割线------------------")

# print os.environ
# print os.times()
print (round(3.1415, 2))  # result  3. 14
print (round(9.995, 2))  # result  9. 99
print (decimal.Decimal(9.995))
print ("-----------------分割线------------------")

# 运算符和运算数
minute = 59
print ("minute/60 =", minute / 60)
print ("minute/60.0 =", minute / 60.0)

first = 'throat'
two = 'warbler'
print ("first+two=", first + two)
width = 17
height = 12.0
delimiter = '.'
# ----------------------
t = 'He is a string. Who are you?'
print(t.capitalize())  # Cap first letter
print(t.split())  # split by words
print (delimiter * 5)

radians = 0.7
height = math.sin(radians)
print ("height=====", height)

print ("-----------------分割线------------------")


def print_lyrics(a):
    print ("a=", a)
    print ("b===", a)


def repeat_lyrics():
    print_lyrics(77777)
    print_lyrics(88888)


print print_lyrics(999999)
print repeat_lyrics()


def print_twice(bruce):
    print bruce
    print bruce


print_twice(math.pi)


def do_twice(f):
    f()
    f()


def print_spam():
    print 'spam'


do_twice(print_spam)

print ("-----------------分割线------------------")
print(t.find('i'))  # return index of 'i'
print(t.find('in'))  # index of 'i' in 'in'
print(t.find('Python'))  # find sth not in
print(t[0:4])  # returu from index 0 to 3
print(t.replace(' ', '|'))  # replace by '|'
w = 'http://www.google.com'
print(w.strip('http://'))  # delete sth

# -----------------------
l = [1, 2, 3.14, 'test']  # list

# print (type(l))l.append ([4,  3])
print type(l)
print l
l.append([4, 3])
print l
# print(l.extend(['delta' ,5 ,6])   #add  a  list
# print(l.insert(3, 'beta')  #insert  before  index 3
# print(l.remove ('data')   #delete an elementprint(l)

print ("-----------------分割线------------------")


# 绘制田字格
def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print '+ - - - -',


def print_post():
    print '|        ',


def print_beams():
    do_twice(print_beam)
    print '+'


def print_posts():
    do_twice(print_post)
    print '|'


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()

print ("-----------------分割线------------------")
# 条件语句
x = 1000
if x % 2 == 0:
    print 'x is even'
else:
    print 'x is odd'
