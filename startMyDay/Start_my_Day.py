import tkinter as tk
from tkinter import Canvas, Frame, Label, filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in Frame.winfo_children():
        widget.destroy


    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables","*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        Label = tk.label(Frame, text=app, bg="gray")
        Label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

Canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
Canvas.pack()

Frame = tk.Frame(root, bg="White")
Frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10
                     , pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10
                     , pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()


for app in apps:
    label = tk.Label(Frame, text=app)
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")
