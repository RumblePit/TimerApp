from tkinter import *
from playsound import playsound
import time

#Funciones
def clock():
    '''Da la hora actual'''
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)

def timer():
    '''Funcion principal del timer'''
    #Convierte primero el tiempo en segundos
    times = int(hrs.get())*3600 + int(mins.get())*60 + int(secs.get())

    #Si tiempo es mayor a -1 convertira el tiempo dado a sus unidades
    while times > -1:
        minute, second  = (times//60, times % 60)
        hour = 0

        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        hrs.set(hour)
        mins.set(minute)
        secs.set(second)

        wn.update()
        time.sleep(1)

        if(times==0):
            playsound("sounds/tuturu.mp3") # Alarma cuando termina timer
            secs.set("00")
            mins.set("00")
            hrs.set("00")

        times -= 1

def brush():
    '''Establece el tiempo para lavado de dientes'''
    hrs.set("00")
    mins.set("02")
    secs.set("00")

def face():
    '''Establece el tiempo para mascarilla '''
    hrs.set("00")
    mins.set("15")
    secs.set("00")

def eggs():
    '''Establece tiempo para hervir huevos'''
    hrs.set("00")
    mins.set("10")
    secs.set("00")

#Configuraciones de Ventana
wn = Tk()
wn.title("Timer App")
wn.geometry("400x600")
wn.config(bg="#dae5ab")
wn.resizable(False,False)

#Titulo de App
heading = Label(wn, text="Timer App", font="arial 30 bold", bg="#dae5ab", fg="#87313f")
heading.pack(pady=10)

# Leyenda tiempo actual
Label(wn, font=("arial", 15, "bold"), text="Tiempo Actual:", bg="#e9a385").place(x=50, y=70)

# Reloj - Tiempo actual
current_time = Label(wn, font=("arial", 15, "bold"), text="", fg="#604e48", bg="#fa154b")
current_time.place(x=220, y=70)
clock()

#Timer
hrs = StringVar()
Entry(wn, textvariable=hrs, width=2, font="arial 50", bg="#dae5ab", fg="#604e48", bd=0).place(x=30, y=155)
hrs.set("00")

mins = StringVar()
Entry(wn, textvariable=mins, width=2, font="arial 50", bg="#dae5ab", fg="#604e48", bd=0).place(x=150, y=155)
mins.set("00")

secs = StringVar()
Entry(wn, textvariable=secs, width=2, font="arial 50", bg="#dae5ab", fg="#604e48", bd=0).place(x=270, y=155)
secs.set("00")

# Texto de timer
Label(wn, text="horas", font="arial 12", bg="#dae5ab", fg="#604e48").place(x=105, y=200)
Label(wn, text="min", font="arial 12", bg="#dae5ab", fg="#604e48").place(x=225, y=200)
Label(wn, text="seg", font="arial 12", bg="#dae5ab", fg="#604e48").place(x=345, y=200)

# Boton de Inicio
btn = Button(wn, text="Inicio", bg="#fa154b", bd=0, fg="#604e48", width=20, height=2, font="arial 12 bold",
    cursor="hand2", command=timer)
btn.pack(padx=5, pady=40, side=BOTTOM)

# Boton de cepillado de dientes
img_brush = PhotoImage(file="images/brush.png")
brush_btn = Button(wn, image=img_brush, bg="#dae5ab", bd=0, cursor="hand2", command=brush)
brush_btn.place(x=7, y=270)

# Boton de lavado de mascarilla
img_face = PhotoImage(file="images/face.png")
face_btn = Button(wn, image=img_face, bg="#dae5ab", bd=0, cursor="hand2", command=face)
face_btn.place(x=137, y=270)

# Boton de hervido de huevos
img_eggs = PhotoImage(file="images/eggs.png")
eggs_btn = Button(wn, image=img_eggs, bg="#dae5ab", bd=0, cursor="hand2", command=eggs)
eggs_btn.place(x=263, y=270)

wn.mainloop()
