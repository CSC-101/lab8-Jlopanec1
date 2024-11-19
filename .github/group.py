def groups_of_3(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]
print(groups_of_3([1,2,3,4,5,6,7,8,9]))