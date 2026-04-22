# @Developed by @lucns

print("Teste") # Sem isso o Github Actions rejeita a importação de arquivos secundarios.

import time
from tm1637 import TM1637
from machine import Pin
from button import Button
from scheduler_time import Scheduler

display = TM1637(clk=Pin(12), dio=Pin(13))
button = Button(18)
scheduler = Scheduler()

buzzer = Pin(19, Pin.OUT);
aGreen = Pin(23, Pin.OUT)
aYellow = Pin(22, Pin.OUT)
aRed = Pin(21, Pin.OUT)
bGreen = Pin(5, Pin.OUT)
bYellow = Pin(4, Pin.OUT)
bRed = Pin(2, Pin.OUT)

timePedestrian = 8
timeGreen = 10
timeYellow = 3
timeRed = 8
avenue = 'A'

# -------------------- logic functions -------------------#
def showInDisplay(number):
    display.numbers(00, number)

def runLightsLogic():
    state = 0
    goToPedestrianMode = False
    aRed.on() 
    bRed.on()
    while True:
        if state == 0: # verde
            if avenue == 'A':
                aRed.off() 
                aGreen.on()
            else: 
                bRed.off() 
                bGreen.on()
            timeCounter = 0
            scheduler.schedule(timeGreen) # agendar contagem regressiva
            while not scheduler.thrigger():
                tc = scheduler.getTime()
                if timeCounter != tc: # atualiza o display somente se a contagem mudar
                    timeCounter = tc
                    showInDisplay(tc)
                    print("Saindo do verde em " + str(tc) + "s.");
                if button.onClick():
                    goToPedestrianMode = True
                    print("Entrando em modo pedestre... Ativando amarelo.")
                    break
            state = 2
        elif state == 2: # amarelo
            if avenue == 'A': 
                aGreen.off()
                aYellow.on()
            else:
                bGreen.off()
                bYellow.on()
            timeCounter = 0
            scheduler.schedule(timeYellow) # agendar contagem regressiva
            while not scheduler.thrigger():
                tc = scheduler.getTime()
                if timeCounter != tc: # atualiza o display somente se a contagem mudar
                    timeCounter = tc
                    showInDisplay(tc)
                    if goToPedestrianMode: print("Entrando no modo pedestre em: " + str(tc) + "s.")
                    else: print("Saindo do amarelo em " + str(tc) + "s.");
            state = 3
        elif state == 3: # vermelho
            if goToPedestrianMode: print("Em modo pedestre.")
            if avenue == 'A': 
                aYellow.off()
                aRed.on()
            else:
                bYellow.off()
                bRed.on()
            timeCounter = 0
            scheduler.schedule(timeRed) # agendar contagem regressiva
            while not scheduler.thrigger():
                tc = scheduler.getTime()
                if timeCounter != tc: # atualiza o display somente se a contagem mudar
                    timeCounter = tc
                    showInDisplay(tc)
                    if goToPedestrianMode: 
                      print("Saindo do modo pedestre em " + str(tc) + "s.");
                      buzzer.value(not buzzer.value())
                    else: 
                      print("Saindo do vermelho em " + str(tc) + "s.");
            buzzer.off();
            goToPedestrianMode = False
            state = 0
            break

# ------------------------- main ------------------------ #
def main():
    buzzer.off();
    display.write([0, 0, 0, 0])
    global avenue
    while (True):
        runLightsLogic()
        if avenue == 'A': avenue = 'B'
        else: avenue = 'A'
    
        print("Dois vermelhos por 2 segundos.")
        showInDisplay(2);
        time.sleep(1)
        showInDisplay(1);
        time.sleep(1)
        showInDisplay(0);

if __name__ == '__main__':
    main()
    print("Simulacao finalizada.")
