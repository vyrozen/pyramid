import turtle as t
import random as r
t.bgcolor("green")
bottom = min = int(t.numinput("Input","Silahkan masukkan input untuk lapisan bawah (Max = 25)",7,minval=1,maxval=25))
top = max = int(t.numinput("Input","Silahkan masukkan input untuk lapisan atas (Max = n Lapisan bawah)",1,minval=1,maxval=bottom))
length_px = int(t.numinput("Input","Silahkan masukkan input untuk panjang satu buah bata (Max = 35)",35,minval=1,maxval=35))
wide_px = int(t.numinput("Input","Silahkan masukkan input untuk lebar satu buah bata (Max = 25)",25,minval=1,maxval=25))
Sn=0
t.pu()
t.speed(0)
y_init = -((bottom-top+1)*(wide_px))/2
warna = t.colormode(255)
for y in range (1,bottom-top+2):
    x_init = -(bottom*length_px)/2
    y_init = y_init + wide_px
    t.setpos(x_init,y_init)
    for x in range (1,bottom+1):
        t.fillcolor(r.randint(0,255), r.randint(0,255), r.randint(0,255))
        for _ in range (2):
            t.begin_fill()
            t.pd()
            if y == 1 or y == (min-max+1) or x == 1 or x == (min+1-y):
                t.fillcolor("#BC4A3C")
            t.forward(length_px)
            t.right(90)
            t.forward(wide_px)
            t.right(90)
            t.end_fill()
            t.pu()
            Sn += .5
        t.forward(length_px)
    bottom -= 1
t.setpos(0,(-((wide_px*y)/2)) - 45)
t.write("Candi warna-warni dengan " + str(int(Sn)) + " batu bata", font=("Verdana",15,"normal"), align="center")   
t.done()
