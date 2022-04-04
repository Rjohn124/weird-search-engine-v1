import wikipedia
import tkinter as tk
from playsound import playsound
from gtts import gTTS

root=tk.Tk()
root.geometry('500x500+550+200')
root.config(bg='blue')

def get_input():
    result=textbox.get("1.0","end-1c")
    wikiResult = wikipedia.summary(str(result), sentences = 2)
    textbox.delete(1.0, 'end')
    myobj = gTTS(text=str(wikiResult), lang='en', slow=False)
    myobj.save("welcome.mp3")
    playsound("welcome.mp3")
    label=tk.Label(root, text=str(wikiResult), font=('Calibri', 18, 'bold'), wraplengt=500)
    label.config(bg='blue')
    label.pack()

textbox=tk.Text(root, height=3, width=50)
textbox.pack()

enter=tk.Button(root, height=1, width=10, text="Enter", 
                    command=lambda: get_input())

enter.pack()

tk.mainloop()
