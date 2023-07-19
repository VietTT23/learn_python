# DICTIONARIES LÀ KIỂU LƯU TRỮ DỮ LIỆU THEO KIỂU KEY:VALUE
# ĐÂY LÀ KIỂU DỮ LIỆU CÓ THỨ TỰ, CÓ THỂ THAY ĐỔI NHƯNG KHÔNG ƯỢC TRÙNG LẶP KEY

day_la_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'z': [1, 2, 3]
}

for x, y in day_la_dict.items():
    print(x, y)

print(day_la_dict['z'])
print(day_la_dict.get('z'))
print(day_la_dict.keys())

# danh sách caác key() sẽ tương ứng như 1 view của dict, thay đổi trên dict cũng sẽ thay đổi trên view
x = day_la_dict.keys()
print(x)
day_la_dict['d'] = 4
print(x)

# NESTED DICTIONARIES
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#### OR ####
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}