#Invocacion de selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# #Invocacion de Tkinter
from tkinter import *
from tkinter import messagebox 


#ventana de root
root = Tk()
root.minsize(150,150)
root.title('Tiempo Buenos Aires')


# #Selenium

chrome_options = Options()
chrome_options.add_argument("--headless")

#Pantalla de Display
driver = webdriver.Chrome(options = chrome_options)
time.sleep(1)

busqueda = driver.get('https://www.meteored.com.ar/tiempo-en_Buenos+Aires-America+Sur-Argentina-Ciudad+Autonoma+de+Buenos+Aires-SABE-1-13584.html')

boton_aceptar = driver.find_element(By.ID, "sendOpGdpr")
boton_aceptar.click()

tabla = driver.find_element(By.CLASS_NAME, "tabla-horas")
tabla = tabla.text

tiempo_hoy = tabla.split('FPS:')[0].split('\n')[0:-1]

print(tiempo_hoy)

driver.quit()

marco = Frame(root, width=250, height=250)
marco.config(
            padx=15,
            pady=15,
            bd=1,
            relief=SOLID,            
)

marco.pack(anchor=CENTER)
marco.propagate(False)

hora_Label = Label(marco, text= "Hora").pack(anchor=CENTER)
hora_Label_output = Label(marco, text=tiempo_hoy[0])
hora_Label_output.config(
    font=('Arial', 20),
    fg= 'Black'
)
hora_Label_output.pack(anchor=CENTER) 


temp_Label = Label(marco, text= "Temperatura").pack(anchor=CENTER)
temp_Label_output = Label(marco, text=tiempo_hoy[1])
temp_Label_output.config(
    font=('Arial', 15),
    fg= 'Black'
)

temp_Label_output.pack(anchor=CENTER)

v_viento_Label = Label(marco, text= "Velocidad de Viento").pack(anchor=CENTER) 
v_viento_output = Label(marco, text= tiempo_hoy[4])
v_viento_output.config(
    font=('Arial', 20),
    fg= 'Black'
)

v_viento_output.pack(anchor=CENTER)

def salir():
    l = messagebox.askyesno('Salir', 'Desea salir de la aplicacion?')

    if l != False:
        root.destroy()



Button(marco, text='Salir' ,command=salir).pack(anchor=CENTER)


root.mainloop()


