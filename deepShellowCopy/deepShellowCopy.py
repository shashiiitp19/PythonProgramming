import copy

#Shellow Copy: A shallow copy creates a new object but inserts references into it for
#the objects found in the original. In other words, the new object itself is a copy,
#but its elements are references to the same objects as the original.
fist_list = [[1,2,3],[4,5,6]]
sec_list = copy.copy(fist_list)
sec_list[0][0] = 15

print(fist_list)
print(sec_list)

#Deep Copy:A deep copy creates a new object and recursively copies all objects
#found inside the original object. This means that the new object is entirely
#independent of the original one, and changes in the deep-copied object do not affect the original.
new_first = [[10,11,12],[13,14,15]]
new_sec = copy.deepcopy(new_first)
new_sec[0][0] = 55

print(new_first)
print(new_sec)
