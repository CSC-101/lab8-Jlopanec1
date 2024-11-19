def groups_of_3(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]
print(groups_of_3([10,11,12,13,14,15,16]))
print(groups_of_3([]))