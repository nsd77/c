from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x650")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 650,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 320.0,
    image=background_img)

canvas.create_text(
    565.5, 398.5,
    text = "Forget your password?",
    fill = "#ac0606",
    font = ("Inter-Regular", int(16.0)))

canvas.create_text(
    497.5, 98.5,
    text = "Login",
    fill = "#000000",
    font = ("Inter-Bold", int(32.0)))

canvas.create_text(
    431.0, 192.0,
    text = "Email Address:",
    fill = "#000000",
    font = ("Inter-Bold", int(20.0)))

canvas.create_text(
    409.5, 290.0,
    text = "Password:",
    fill = "#000000",
    font = ("Inter-Bold", int(20.0)))

canvas.create_text(
    497.5, 462.5,
    text = "login",
    fill = "#ffffff",
    font = ("Inter-Regular", int(16.0)))

canvas.create_text(
    497.5, 526.5,
    text = "Register",
    fill = "#000000",
    font = ("Inter-Regular", int(16.0)))

window.resizable(False, False)
window.mainloop()
