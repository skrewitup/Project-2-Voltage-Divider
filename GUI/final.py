import tkinter as tk
from PIL import ImageTk, Image
import serial.tools.list_ports
import serial

def light_up_button(button):
    button.config(bg='green')

def turn_off_button(button):
    button.config(bg='black')

def make_circle(image_path, size):
    image = Image.open(image_path)
    image = image.resize((size, size), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)

def get_serial_ports():
    ports = serial.tools.list_ports.comports()
    port_names = [port.device for port in ports]
    return port_names

window = tk.Tk()
window.geometry("250x400")
window.configure(background='black')
window.resizable(False, False)
window.title("Skrew It Up")

title_logo = make_circle("img.png", 32)
window.iconphoto(True, title_logo)

def on_button_click():
    global arduino 
    selected = selected_port.get()
    print("Selected Port:", selected)
    arduino = serial.Serial(selected, 9600)  
    port_dropdown.grid_forget()
    submit_button.grid_forget()
    window.geometry("250x350")
    read_from_arduino()  

button1_image = make_circle("img.png", 100)
button1 = tk.Button(window, image=button1_image, relief=tk.SOLID, bd=0, command=lambda: None)
button1.grid(row=0, column=0, padx=10, pady=5)
button1_text = tk.Label(window, text="Button 1", fg="white", bg="black", font=("Roboto", 16))
button1_text.grid(row=0, column=1)
turn_off_button(button1)  # Set default state to off

button2_image = make_circle("img.png", 100)
button2 = tk.Button(window, image=button2_image, relief=tk.SOLID, bd=0, command=lambda: None)
button2.grid(row=1, column=0, padx=10, pady=5)
button2_text = tk.Label(window, text="Button 2", fg="white", bg="black", font=("Roboto", 16))
button2_text.grid(row=1, column=1)
turn_off_button(button2)  # Set default state to off

button3_image = make_circle("img.png", 100)
button3 = tk.Button(window, image=button3_image, relief=tk.SOLID, bd=0, command=lambda: None)
button3.grid(row=2, column=0, padx=10, pady=5)
button3_text = tk.Label(window, text="Button 3", fg="white", bg="black", font=("Roboto", 16))
button3_text.grid(row=2, column=1)
turn_off_button(button3)  # Set default state to off

serial_ports = get_serial_ports()
selected_port = tk.StringVar()
selected_port.set(serial_ports[0])

port_dropdown = tk.OptionMenu(window, selected_port, *serial_ports)
port_dropdown.grid(row=3, column=0, padx=10, pady=10)

submit_button = tk.Button(window, text="Submit", command=on_button_click)
submit_button.grid(row=3, column=1, pady=10)

def read_from_arduino():
    try:
        data = arduino.readline().strip().decode('utf-8', errors='ignore')
    except UnicodeDecodeError:
        print("Error decoding data from Arduino")
        data = ''
        
    if data == '1':
        light_up_button(button1)
    elif data == '2':
        light_up_button(button2)
    elif data == '3':
        light_up_button(button3)
    else:
        turn_off_button(button1)
        turn_off_button(button2)
        turn_off_button(button3)
        
    window.after(1, read_from_arduino) 

window.mainloop()
