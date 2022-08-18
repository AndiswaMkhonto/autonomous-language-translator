import tkinter as tk
from tkinter import filedialog
from tkinter import *

import numpy as np
from PIL import ImageTk, Image

import numpy
# load the trained model to classify sign
from keras.models import load_model
import googletrans
from googletrans import Translator

translator = Translator()

model = load_model('traffic_classifier.h5')

# dictionary to label all traffic signs class.
classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}

# initialise GUI
top = tk.Tk()
top.geometry('800x600')
# top.configure(bg='blue')
top.title('Traffic sign classification')
# top.configure(bg='white')
# top.configure(background='green')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict([image])[0]
    numpy.argmax(pred)
    sign = classes[numpy.argmax(pred) + 1]
    print(sign)
    # print(googletrans.LANGUAGES)
    label.configure(foreground='#011638', text=sign)
    result = translator.translate(sign, src='en', dest='af')

    # print(result.src)
    # print(result.dest)
    # print(result.origin)
    print(result.text)
    # print(result.pronunciation)

    result1 = translator.translate(sign, src='af', dest='st')
    # print(result1.src)
    # print(result1.dest)
    # print(result1.origin)
    print(result1.text)
    # print(result1.pronunciation)

    result2 = translator.translate(sign, src='st', dest='xh')
    # print(result2.src)
    # print(result2.dest)
    # print(result2.origin)
    print(result2.text)
    # print(result2.pronunciation)

    result3 = translator.translate(sign, src='xh', dest='zu')
    # print(result3.src)
    # print(result3.dest)
    # print(result3.origin)
    print(result3.text)
    # print(result3.pronunciation)

    #Converting text to sound
    # import pyttsx3
    #
    # engine = pyttsx3.init()
    # engine.say(result3)
    # engine.runAndWait()

    # import pyttsx3
    # speaker = pyttsx3.init()
    # speaker.say(result)
    # speaker.runAndWait()

    # from gtts import gTTS
    # from playsound import playsound
    #
    # mytext = result
    # language = 'af'
    # myobj = gTTS(text=mytext, lang=language, slow=True)
    # myobj.save("welcome1.mp3")
    # playsound("welcome1.mp3")

    # from text_to_speech import speak
    #
    # speak("how are you", "af", save=True, file="speech.mp3")


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Know Your Traffic Sign", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
