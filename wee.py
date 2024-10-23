def func(*var):
   for i in var:
       print(i)
func(1)
func(20,1,6)

def check_distinct(data_list):
 if len(data_list) == len(set(data_list)):
   return True
 else:
   return False;
print(check_distinct([1,6,5,8]))     #Prints True
print(check_distinct([2,2,5,5,7,8]))

# import collections
# import pprint
# with open("sample_file.txt", 'r') as data:
#  count_data = collections.Counter(data.read().upper())
#  count_value = pprint.pformat(count_data)
# print(count_value)

def add(num1, num2):
   while num2 != 0:
       data = num1 & num2
       num1 = num1 ^ num2
       num2 = data << 1
   return num1
print(add(2, 10))

a, b, c, m, n, o = 5, 9, 4, 7, 9, 4
temp = a*n - b*m
if n != 0:
   x = (c*n - b*o) / temp
   y = (a*o - m*c) / temp
   print(str(x), str(y))

import re
def transform_date_format(date):
   return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date_input = "2024-09-03"
print(transform_date_format(date_input))


from datetime import datetime
new_date = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d:%m:%Y")
print(new_date)


from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)
