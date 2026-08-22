
##Print the outputs before running code:
#Arithmetic Operators
print(10 + 5 * 2)   ##output=20       
print(2 ** 3 ** 2)  ##512
print(10 // 3)    ##0utput=3
print(10 % 3)     ##output=1
print(5 / 2)        ##2.5
print([1,2,3] + [4,5,6])  ##output=[1, 2, 3, 4, 5, 6]
print((1,2,3) + (4,5,6))  ##output=(1, 2, 3, 4, 5, 6)
print({1,2,3} + {4,5,6})  ##output={1, 2, 3, 4, 5, 6}
print([1,2,3] * 4)        ##output=[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(*[1,2,43])           ##output=1 2 43
print([1,2,3] + (1,2,3))    ##output=error
print([1,2,3] + 'dog')       ##output=error


#Relational and Logical Operators:
print(10 > 5 and 20 < 30)     ##output=true
print(10 > 20 and 5 < 10)     ##output=false
print(not 1 == 1)              ##output=false
print(1 < 2 < 3)              ##output=true
print(1 > 2 > 3)              ##output=false
print('abc' > 'def')          ##output=false
print([1,2,3] < [1,3,4])      ##output=true

#Assignment and walrus operator:
print(a=10)
print(a:=10)
if (n := 34) > 10:
   print(n)
##output=34
#Identity and equality operators:
a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)
a = 'abc'
b = 'abc'
print(a==b)
print(a is b)
a = (1,2,3)
b = (1,2,3)
print(a == b)
print(a is b)
##output=true


##Membership operator
a = [1,2,3,4,5]
print(6 in a)
print(6 not in a)
print('abc' in 'abcde')
##output=false
