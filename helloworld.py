#####################
#                   #
#   Hello, World!   #
#                   #
#####################

"""
This is a comment
written in
more than just one line
"""
# This is a comment
# written in
# more than just one line

# variable
hello_world = 4
hello_world = "Hello, World!"
print(hello_world)

# assign multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = 2
y = "_thug"
print(x, y)

# global variable
t = 'thang'


def toi_la_toi_01():
    # local variable
    t = 'duyen'
    print('toi la ' + t)


def toi_la_toi_02():
    # global variable
    global tad
    tad = 'thang_and_duyen'
    print(tad)


# print local variable
toi_la_toi_01()
# print global variable
print('toi la ' + t)
toi_la_toi_02()
print(tad)



a = 'realm'
b = a
print(b[3])
b[3] = '1'
a = b
print(a)
