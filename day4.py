###DAY 5 Task (20mins)
##Write outputs of following without running the code:

#1. strip, lstrip, rstrip methods
a = '   python is simple   '
print(a.strip())   ##output-python is simple
print(a.lstrip())  ##output-python is simple   
print(a.rstrip())  ##output-   python is simple

#2. replace
a = 'python is simple, python is easy, python is allrounder'
b = a.replace('python', 'java')  
print(a)    #output-python is simple, python is easy, python is allrounder
print(b)    ## java is simple, java is easy, java is allrounder

#3. upper, lower, swapcase, title, capitalize
a = 'PYTHON is siMPle'
print(a.lower())   ##python is simple
print(a.upper())    ##PYTHON IS SIMPLE
print(a.swapcase())  ##python is SImpLE
print(a.title())      ##Python Is Simple
print(a.capitalize()) ##Python is simple

#4. count, startswith, endswith
a = 'abacad'
b = a.startswith('a')
c = a.startswith('ad')
d = a.endswith('d')
e = a.endswith('de')
f = a.count('a')
g = a.count('ad')
print(b)  #true
print(c)  #false
print(d)  #true
print(e)  #false
print(f)  #3
print(g)  #1

#5. find, rfind, index, rindex
s = 'abacada'
print(s.find('a'))    #0
print(s.find('a', 3))  #3
print(s.find('a', 4, 8))  #4
print(s.rfind('a'))  #6
print(s.rfind('a', 3))  #3
print(s.rfind('a', 4, 8))  #4
print(s.index('a'))  #0
print(s.index('a', 3))  #3
print(s.index('a', 4, 8))  #4
print(s.index('a'))  #0
print(s.index('a', 3))  #3
print(s.index('a', 4, 8))  #4
print(s.index('z'))  # ValueError: substring not found
print(s.find('z'))  # -1


#6. is methods
a = ' '
b = ' a'
print(a.isspace())  # True
print(b.isspace())  # False

a = 'aBcD'
print(a.isalpha())  # True
b = 'aBcD1'
print(b.isalpha())  # False
c = 'aBc@D'
print(c.isalpha())  # False

a = '13'
print(a.isdigit())  # True
b = '12a'
print(b.isdigit())  # False

a = 'AbC123'
print(a.isalnum())  # True
b = 'Ab#C2'
print(b.isalnum())  # False

a = '23$U'
print(a.isupper())  # True
b = '23%Ua'
print(b.isupper())  # False

a = '23$u'
print(a.islower())  # True
b = '23%uA'
print(b.islower())  # False



# split

a = 'badac'
print(a.split('a'))  # ['b', 'd', 'c']
b = '   '  #3 spaces 
print(b.split(' '))  # ['', '', '', '']
c = 'abaca'
print(c.split('a'))  # ['', 'b', 'c', '']
d = 'iam a good person'
print(d.split())  # ['iam', 'a', 'good', 'person']


#join
a = '@'
l = [1,2,3]
t = (1,2,3)
s = {1,2,3}
d = {3:1, 2:3, 3:1}
print(a.join(l))  #1@2@3
print(a.join(t))  #1@2@3
print(a.join(s))  #1@2@3
print(a.join(d))  #3@2@3
