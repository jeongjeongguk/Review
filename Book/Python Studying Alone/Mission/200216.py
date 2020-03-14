import copy
org_list_a = [0, 1, 2, 3, 4, 5, 6, 7]

list_a = copy.deepcopy(org_list_a)
list_a.extend(list_a)
print(list_a)
# [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]

list_a = copy.deepcopy(org_list_a)
list_a.append(10)
print(list_a)  # [0, 1, 2, 3, 4, 5, 6, 7, 10]

list_a = copy.deepcopy(org_list_a)
list_a.insert(3, 0)
print(list_a)  # [0, 1, 2, 0, 3, 4, 5, 6, 7]

list_a = copy.deepcopy(org_list_a)
list_a.remove(3)
print(list_a)  # [0, 1, 2, 4, 5, 6, 7]

list_a = copy.deepcopy(org_list_a)
list_a.pop(3)
print(list_a)  # [0, 1, 2, 4, 5, 6, 7]

list_a = copy.deepcopy(org_list_a)
list_a.clear()
print(list_a)  # []

imsi = "Test"; list_a = [ 273, 32, 103, "묻고 더블로 가", True, imsi];

print("done")
