"""
SMTP
¿Qué es y para qué sirve SMTP?
SMTP, Simple Mail Transfer Protocol por sus siglas en inglés, es un protocolo o conjunto de reglas 
de comunicación que utilizan los servidores de correo electrónico para enviar y recibir e-mails.
"""
from email.message import EmailMessage #Construir la estructura del email
import smtplib # conectar con el servidor y enviarlo
from tkinter import *
from tkinter import messagebox
#Python image Library
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk

"------------INTERFAZ TKINTER------------"
ventana =Tk()
ventana.title("ALICACION DE MENSAJERIA")
ventana.geometry("335x385")
ventana.resizable(0,0)
ventana.config(bd=10)

Label(ventana, text="ENVIAR CORREO VIA GMAIL",fg="black",font=("Arial", 15,"bold"),padx=5,pady=5).grid(row=0,column=0,columnspan=2)

#Imagen GMAIL
imagen_gmail=Image.open("logo_gmail.ico")
nueva_imagen=imagen_gmail.resize((125,84))
render=ImageTk.PhotoImage(nueva_imagen)
label_imagen= Label(ventana, image= render)
label_imagen.image=render
label_imagen.grid(row=1,column=0,columnspan=2)

#Variables
destinatario=StringVar()

destinatario=StringVar()
opcion_destinatario = ttk.Combobox(ventana,
    font="consolas 10 bold",
    width=25,
    values=["fjcoronati@gmail.com","programacionsabattini@gmail.com","vavalos282@gmail.com"],
    state="readonly",
    textvariable=destinatario)
opcion_destinatario.grid(row=3, column=1)

def opcion():
    if(otro.get()== 1):
        opcion_destinatario = ttk.Combobox(ventana,
        font="consolas 10 bold",
        width=25,
        values=["fjcoronati@gmail.com","programacionsabattini@gmail.com","vavalos282@gmail.com"],
        textvariable=destinatario)
        opcion_destinatario.grid(row=3, column=1)
    else:
        opcion_destinatario = ttk.Combobox(ventana,
        font="consolas 10 bold",
        width=25,
        values=["fjcoronati@gmail.com","programacionsabattini@gmail.com","vavalos282@gmail.com"],
        state="readonly",
        textvariable=destinatario)
        opcion_destinatario.grid(row=3, column=1)


        
    

otro=IntVar()
otro_check=Checkbutton(ventana,
    text="Otro",
    font="consolas 10 ",
    width=20,
    variable= otro,
    command = opcion              
    )
otro_check.grid(row=5, column=1)

asunto=StringVar(ventana)

Label(ventana, text="Mi correo: mariaavalos7090@gmail.com",fg="white",bg="blue",font=("Arial", 10,"bold"),padx=5,pady=5).grid(row=2,column=0,columnspan=2,pady=5)

Label(ventana, text="Destinatario:",fg="black",font=("Arial", 10,"bold"),padx=5,pady=5).grid(row=3,column=0)

Label(ventana, text="Asunto:",fg="black",font=("Arial", 10,"bold"),padx=5,pady=5).grid(row=6,column=0)
Entry(ventana,textvariable=asunto, width=34).grid(row=6,column=1)

Label(ventana, text="Mensaje:",fg="black",font=("Arial", 10,"bold"),padx=5,pady=5).grid(row=7,column=0)
mensaje=Text(ventana,height=2,width=28,padx=5,pady=5)
mensaje.grid(row=7,column=1)
mensaje.config(font=("Arial", 9),padx=5, pady=5)


"------------ENVIO DE CORREO------------"
def enviar_email():
    remitente = "luisochoa.1495@gmail.com"
    #Estrutura de email
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario.get()
    email["Subject"] = asunto.get()
    email.set_content(str(mensaje.get(1.0, 'end')))
    #Envio de email
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, "clave-personal")
    smtp.sendmail(remitente, destinatario.get(), email.as_string())
    messagebox.showinfo("MENSAJERIA","Mensaje enviado correctamente ")
    smtp.quit()

"------------BOTON------------"
Button(ventana,text="ENVIAR",command=enviar_email,height=2,width=10,bg="black",fg="white",font=("Arial", 10,"bold")).grid(row=8,column=0,columnspan=2,padx=5,pady=10)

ventana.mainloop()