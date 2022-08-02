def f(x):
    return x**3+2*x+3
#Program Utama (Pemanggil)
h=int(input('Nilai h='))
x=int(input('Nilai x='))
f1Mundur=(f(x)-f(x-h))/h
print('Hasil f1 Selisih Mundur orde 0(h)=',f1Mundur)

#Pendekatan Selisih Pusat Orde 0(h^2)
f1Pusat=(f(x+h)-f(x-h))/h 
print('Hasil f1 Selisih Mundur orde 0(h)=',f1Pusat)

#Pendekatan Selisih Maju Orde 0(h)
f1Maju=(f(x+h)-f(x))/h 
print('Hasil f1 Selisih Maju Orde 0(h)=',f1Maju)

#Pendekatan Selisih Pusat Orde 0(h^4)
f1PusatOrde4=(-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
print('Hasil f1 Selisih Pusat Orde 0(h^4)=',f1PusatOrde4)