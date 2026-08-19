#SET METHODS
#create a empty dict and print its type
d = {}
print(type(d))
#create a empty set and print its type
s = set()
print(type(s))
#add 5 non-sequences and 6 sequences to that set with add method
s = set()
s.add(1)
s.add(2.5)
s.add(3+4j)
s.add(True)
s.add(None)
s.add('abc')
#s.add([1,2,3])
#s.add(range(1,4))
#s.add((1,2,3))
#s.add({1,2,3})
#s.add({1: 'a', 2: 'b'})
print(s)
#add 5 non-sequences and 6 sequences with update method
s = set()
#s.update(4)          
#s.update(5.6)        
#s.update(4+5j)       
#s.update(False)      
#s.update(None)       
s.update('abc')
#s.update([4,5,6])
s.update(range(4,7))
s.update((4,5,6))
s.update({4,5,6})
s.update({7: 'a', 8: 'b'})
print(s)

#print a set and remove first element from that set
print(s)
s.pop()
print(s)
#remove one existing and one non-existing element from that set
s.remove('a')
#s.remove('z')
print(s)
#discard one existing and one non-existing element from that set
s.discard('a')
s.discard('z')
print(s)
#remove all elements from the set
s.clear()
print(s)
#create a set {1,2,3,4}, a list [3,4,5,6]. 
s = {1,2,3,4}
l = [3,4,5,6]
#write union of set and list
print(s.union(l))
#write intersection of set and list
print(s.intersection(l))
#write difference of set and list
print(s.difference(l))
#write symmetric difference of set and list
print(s.symmetric_difference(l))
#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs


#DICT METHODS
#create a empty dict
d = {}
#extend dict with another dict
d.update({1: 'a', 2: 'b'})
print(d)
#extend dict with another list
d.update([(1,'a'),(2,'b'),(3,'c'),(4,'d')])
print(d)
#extend dict with another tuple
d.update(((5,'e'),(6,'f'),(7,'g'),(8,'h')))
print(d)
#extend dict with another set
d.update({(9,'i'),(10,'j'),(11,'k')})
print(d)

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
#remove the pair with key 4
d.pop(4)
#remove the pair with key 100
#d.pop(100) ##100 is not in dict.
#remove the pair with key 100 if not there return 'z'
d.pop(100, 'z')
#remove the last pair
d.popitem()
print(d)
#remove all elements from the dict
d.clear()
print(d)

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
#get the value of key 4
print(d.get(4))
#get the value of key 100
print(d.get(100))
#get the value of key 100, if key is not present get 'z'
print(d.get(100, 'z'))

#get the value of key 4 with setdefault
print(d.setdefault(4))

#get the value of key 100 with setdefault
print(d.setdefault(100))
#get the value of key 100 with setdefault, if key is not there add 100 with 'z'
print(d.setdefault(100,'z'))
#get all keys of dict and print its type
print(d.keys())
print(type(d.keys()))
#get all values in dict and print its type
print(d.values())
print(type(d.values()))
#get all items in dict and print its type
print(d.items())
print(type(d.items()))
