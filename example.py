import turtle as t
import random as r
from tkinter import CENTER, messagebox
n = 1
ws = t.Screen()

#Bata bagian bawah (Jumlah)
jumlah_bawah = int(t.numinput("Input", "Jumlah batu bata pada lapisan paling bawah:"))
min = jumlah_bawah
while not 1<=jumlah_bawah<=25 :
    if jumlah_bawah < 1 :
        messagebox.showinfo("Too small", "Nilai terkecil yang diperbolehkan adalah 1. Mohon coba lagi.")
    if jumlah_bawah > 25 :
        messagebox.showinfo("Too large", "Nilai terbesar yang dibolehkan adalah 25. Mohon coba lagi.")
    jumlah_bawah = int(t.numinput("Input", "Jumlah batu bata pada lapisan paling bawah:"))
    min = jumlah_bawah

#Bata bagian atas (Jumlah)
jumlah_atas = int(t.numinput("Input", "Jumlah batu bata pada lapisan paling atas:"))
max = jumlah_atas
while not 1<=jumlah_atas<=jumlah_bawah :
    if jumlah_atas < 1 :
        messagebox.showinfo("Too small", "Nilai terkecil yang diperbolehkan adalah 1. Mohon coba lagi.")
    if jumlah_atas > jumlah_bawah :
        messagebox.showinfo("Invalid", "Jumlah batu bata atas tidak boleh melebihi batu bata bawah. Mohon coba lagi.")
    jumlah_atas = int(t.numinput("Input", "Jumlah batu bata pada lapisan paling atas:"))
    max = jumlah_atas

#Panjang bata (px)
length_px = int(t.numinput("Input", "Panjang satu buah batu bata (piksel):"))
while not 1<=length_px<=35 :
    if length_px < 1 :
        messagebox.showinfo("Too small", "Nilai terkecil yang diperbolehkan adalah 1. Mohon coba lagi.")
    if length_px > 35 :
        messagebox.showinfo("Too large", "Nilai terbesar yang dibolehkan adalah 35. Mohon coba lagi.")
    length_px = int(t.numinput("Input", "Panjang satu buah batu bata (piksel):"))

#Lebar bata (px)
wide_px = int(t.numinput("Input", "Lebar satu buah batu bata (piksel):"))
while not 1<=wide_px<=25 :
    if wide_px < 1 :
        messagebox.showinfo("Too small", "Nilai terkecil yang diperbolehkan adalah 1. Mohon coba lagi.")
    if wide_px > 25 :
        messagebox.showinfo("Too large", "Nilai terbesar yang dibolehkan adalah 25. Mohon coba lagi.")
    wide_px = int(t.numinput("Input", "Lebar satu buah batu bata (piksel):"))
    
ws.bgcolor('green')
t.speed(0)
x = 0




# Menggunakan rumus Sn untuk menghitung semua jumlah batu bata yang akan terbentuk
n = (jumlah_bawah)-(jumlah_atas)+1
Sn = (n/2)*((2*jumlah_bawah)+(n-1)*(-1))
Sn = int(Sn)
print (n,Sn)

"""col_num = Sn
for i in range (col_num):
    color = ("#"+''.join([r.choice('0123456789ABCDEF') for j in range(6)]))
    print(color)"""
t.hideturtle()


for y in range (1,min-max+2):
    x_init = 0-((length_px*min)/2) #titik awal turtle (x)
    y_init = 0-((wide_px*n)/2) #titik awal turtle (y)
    for x in range (1, min+1):
        if y == 1 or y == n :
            t.color('#BC4A3C')
            t.pencolor('black')
            xo = x_init + (length_px*(x-1))
            yo = y_init + (wide_px*(y-1))
            t.pu()
            t.setx(xo)
            t.sety(yo)
            t.pd()
            t.begin_fill()
            t.forward(length_px)
            t.left(90)
            t.forward(wide_px)
            t.left(90)
            t.forward(length_px)
            t.left(90)
            t.forward(wide_px)
            t.left(90)
            t.pu()
            t.end_fill()
            print (x,y)
        if y > 1 :
            if (y % 2 == 0) : #Saat y genap
                Un = jumlah_bawah - y + 1
                if x == 1 or x == Un :
                    if y == n :
                        continue
                    t.color('#BC4A3C')
                    t.pencolor('black')
                    xo = x_init + (length_px*(x-1))
                    yo = y_init + (wide_px*(y-1))
                    t.pu()
                    t.setx(xo)
                    t.sety(yo)
                    t.pd()
                    t.begin_fill()
                    t.forward(length_px)
                    t.left(90)
                    t.forward(wide_px)
                    t.left(90)
                    t.forward(length_px)
                    t.left(90)
                    t.forward(wide_px)
                    t.left(90)
                    t.pu()
                    t.end_fill()
                    print (x,y)
                if 1<x<Un :
                    if y == n :
                        continue
                    color = ("#"+''.join([r.choice('9312746580AFBDCE') for j in range(6)]))
                    t.color(color)
                    t.pencolor('black')
                    xo = x_init + (length_px*(x-1))
                    yo = y_init + (wide_px*(y-1))
                    t.pu()
                    t.setx(xo)
                    t.sety(yo)
                    t.pd()
                    t.begin_fill()
                    t.forward(length_px)
                    t.left(90)
                    t.forward(wide_px)
                    t.left(90)
                    t.forward(length_px)
                    t.left(90)
                    t.forward(wide_px)
                    t.left(90)
                    t.pu()
                    t.end_fill()
                    print (x,y)
            if not (y % 2 == 0) : #Saat y ganjil
                Un = jumlah_bawah - y + 1
                if x == 1 or x == Un :
                    if y == n :
                        continue
                    t.color('#BC4A3C')
                    t.pencolor('black')
                    xo = x_init + (length_px*(x-1))
                    yo = y_init + (wide_px*(y-1))
                    t.pu()
                    t.setx(xo)
                    t.sety(yo)
                    t.pd()
                    t.begin_fill()
                    t.forward(length_px)
                    t.left(90)
                    t.forward(wide_px)
                    t.left(90)
                    t.forward(length_px)
                    t.left(90)
                    t.forward(wide_px)
                    t.left(90)
                    t.pu()
                    t.end_fill()
                    print (x,y)
                if 1<x<Un :
                    if y == n :
                        continue
                    color = ("#"+''.join([r.choice('A1B2C3D45E67F890') for j in range(6)]))
                    t.color(color)
                    t.pencolor('black')
                    xo = x_init + (length_px*(x-1))
                    yo = y_init + (wide_px*(y-1))
                    t.pu()
                    t.setx(xo)
                    t.sety(yo)
                    t.pd()
                    t.begin_fill()
                    t.forward(length_px)
                    t.left(90)
                    t.forward(wide_px)
                    t.left(90)
                    t.forward(length_px)
                    t.left(90)
                    t.forward(wide_px)
                    t.left(90)
                    t.pu()
                    t.end_fill()
                    print (x,y)
        
    min = min - 1
y_init = 0-((wide_px*n)/2)
t.setpos(0,y_init - 45)
t.write("Candi warna-warni dengan " + str(Sn) + " batu bata", font=("Verdana",15,"normal"), align="center")    
t.done()
        




# UNUSED CODE
"""for _ in range(max,min+1): 
    x = 0-((length_px*jumlah_bawah)/2)
    t.pu()
    t.setx(x)
    t.pd()
    t.forward(length_px*jumlah_bawah)
    t.pu()
    y = 0+(wide_px*n)
    t.sety(y)
    t.pd()
    t.backward(length_px*jumlah_bawah)
    jumlah_bawah = jumlah_bawah - 1
    n = n + 1

#Mengembalikan variable ke nilai semestinya
jumlah_bawah = min
t.pu()
t.sety(wide_px)
n = 1
t.right(90)
x = 0-((length_px*jumlah_bawah)/2)
t.pu()
t.setx(x)
t.pd()
t.forward(wide_px)

for _ in range(max,min+1):
    t.color('black')
    t.begin_fill()
    for i in range (jumlah_bawah):
        x = x+(length_px)
        t.pu()
        t.setpos(x,wide_px*n)
        t.pd()
        t.forward(wide_px)
    t.end_fill()
    jumlah_bawah = jumlah_bawah - 1
    x = 0-((length_px*jumlah_bawah)/2)
    t.pu()
    n = n + 1
    t.setpos(x,wide_px*n)
    print("Hi",_)
    t.pd()
    if not (min==_):
        t.forward(wide_px) """
