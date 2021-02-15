import pyautogui
import pyaudio
import math
import numpy as np
from capture import soundplot
from threading import Thread



class Main:

    def __init__(self):
        p = pyaudio.PyAudio()
        self.stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)
        self.keyPress = []
        th = Thread(target=self.toPress)
        th.start()
        
        th2 = Thread(target=self.findFreq)
        th2.start()
    def findFreq(self):
        while True:         
            data = np.fromstring(self.stream.read(CHUNK), dtype=np.int16)
            
            self.freq = soundplot(data)
            if not self.freq :
                self.freq = 1
         


            ###################################### TROMPETTE ##########################
            """if 225<=self.freq<=238: #Do en Sib
                self.releaseAll('w')

                if not 'w' in self.keyPress: self.keyPress.append('w')



            elif 192<=self.freq<=207: #Sib en Sib, Lab en Do
                self.releaseAll('s')

                if not 's' in self.keyPress: self.keyPress.append('s')
            
            elif 255<=self.freq<=268.5: #Re en Sib, Do en Do

                self.releaseAll("a")
                if not 'a' in self.keyPress: self.keyPress.append('a')
            
            elif 269.5<=self.freq<=290: #Mi en Sib, Re en Do
                self.releaseAll("d")

                if not 'd' in self.keyPress: self.keyPress.append('d')"""


            ################################### BASSE #########################
            
            if 75<=self.freq<=87: #Fa
                self.releaseAll('w')

                if not 'w' in self.keyPress: self.keyPress.append('w')



            elif 10<=self.freq<=32 and self.freq: #Sol
                self.releaseAll('s')

                if not 's' in self.keyPress: self.keyPress.append('s')
            
            elif 43<=self.freq<=53: #La

                self.releaseAll("a")
                if not 'a' in self.keyPress: self.keyPress.append('a')
            
            elif 90<=self.freq<=100: #Sol
                self.releaseAll("d")

                if not 'd' in self.keyPress: self.keyPress.append('d')


            elif 60<= self.freq <=70:
                pyautogui.click(x=1551,y=936) # Kill
                self.releaseAll(None)

            elif 180<= self.freq <=190:
                pyautogui.click(x=1807,y=947) #Use button
                self.releaseAll(None)

            elif 107<= self.freq <=118:
                pyautogui.click(x=319,y=139) # Exit menu buttons
                self.releaseAll(None)



            else:
                self.releaseAll(None)



    def releaseAll(self, s):
        for string in self.keyPress:
            
            if string is not s:
                self.keyPress.remove(string)
                pyautogui.keyUp(string)


    def toPress(self):
        while True:
            for string in self.keyPress:
                pyautogui.keyDown(string)






if __name__ == '__main__':

    RATE = 22050
    WIDTH = 2
    CHANNELS = 1

    CHUNK = 2048
    
    
    main = Main()
    main.findFreq()