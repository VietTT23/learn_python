day_la_list = ['tao', 'chuoi', 'cam', 'tao']
(a, *c) = day_la_list
print(a)
print(c)

day_la_list_2 = list((1, 2, 3, 4, 5, 6))
print(day_la_list_2)
# print(type(day_la_list))
# print(day_la_list_2[-2])
# day_la_list_2[0:3] = [7, 7]
day_la_list_2.insert(0, 7)  # insert vào vị trí bất kì
print(day_la_list_2)
day_la_list_2.append(7)  # append sẽ thêm phần ử vào cuối list
print(day_la_list_2)
day_la_list_2.extend(day_la_list)
print(day_la_list_2)

# LIST COMPREHENSION
# SYNTAX: new_list = [expression for item in iterable if condition == True]

# new_list = []
# for x in day_la_list:
#     for a in x:
#         if 'a' in x:
#             a[0]
#             new_list.append(x)
# print(new_list)

new_list = [x[0:].upper() for x in day_la_list if 'a' in x]
print(new_list)