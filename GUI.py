import serial
import time

arduinoSerialData = serial.Serial('/dev/cu.usbmodem1421', 9600)

from Tkinter import *

app = Tk();
app.title("tkinter")
app.geometry('450x300+200+200')
frame = Frame(app)

labelTempText = StringVar()
labelPresText = StringVar()
labelTemp = Label(frame, textvariable=labelTempText)
labelPres = Label(frame, textvariable=labelPresText)
while True:     #loop forever
    time.sleep(1)  # Sleep (or inWaiting() doesn't give the correct value)
    while (arduinoSerialData.inWaiting() == 0):
        pass
    data = arduinoSerialData.readline()
    if(data != '?+/r/n'):
        pass
    dataArray = data.split(',')
    tempData = float(dataArray[0])
    pressData = float(dataArray[1])
    labelPresText.set("Pressure :" + str(pressData))
    labelTempText.set("Temperature :" + str(tempData))
    labelTemp.pack()
    labelPres.pack()
    frame.pack()
    app.update()

