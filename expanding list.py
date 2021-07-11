'''Write a Python program to extend a list without append.
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]'''

'''list1=[10,20,30]
list2=[40,50,60]
print(list1+list2)
'''

'''x = [10, 20, 30]
y = [40, 50, 60]
x[:0] =y
print(x)'''

'''
Write a Python program to split a given list into two parts where the length of the first part of the list is given.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])'''

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 



rows = 5

for i in range(1, rows + 1):

    for j in range(1, i + 1):
       print(j, end= ' ')

    print('')
'''

'''
* 
* * 
* * * 
* * * * 
* * * * * 

'''

rows=5
for i in range(0,rows):
    for j in range(0,i+1):
        print(1*("*"), end=' ')
    print('')
