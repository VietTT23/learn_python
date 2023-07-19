class t_complex:
    def __init__(self):
        self.so_ao = None
        self.so_thuc = None

    def nhap(self):
        print('Nhap so phuc:')
        self.so_thuc = int(input('Phan thuc = '))
        self.so_ao = int(input('Phan ao = '))

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




#test2