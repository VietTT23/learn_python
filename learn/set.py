# SET LÀ KIỂU DỮ LIỆU KHÔNG THỂ THAY ĐỔI, NHƯNG CÓ THỂ THÊM VÀ XOÁ

day_la_set = {True, 2, 3, 4}
day_la_list = ['a', 'b']
day_la_tuple = ('c', 'd')

day_la_set.update(day_la_tuple, day_la_tuple)
# day_la_set.update(day_la_tuple)

print(day_la_set)
print(type(day_la_set))

# day_la_set.remove('e')
day_la_set.discard('e')

x = {'a', 'b', 'c', 'd'}
y = {'a', 'e', 'f', 'g'}

x.intersection_update(y)
z = x.intersection(y)

print(x)
print(z)