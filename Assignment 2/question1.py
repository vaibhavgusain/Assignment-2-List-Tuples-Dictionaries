# Write a Python program to get a list, sorted in increasing order by 
# the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# emptytuple = ()

# list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# list1.sort()
# print(list1)

lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(len(lst))
# length = len(lst)
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

lst2 = []
final_list = []

for i in lst:
    lst2.append(i[1]) #[5,2,4,3,1]

lst2.sort()    # [1,2,3,4,5]

for i in lst2:
    for j in lst:
        if i == j[1]:
            final_list.append(j)


print(final_list)





















