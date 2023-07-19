import TComplex


cplx_1 = TComplex.t_complex()
cplx_2 = TComplex.t_complex()
tong = TComplex.t_complex()
hieu = TComplex.t_complex()
tich = TComplex.t_complex()
thuong = TComplex.t_complex()

cplx_1.nhap()
cplx_1.xuat()
cplx_2.nhap()
cplx_2.xuat()

print('\n=====ket qua=====')
print('phep +:')
tong = cplx_1+cplx_2
print('phep -:')
hieu = cplx_1-cplx_2
print('phep *:')
tich = cplx_1*cplx_2
print('phep /:')
thuong = cplx_1/cplx_2