class t_complex:
    def __init__(self):
        self.so_ao = None
        self.so_thuc = None

    def nhap(self):
        print('Nhap so phuc:')
        self.so_thuc = float(input('Phan thuc = '))
        self.so_ao = float(input('Phan ao = '))

    def xuat(self):
        print('{0} + {1}i'.format(self.so_thuc, self.so_ao))
        # print(type(self.so_thuc))
        # print(type(self.so_ao))

    def __add__(self, other):
        thuc = self.so_thuc + other.so_thuc
        ao = self.so_ao + other.so_ao
        print('{0} + {1}i'.format(thuc, ao))

    def __sub__(self, other):
        thuc = self.so_thuc - other.so_thuc
        ao = self.so_ao - other.so_ao
        print('{0} + {1}i'.format(thuc, ao))

    def __mul__(self, other):
        thuc = self.so_thuc * other.so_thuc
        ao = self.so_ao * other.so_ao
        print('{0} + {1}i'.format(thuc, ao))

    def __truediv__(self, other):
        thuc = self.so_thuc / other.so_thuc
        ao = self.so_ao / other.so_ao
        print('{0} + {1}i'.format(thuc, ao))


cplx_1 = t_complex()
cplx_2 = t_complex()
tong = t_complex()
hieu = t_complex()
tich = t_complex()
thuong = t_complex()

cplx_1.nhap()
cplx_1.xuat()
cplx_2.nhap()
cplx_2.xuat()

tong = cplx_1+cplx_2
hieu = cplx_1-cplx_2
tich = cplx_1*cplx_2
thuong = cplx_1/cplx_2

print('\n=====ket qua=====')
print('phep +:')
tong = cplx_1+cplx_2
print('phep -:')
hieu = cplx_1-cplx_2
print('phep *:')
tich = cplx_1*cplx_2
print('phep /:')
thuong = cplx_1/cplx_2
#test2