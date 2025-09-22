student = {"rahul","gaurav","dhruv"} #this is set in which no duplicates are allowed
print(student)

#checking values present in the set or not with the help of (in)
print("rahul" in student)
print("rahuliya" in student)

set_a = {1,2,3}
set_b = {4,2,5}

print(set_a | set_b)#union
print(set_a & set_b)#intersection
print(set_a - set_b)#here we get the answer from the set_a after removing the commans
print(set_b - set_a)#here we get the answer from the set_b after removing the commans

#in difference method whatsoever is written first the answer will come from that set only.
