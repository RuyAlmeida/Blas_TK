from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from time import strftime
import datetime
import locale
import tkintermapview
from tkcalendar import Calendar
from gnewsclient import gnewsclient

#Definições da janela do TKINTER
root = Tk()
root.title("Blas_TK")
root.attributes('-fullscreen', True)
root.configure(bg="#404040")

#styl = ttk.Style()
#styl.configure('blue.TSeparator', background="#c65bfc")

#separator = ttk.Separator(root, orient='vertical', style='blue.TSeparator')
#separator.place(x=1560, y=15, height=557)

#separator2 = ttk.Separator(root, orient='horizontal', style='blue.TSeparator')
#separator2.place(x=1620, y=572, width=250)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        #local_time = datetime.now(home)
        #current_time = local_time.strftime("%I:%M %p")
        #clock.config(text=current_time)
        #name.config(text="CURRENT TIME")
        # print(result)

        #Link da API do OpenWeather
        api = (
            "https://api.openweathermap.org/data/2.5/weather?q="
            +city
            +"&appid=ab7987871d22363c09e4d1bd08aafc2b"
            +"&lang=pt_br"
        )

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"] #Extrai descrição do clima
        tempt = int(json_data["main"]["temp"] - 273.15) #Extrai temperatura atual
        feels_like = int(json_data["main"]["feels_like"] - 273.15) # Extrai sensação térmica
        press = json_data["main"]["pressure"] #Exrtai pressão atmosférica
        humid = json_data["main"]["humidity"] #Extrai humidade do ar
        wind_1 = json_data["wind"]["speed"] #Extrai velocidade do vento
        max_1 = int(json_data["main"]["temp_max"] - 273.15) #Extrai temperatura máxima
        min_1 = int(json_data["main"]["temp_min"] - 273.15) #Extrai temperatura mínima
        coorde = float(json_data["coord"]["lon"]) #Extrai informação de longitude
        coorde2 = float(json_data["coord"]["lat"]) #Extrai informação de latitude

        #formatação das informações json
        temp.config(text=(tempt,"°"))
        cond.config(text=("Sensação Térmica:", feels_like, "°C")) #description, "\n",
        wind.config(text=wind_1)
        humidity.config(text=humid)
        pressure.config(text=press)
        tempera.config(text=("Max:", max_1, "°C", "|", "Mín:", min_1, "°C"))

        map_widget = tkintermapview.TkinterMapView(root, width=300, height=300)
        map_widget.place(x=1590, y=245)
        map_widget.set_position(coorde2, coorde) #coordenada do mapa
        map_widget.set_zoom(12)
        #map_widget.set_overlay_tile_server("https://tile.openweathermap.org/map/precipitation_new/12/187/296.png?appid=ab7987871d22363c09e4d1bd08aafc2b")  # sea-map overlay

        root.after(50000, getWeather)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Input!")

#ícone de pesquisa
Search_icon = PhotoImage(file="/home/malyutka/Documentos/Alarme Python/search_icon.png")
myimage_icon = Button(
    image=Search_icon, width=28, height=28, borderwidth=0, cursor="hand2", bg="#fff", command=getWeather
)
myimage_icon.place(x=1850, y=40)
        
# Search Box
#Search_image = PhotoImage(file="/home/malyutka/Documentos/Alarme Python/box.png")
#myimage = Label(image=Search_image)
#myimage.place(x=220, y=20)

#Campo de pesquisa da localização
textfield = tk.Entry(
    root,
    justify="center",
    width=20,
    font=("Arial", 18),
    bg="#fff",
    fg="#000",
    border=0,
)
textfield.place(x=1600, y=40)
textfield.focus()

# Resizing the image
#image = Image.open("/home/malyutka/Documentos/Alarme Python/search_icon.png")
# Resize the image using resize() method
#resize_image = image.resize((250, 250))

# Logo
#Logo_image = ImageTk.PhotoImage(resize_image)
#logo = Label(image=Logo_image)
#logo.size
#logo.place(x=325, y=165)

# Bottom Box
#Frame_image = PhotoImage(file="/home/malyutka/Documentos/Alarme Python/box.png")
#frame_myimg = Label(image=Frame_image)
#frame_myimg.place(x=10, y=450)
#frame_myimg.pack(side=BOTTOM)

# Time
#name = Label(root, font=("arial", 16, "bold"))
#name.place(x=380, y=100)
#clock = Label(root, font=("Georgia", 20, "bold"))
#clock.place(x=390, y=130)

# Labels de formatação do layout
# Label 1
label1 = Label(
    root, text="Vento", font=("Arial", 14, "bold"), fg="white", bg="#404040"
)
label1.place(x=1600, y=180)
# Label 2
label1 = Label(
    root, text="Umidade", font=("Arial", 14, "bold"), fg="white", bg="#404040"
)
label1.place(x=1700, y=180)
# Label 3
label1 = Label(
    root, text="Pressão", font=("Arial", 14, "bold"), fg="white", bg="#404040"
)
label1.place(x=1815, y=180)

#Temperatura, condição, mínimo/máxiimo
temp = Label(font=("Arial", 40, "bold"), fg="#fff", bg="#404040")
temp.place(x=1600, y=75)
cond = Label(font=("Arial", 12, "bold"), fg="#fff", bg="#404040")
cond.place(x=1600, y=150)
tempera = Label(font=("Arial", 12, "bold"), fg="white", bg="#404040")
tempera.place(x=1600, y=130)


#Vento, humidade e pressão atmosférica
wind = Label(text="....", font=("Arial", 12, "bold"), fg="#fff", bg="#404040")
wind.place(x=1610, y=210)
humidity = Label(text="....", font=("Arial", 12, "bold"), fg="#fff", bg="#404040")
humidity.place(x=1730, y=210)
pressure = Label(text="....", font=("Arial", 12, "bold"), fg="#fff", bg="#404040")
pressure.place(x=1830, y=210)

#Formataçao do relógio principal
def relogio():

    horario = strftime("%H:%M:%S")
    clock.config(text = horario)
    clock.after(200, relogio)
    
clock = Label(root, font = ("Arial", 800), fg="#fff", bg = "#404040")
clock.pack()
clock.place(x=850, y=15)

relogio()

#Formatação da data atual
def dias():

    locale.setlocale(locale.LC_ALL, "pt_PT.UTF-8")
    date = datetime.datetime.now()
    format_date = f"{date:%A, %d %b %Y}" #formatação da data

    label = Label(root, text = format_date, font = ("Arial", 17), fg="#fff", bg = "#404040")
    label.pack()
    label.place(x=850, y=75)

dias()

#Formatação do calendário
def date():

    cal = Calendar(root, selectmode="day", background="black", foreground="white")
    cal.place(x=840, y=120)

date()

#Formatação do campo de notícias
def news():
    client = gnewsclient.NewsClient(
    language=lang.get(), location=loc.get(), topic=top.get(), max_results=5)
    news_list = client.get_news()
    result_title.set(news_list[0]["title"] + "\n" +
                     news_list[1]["title"] + "\n" + 
                     news_list[2]["title"] + "\n" + 
                     news_list[3]["title"] + "\n" + 
                     news_list[4]["title"])   
    
result_title = StringVar()
result_link = StringVar()

#campos de parametrização de notícias
Label(root, text="Idioma: ", fg="#fff", bg="#404040").place(x=1100, y=40)
Label(root, text="País: ", fg="#fff", bg="#404040").place(x=1100, y=70)
Label(root, text="Tópico: ", fg="#fff", bg="#404040").place(x=1100, y=100)

#Formatação no layout (notícias)
lang = Entry(root)
lang.place(x=1170, y=40)
 
loc = Entry(root)
loc.place(x=1170, y=70)
 
top = Entry(root)
top.place(x=1170, y=100)

Label(root, text="", textvariable=result_title, fg="#fff", bg="#404040", wraplength=465, justify="left").place(x=1100, y=140)

Button(root, text="Ok", command=news, bg="#fff").place(x=1340, y=90)

#mapa de trânsito waze
#<iframe src="https://embed.waze.com/iframe?zoom=16&lat=-23.503413&lon=-46.635714&ct=livemap" width="600" height="450" allowfullscreen></iframe>

#Comando para encerrar o programa
Button = ttk.Button(root, text='Finalizar',command=root.destroy)
Button.place(x=0, y=1050)

root.mainloop()