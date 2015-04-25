#!/usr/bin/env python
"""
sms.py - Used to send txt messages.
"""
import serial
import time
 # 3G PC UI Interface Using This COM in HUAW
class TextMessage:
 
    #def __init__(self, recipient="+556781690759", message="Estamos enviando msgs-2"):
    def __init__(self, recipient="+556796784414", message="Estamos enviando msgs-3"):
        self.recipient = recipient
        self.content = message
 
    def setRecipient(self, number):
        self.recipient = number
 
    def setContent(self, message):
        self.content = message
 
    def connectPhone(self):
        self.ser = serial.Serial('COM17', 460800, timeout=5)
        time.sleep(0.1)
 
    def sendMessage(self):
        self.ser.write('ATZ\r')
        time.sleep(0.5)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(0.5)
        self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(0.5)
        self.ser.write(self.content + "\r")
        time.sleep(0.5)
        self.ser.write(chr(26))
        time.sleep(0.5)
 
    def readAllMessage():
        pass
    def disconnectPhone(self):
        self.ser.close()
 
def main():

    sms = TextMessage()
    sms.connectPhone()    
    i = 0

    while(1):

        sms.setContent("Parabens seu Cobaia Viado: "+str(i))
        sms.sendMessage()
        print "Parabens seu Cobaia Viado: " + str(i) + " Enviada."
        i = i + 1

    sms.disconnectPhone()
 
 
if __name__ == '__main__':
    main()