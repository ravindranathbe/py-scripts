# a = 'Hello world'
# print(a)
"""
Multi line comment
if(a == 'Hello world'):
	print('a is equal to H')
else:
	print('a is not equal to H')


def func1(v1):
	print('func1 called', v1)

# func1('val1')

a = 100
b = 100
if(a == 10):
	print('a is equal to 10')
else:
	print ('a is not equal to 10')

"""

# print('a is great', 'b is great too')
#import os
#print(dir(os))

'''
arr = ['One', 'Two']
print(arr[0])
print(len(arr))
arr.append('Three')
#arr.insert(0, 'Four')
arr.pop()
arr.remove('Two')
arr.extend(['Two', 'Three'])
print(arr)
for a in arr:
	print(a)


def getMsg():
	return 'Msg 1'

msg = getMsg()
print(msg)

if(msg == 'Msg 1'):
	print('Fine')
elif(msg == 'Msg 2'):
	print('Not bad')
else:
	print('Bad')

list1 = [1, 2, 3, 4]
list1.insert(0, 5)
list1.remove(3)
print('The count of 3 is: ' + str(list1.count(3)))

for i in list1:
	print('The value is: ' + str(i))



testStr = 'A bat has no ears. Really!!!'

print('The count of "a" is: ');
print(testStr.count('a'))

print(testStr[1])
print(testStr.lower())
print(testStr.find('a'))

print(testStr[0:4])

a = 1
while a <= 100000:
	print(a, end = ' | ')
	a += 1

for i in range(1, 10001):
	if(i == 10000):
		print(i)
	else:
		print(i, end = ' // ')



rList1 = [1,2,3,4,5]
rTuple1 = (1,2,3,4,5)

rList1.append(6)
print(rList1)

rList2 = list(rTuple1);
rList2.append(6)
print(rList2)

rDict1 = {'a': 'It is A', 'b': 'It is B'}
# print(rDict1['a'])
for k in rDict1:
	print('Key: ' + k + ' Value: ' + rDict1[k])

a = 10
b = 100
print('The value of a is: {0} and b is: {1}'.format(a, b))

a = 'Test'
try:
	print('The value of a is: ' + a)
except:
	print('The value of a should be string.')

print(a)



f = open('testFile.txt', 'r')
#print(f.read(5))
#print(f.read())

lines = []
for l in f:
	lines.append(l)

print(lines)

f.close()


f = open('test.txt', 'a')
for i in range(1, 1001):
	print('{0}'.format(i))
	f.write('{0}\n'.format(i))
f.close()


from cls1 import *

calcObj = calc()
calcObj.setVar1(100)
calcObj.setVar2(100)
print(calcObj.add())

import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1', user='root', password='', db='vue', cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
  sql = "SELECT * FROM `notes`"
  cursor.execute(sql)
  result = cursor.fetchall()
  #print(result)
  #print(cursor.rowcount)
  print(cursor.description)


connection.close()    

import csv
import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1', user='root', password='', db='sakila', cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
  sql = "SELECT * FROM customer c LEFT JOIN address a ON a.address_id = c.address_id INNER JOIN city ct ON ct.city_id = a.city_id INNER JOIN country cty ON cty.country_id = ct.country_id"
  cursor.execute(sql)
  result = cursor.fetchall()

fileObj = open('test.txt', 'w')

# Writing the results in CSV
with open('customer.csv', 'w', newline='') as customerFile:
	customerWriter = csv.writer(customerFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	customerWriter.writerow(['First name', 'Last name', 'Status', 'Address', 'District', 'City', 'Country', 'Postal code'])

	for customer in result:
		customer_status = 'Inactive'
		customer_firstName = customer['first_name'][0].upper() + customer['first_name'][1:].lower()
		customer_lastName = customer['last_name'][0].upper() + customer['last_name'][1:].lower()
		customer_address = customer['address'] + ', ' + customer['district'] + ', ' + customer['city'] + ', ' + customer['country'] + ', ' + customer['postal_code'] 
		if(customer['active'] == 1):
			customer_status = 'Active'

		# fileObj.write('First name: {0} Last name: {1} Status: {2}\nAddress: {3}\n\n'.format(customer_firstName, customer_lastName, customer_status, customer_address))
		customerWriter.writerow([customer_firstName, customer_lastName, customer_status, customer['address'], customer['district'], customer['city'], customer['country'], customer['postal_code']])

customerFile.close()
fileObj.close()
connection.close() 

'''
