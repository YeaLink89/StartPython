import decimal
import os

print ("start python")
print os.environ
# print os.times()
print (round(3 * 1415, 2))  # result  3. 14
print (round(9.995, 2))  # result  9. 99
print (decimal.Decimal(9.995))

t = 'He is a string. Who are you?'
print(t.capitalize())  # Cap first letter
print(t.split())  # split by words
print(t.find('i'))  # return index of 'i'
print(t.find('in'))  # index of 'i' in 'in'
print(t.find('Python'))  # find sth not in
print(t[0:4])  # returu from index 0 to 3
print(t.replace(' ', '|'))  # replace by '|'
w = 'http://www.google.com'
print(w.strip('http://'))  # delete sth
