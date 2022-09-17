import turtle as t
import random as r
from tkinter import messagebox
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
t.speed(1)

    


for _ in range(max,min+1):
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

for _ in range(max,min+1):
    x = 0-((length_px*jumlah_bawah)/2)
    t.pu()
    t.setx(x)
    t.pd()
    t.forward(wide_px)
    for i in range (jumlah_bawah):
        x = x+(length_px)
        t.pu()
        t.setpos(x,wide_px*n)
        t.pd()
        t.forward(wide_px)
    jumlah_bawah = jumlah_bawah - 1
    n = n + 1
