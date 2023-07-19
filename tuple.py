day_la_tuple = ('a', 'b', 'c', 'd', 'e')
print(day_la_tuple)
print(type(day_la_tuple))
dem = day_la_tuple.count('a')
print(dem)

day_la_tuple_2 = ('a',)
print(type(day_la_tuple_2))

# TUPLE LÀ KIỂU LƯU TRỮ KHÔNG THỂ THAY ĐỔI, THÊM, SỬA, XOÁ
# ĐỂ THỰC HIỆN THAY ĐỔI, THÊM, SỬA, XOÁ CHUYỂN QUA KIỂU LIST

# UNPACKING: TRÍCH XUẤT CÁC GIÁ TRỊ TRỞ LẠI THÀNH BIẾN

unpack = (1, 2, 3, 4)
(a, *b, c) = unpack
print(unpack)
print(type(a))
print(b)
print(type(c))
#print(d)
