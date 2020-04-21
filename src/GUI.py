#############################################################################
#   Author: Martin Mucha                                                    #
#           xmucha10                                                        #
#   Date:   04/08/2020                                                      #
#   Name:   Calculator GUI                                                  #
#                                                                           #
#   Requirements:   Kivy 1.11.1                                             #
#                   Python 3.7.2                                            #
#                   Windows 7 or higher                                     #
#############################################################################

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
import mathlib
import AdvancedMathFunctions
Config.set('graphics','resizable',0)
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')

firstNumber="0" #result or number that was added before operation
numberString="0" #string containing numbers from input
operation=""
def addNumber(number):
    global numberString
    if len(numberString)<15:
        if (numberString=="0") and (str(number) != ","):
            numberString=str(number)
        elif (numberString=="-0"):
            numberString="-"+str(number)
        else:
            numberString=numberString+str(number)
    print(numberString)
    return numberString

def setFirstNumber():
    global numberString
    global firstNumber
    firstNumber=numberString
    return firstNumber
    
def clearNumber():
    global numberString
    global firstNumber
    numberString="0"
    return numberString

def clearFirstNumber():
    global firstNumber
    firstNumber="0"
    return firstNumber

def addOperation(op):
    global operation
    operation=op
    op=" "+op
    return op

def result():
    global operation
    global firstNumber
    global numberString
    res=""
    if operation=="+":
        res=str(mathlib.add(float(firstNumber.replace(',', '.')),float(numberString.replace(',', '.'))))
    if operation=="-":
        res=str(mathlib.sub(float(firstNumber.replace(',', '.')),float(numberString.replace(',', '.'))))
    if operation=="×":
        res=str(mathlib.mul(float(firstNumber.replace(',', '.')),float(numberString.replace(',', '.'))))
    if operation=="÷":
        res=str(mathlib.div(float(firstNumber.replace(',', '.')),float(numberString.replace(',', '.'))))
    if operation=="√":
    	res=str(AdvancedMathFunctions.root(float(numberString.replace(',', '.')),float(firstNumber.replace(',', '.'))))
    if operation=="^":
    	res=str(AdvancedMathFunctions.power(float(firstNumber.replace(',', '.')),float(numberString.replace(',', '.'))))
    if operation=="!":
    	res=str(AdvancedMathFunctions.factorial(float(firstNumber.replace(',', '.'))))
    print(res)
    firstNumber=res
    return res.replace('.',',')
    
class CalcGUI(FloatLayout):
    def __init__(self,**kwargs):
        super(CalcGUI,self).__init__(**kwargs)

        #labels
        
        self.firstNumber = Label(text=str(firstNumber), size_hint=(.4, .15),pos_hint={'x':.4, 'y':.9}, font_size = 50, halign="left", text_size=(700,100))
        self.add_widget(self.firstNumber)

        self.numberLabel = Label(text=str(numberString), size_hint=(.4, .15),pos_hint={'x':.4, 'y':.8}, font_size = 70, halign="left", text_size=(700,100))
        self.add_widget(self.numberLabel)

        #buttons
        
        self.buttonOne = Button(text="1",size_hint=(.2,.2),on_press = self.addOne, pos_hint={'x':.0, 'y':.6}, font_size = 70 )        
        self.add_widget(self.buttonOne)
        
        self.buttonTwo= Button(text="2",size_hint=(.2,.2),on_press = self.addTwo, pos_hint={'x':.2, 'y':.6 }, font_size = 70)        
        self.add_widget(self.buttonTwo)
        
        self.buttonThree = Button(text="3",size_hint=(.2,.2),on_press = self.addThree, pos_hint={'x':.4, 'y':.6 }, font_size = 70)        
        self.add_widget(self.buttonThree)
        
        self.buttonFour = Button(text="4",size_hint=(.2,.2),on_press = self.addFour, pos_hint={'x':.0, 'y':.4}, font_size = 70)        
        self.add_widget(self.buttonFour)
        
        self.buttonFive = Button(text="5",size_hint=(.2,.2),on_press = self.addFive , pos_hint={'x':.2, 'y':.4}, font_size = 70)        
        self.add_widget(self.buttonFive)
        
        self.buttonSix = Button(text="6",size_hint=(.2,.2),on_press = self.addSix, pos_hint={'x':.4, 'y':.4}, font_size = 70)        
        self.add_widget(self.buttonSix)
        
        self.buttonSeven = Button(text="7",size_hint=(.2,.2),on_press = self.addSeven , pos_hint={'x':.0, 'y':.2}, font_size = 70)        
        self.add_widget(self.buttonSeven)
        
        self.buttonEight = Button(text="8",size_hint=(.2,.2),on_press = self.addEight , pos_hint={'x':.2, 'y':.2}, font_size = 70)        
        self.add_widget(self.buttonEight)
        
        self.buttonNine = Button(text="9",size_hint=(.2,.2),on_press = self.addNine , pos_hint={'x':.4, 'y':.2}, font_size = 70)        
        self.add_widget(self.buttonNine)

        self.buttonZero = Button(text="0",size_hint=(.2,.2),on_press = self.addZero , pos_hint={'x':.0, 'y':.0}, font_size = 70)        
        self.add_widget(self.buttonZero)

        #self.buttonPointDisabled = Button(text=".",size_hint=(.2,.2), background_color=(0.75,0.75,0.75,1) , pos_hint={'x':.2, 'y':.0}, font_size = 70)        
        #self.add_widget(self.buttonPointDisabled)

        self.buttonPoint = Button(text=",",size_hint=(.2,.2),on_press = self.addPoint , pos_hint={'x':.2, 'y':.0}, font_size = 70)        
        self.add_widget(self.buttonPoint)

        self.buttonClear = Button(text="C",size_hint=(.2,.2),on_press = self.clear , pos_hint={'x':.4, 'y':.0}, font_size = 70)        
        self.add_widget(self.buttonClear)

        self.buttonPlus = Button(text="+",size_hint=(.2,.2),on_press = self.plus , pos_hint={'x':.6, 'y':.6}, font_size = 70)        
        self.add_widget(self.buttonPlus)
        
        self.buttonMinus = Button(text="-",size_hint=(.2,.2),on_press = self.minus , pos_hint={'x':.6, 'y':.4}, font_size = 70)        
        self.add_widget(self.buttonMinus)
        
        self.buttonTimes = Button(text="×",size_hint=(.2,.2),on_press = self.times , pos_hint={'x':.6, 'y':.2}, font_size = 70)        
        self.add_widget(self.buttonTimes)
        
        self.buttonEquals = Button(text="=",size_hint=(.2,.2),on_press = self.equals , pos_hint={'x':.6, 'y':.0}, font_size = 70)        
        self.add_widget(self.buttonEquals)

        self.buttonPlus = Button(text="÷",size_hint=(.2,.2),on_press = self.div , pos_hint={'x':.8, 'y':.6}, font_size = 70)        
        self.add_widget(self.buttonPlus)
        
        self.buttonMinus = Button(text="^",size_hint=(.2,.2),on_press = self.over , pos_hint={'x':.8, 'y':.4}, font_size = 70)        
        self.add_widget(self.buttonMinus)
        
        self.buttonRoot = Button(text="√",size_hint=(.2,.2),on_press = self.root , pos_hint={'x':.8, 'y':.2}, font_size = 70)        
        self.add_widget(self.buttonRoot)
        
        self.buttonEquals = Button(text="!",size_hint=(.2,.2),on_press = self.fact , pos_hint={'x':.8, 'y':.0}, font_size = 70)        
        self.add_widget(self.buttonEquals)

    #button functions

    def addOne(self,event):
        self.numberLabel.text = addNumber(1)
    def addTwo(self,event):
        self.numberLabel.text = addNumber(2)
    def addThree(self,event):
        self.numberLabel.text = addNumber(3)
    def addFour(self,event):
        self.numberLabel.text = addNumber(4)
    def addFive(self,event):
        self.numberLabel.text = addNumber(5)
    def addSix(self,event):
        self.numberLabel.text = addNumber(6)
    def addSeven(self,event):
        self.numberLabel.text = addNumber(7)
    def addEight(self,event):
        self.numberLabel.text = addNumber(8)
    def addNine(self,event):
        self.numberLabel.text = addNumber(9)
    def addZero(self,event):
        self.numberLabel.text = addNumber(0)
        
    def addPoint(self,event):
        self.numberLabel.text = addNumber(",")
        #self.buttonPoint.pos_hint={'x':1, 'y':1}
        self.buttonPoint.disabled = True
        #self.buttonPointDissabled.pos_hint={'x':1, 'y':1}
        
    def clear(self,event):
        if self.numberLabel.text == "0":
            self.firstNumber.text = clearFirstNumber()
        else:
            self.numberLabel.text = clearNumber()
        #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
        self.buttonPoint.disabled = False
        
    def plus(self,event):
        global operation
        if operation=="":
            print("+")
            self.firstNumber.text = setFirstNumber() + addOperation("+")
        else:
            self.firstNumber.text = result() + addOperation("+")
        self.numberLabel.text = clearNumber()
        #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
        self.buttonPoint.disabled = False
        
    def minus(self,event):
        print("-")
        if self.numberLabel.text == "0":
                self.numberLabel.text=addNumber("-0")
        else:
            global operation
            if operation=="":
                print("-")
                self.firstNumber.text = setFirstNumber() + addOperation("-")
            else:
                self.firstNumber.text = result() + addOperation("-")
            self.numberLabel.text = clearNumber()
            #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
            self.buttonPoint.disabled = False
        
    def times(self,event):
        global operation
        if operation=="":
            print("×")
            self.firstNumber.text = setFirstNumber() + addOperation("×")
        else:
            self.firstNumber.text = result() + addOperation("×")
        self.numberLabel.text = clearNumber()
        #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
        self.buttonPoint.disabled = False
        
    def div(self,event):
        global operation
        if operation=="":
            print("÷")
            self.firstNumber.text = setFirstNumber() + addOperation("÷")
        else:
            self.firstNumber.text = result() + addOperation("÷")
        self.numberLabel.text = clearNumber()
        #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
        self.buttonPoint.disabled = False
        
    def over(self,event):
        global operation
        if operation=="":
            print("^")
            self.firstNumber.text = setFirstNumber() + addOperation("^")
        else:
            self.firstNumber.text = result() + addOperation("^")
        self.firstNumber.text = setFirstNumber() + addOperation("^")
        self.numberLabel.text = clearNumber()
        #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
        self.buttonPoint.disabled = False
        
    def root(self,event):
        global operation
        if operation=="":
            print("√")
            self.firstNumber.text = setFirstNumber() + addOperation("√")
        else:
            self.firstNumber.text = result() + addOperation("√")
        #print("√")
        self.firstNumber.text = setFirstNumber() + addOperation("√")
        self.numberLabel.text = clearNumber()
        #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
        self.buttonPoint.disabled = False

    def fact(self,event):
        global operation
        if operation=="":
            print("!")
            self.firstNumber.text = setFirstNumber() + addOperation("!")
        else:
            self.firstNumber.text = result() + addOperation("!")
        self.firstNumber.text = setFirstNumber() + addOperation("!")
        self.numberLabel.text = clearNumber()
        #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
        self.buttonPoint.disabled = False

        
    def equals(self,event):
        global operation
        if operation=="":
            print("=")
            self.firstNumber.text = setFirstNumber()
        else:
            self.firstNumber.text = result()
        #self.firstNumber.text ="= "+ setFirstNumber()
        self.numberLabel.text = clearNumber()
        operation=""
        #self.buttonPoint.pos_hint={'x':.2, 'y':.0}
        self.buttonPoint.disabled=False
        
        
class Calc(App):
    def build(self):
        return CalcGUI()


if __name__ == '__main__':
    Calc().run()
