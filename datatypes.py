# str
x = 'Hello, World!'
# int
x = 20
# float
x = 20.5
x = 11E4
# complex
x = 3 + 4j
# list
x = ['apple', 'orange', 'banana']
# tuple
x = ('apple', 'orange', 'banana')
# range
x = range(1006)
# dict
x = {"name": "thang", "age": 22}
# set
x = {'apple', 'orange', 'banana'}
# frozenset
x = frozenset({'apple', 'orange', 'banana'})
# bool
x = True
# byte
x = b"Hi"
# bytearray
x = bytearray(9)
# memoryview
x = memoryview(bytes(5))
# None
x = None

# display variable
print(x)
# display type of variable
print(type(x))

"""
CASTING
"""
x = float(50)

"""
STRING
"""
s = "thang{2}_dep{1}_trai{0}_vo_dich"
a = 22
b = 3
c = 2
d = 1
print(s)
print(s[1])
print(len(s))
print("thang" in s)
if "thang" in s:
    print("thang dep trai vo dich")
print("thang" not in s)
print(s[0:-1])  # từ vị trí thứ 2 đến vị trí thứ 5
print(s.upper().lower())
print(s.strip('t'))  # xoá đầu hoặc đít
print(s.replace('thang', 'duyen'))
print(s.split('t'))
print(s, '_', a, '_', 'tuoi')
# print(s.format(a))
print(s.format(b, c, d))


"""
ESCAPE CHARACTERS
"""
# CODE      RESULT
# \'	    Single Quote
# \\	    Backslash
# \n	    New Line
# \r	    Carriage Return
# \t	    Tab
# \b	    Backspace
# \f	    Form Feed
# \ooo	    Octal value
# \xhh	    Hex value

"""
STRING METHOD
"""
print(bool(1))