#create a list with 3 elements
l=[1,2,3]
#INSERT OPERATIONS
#appending

#add 5 types of non-sequence elements to it with append
l.append(4)
l.append(5)
l.append(6)
l.append(7)
l.append(8)
#add 5 types of sequences to it with append
l.append([9, 10])
l.append((11, 12))
l.append({13, 14})
l.append({"key1": "value1"})
l.append(None)
#extending
#add 5 types of non-sequence elements to it with extend
l.extend([15, 16, 17, 18, 19])
#add 5 types of sequence elements to it with extend
l.extend([[20, 21], (22, 23), {24, 25}, {"key2": "value2"}, None])
#inserting
#insert an element at index 1 and print
l.insert(1, 20)
print(l)
#insert an element at index -1 and print
l.insert(-1, 21)
print(l)
#insert an element at index 10000 and print
l.insert(10000, 22)
print(l)
#insert an element at index -10000 and print
l.insert(-10000, 23)
print(l)

#DELETE OPERATIONS
#create a list with 1,2,1,3,4,1
l = [1,2,1,3,4,1]
#pop element at index 3 and print element and list
print(l.pop(3))
#pop last element and print element and list
print(l.pop())
#remove first 1 from list and print element and list
l.remove(1)
print(l)
#clear all elements in the list
l.clear()

#UPDATE OPERATIONS
#create a list with 3,2,1,5,4 
l = [3,2,1,5,4]
#sort the list in ascending and print
l.sort()
print(l)
#sort the list in descending and print
l.sort(reverse=True)
print(l)
#reverse the list and print
l.reverse()
print(l)

#READ OPERATIONS
#create a list with 1,2,1,3,1, 2
l = [1,2,1,3,1,2]
#find count of 1 and 2 in list
print(l.count(1))
print(l.count(2))
#find index of 1 from start
print(l.index(1))
#find index of 1 from 2nd index
print(l.index(1, 2))
#find index of 1 from 5th index
#print(l.index(1, 5))

#TUPLE
#create a tuple with 1,2,1,3,1, 2
t = (1,2,1,3,1,2)
#find count of 1 and 2 in tuple
print(t.count(1))
print(t.count(2))
#find index of 1 from start
print(t.index(1))
#find index of 1 from 2nd index
print(t.index(1, 2))
#find index of 1 from 5th index
#print(t.index(1, 5))
