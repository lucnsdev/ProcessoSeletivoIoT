# @Developed by @lucns

'''
------------------------------------ OBSERVAÇÃO ---------------------------------

                ESTE SIMULADOR (WOKWI) É EXTREMAMENTE LENTO.

Neste projeto é usado a função 'time.ticks_ms()' no arquivo 'scheduler_time.py' 
para capturar o tempo decorrido em milisegundos e usar no non-blocking delay. 
Mas o uso continuo dela afeta no desempenho. 
A velocidade de simulação cai para 20%.

Ela é usada para gerenciar a contagem de tempo sem travar o restante do sistema.
Se não usar non-blocking delay fica dificil capturar os clicks dos botões. 
Foi dificil construir esse projeto por mais que seja "um mero semaforo". 
Pois o WOKWI não mostra os stacktraces corretamente. 
Mensiona linhas inexistentes e mostra na saída apenas o nome da função principal. 
Também há muitos bugs na simulação do circuito eletrico. 
Como por exemplo, não detecta curto-circuitos. A pinagem real do Raspberry PI PICO
não condiz com a real.

Importante:
    Para desativar o non-blocking e testar o circuito mais rapido, 
    basta descomentar a linha 12 do 'scheduler_time.py'.
----------------------------------------------------------------------------------

'''

import time
import tm1637
from machine import Pin
from button import Button
from scheduler_time import Scheduler

display = tm1637.TM1637(clk=Pin(21), dio=Pin(20))
button = Button(1)
scheduler = Scheduler()

buzzer = Pin(28, Pin.OUT);
led_pins = [2, 3, 4, 6, 7, 8]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]
aGreen = leds[2]
aYellow = leds[1]
aRed = leds[0]
bGreen = leds[5]
bYellow = leds[4]
bRed = leds[3]

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
    aRed.high() 
    bRed.high()
    while True:
        if state == 0: # verde
            if avenue == 'A':
                aRed.low() 
                aGreen.high()
            else: 
                bRed.low() 
                bGreen.high()
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
                aGreen.low()
                aYellow.high()
            else:
                bGreen.low()
                bYellow.high()
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
                aYellow.low()
                aRed.high()
            else:
                bYellow.low()
                bRed.high()
            timeCounter = 0
            scheduler.schedule(timeRed) # agendar contagem regressiva
            while not scheduler.thrigger():
                tc = scheduler.getTime()
                if timeCounter != tc: # atualiza o display somente se a contagem mudar
                    timeCounter = tc
                    showInDisplay(tc)
                    if goToPedestrianMode: print("Saindo do modo pedestre em " + str(tc) + "s.");
                    else: print("Saindo do vermelho em " + str(tc) + "s.");
                    buzzer.toggle()
            buzzer.low();
            goToPedestrianMode = False
            state = 0
            break

# ------------------------- main ------------------------ #
def main():# @Developed by @lucns

'''
------------------------------------ OBSERVAÇÃO ---------------------------------

                ESTE SIMULADOR (WOKWI) É EXTREMAMENTE LENTO.

Neste projeto é usado a função 'time.ticks_ms()' no arquivo 'scheduler_time.py' 
para capturar o tempo decorrido em milisegundos e usar no non-blocking delay. 
Mas o uso continuo dela afeta no desempenho. 
A velocidade de simulação cai para 20%.

Ela é usada para gerenciar a contagem de tempo sem travar o restante do sistema.
Se não usar non-blocking delay fica dificil capturar os clicks dos botões. 
Foi dificil construir esse projeto por mais que seja "um mero semaforo". 
Pois o WOKWI não mostra os stacktraces corretamente. 
Mensiona linhas inexistentes e mostra na saída apenas o nome da função principal. 
Também há muitos bugs na simulação do circuito eletrico. 
Como por exemplo, não detecta curto-circuitos. A pinagem real do Raspberry PI PICO
não condiz com a real.

Importante:
    Para desativar o non-blocking e testar o circuito mais rapido, 
    basta descomentar a linha 12 do 'scheduler_time.py'.
----------------------------------------------------------------------------------

'''

import time
from tm1637 import TM1637
from machine import Pin
from button import Button
from scheduler_time import Scheduler

display = TM1637(clk=Pin(21), dio=Pin(20))
button = Button(1)
scheduler = Scheduler()

buzzer = Pin(28, Pin.OUT);
led_pins = [2, 3, 4, 6, 7, 8]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]
aGreen = leds[2]
aYellow = leds[1]
aRed = leds[0]
bGreen = leds[5]
bYellow = leds[4]
bRed = leds[3]

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
    aRed.high() 
    bRed.high()
    while True:
        if state == 0: # verde
            if avenue == 'A':
                aRed.low() 
                aGreen.high()
            else: 
                bRed.low() 
                bGreen.high()
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
                aGreen.low()
                aYellow.high()
            else:
                bGreen.low()
                bYellow.high()
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
                aYellow.low()
                aRed.high()
            else:
                bYellow.low()
                bRed.high()
            timeCounter = 0
            scheduler.schedule(timeRed) # agendar contagem regressiva
            while not scheduler.thrigger():
                tc = scheduler.getTime()
                if timeCounter != tc: # atualiza o display somente se a contagem mudar
                    timeCounter = tc
                    showInDisplay(tc)
                    if goToPedestrianMode: print("Saindo do modo pedestre em " + str(tc) + "s.");
                    else: print("Saindo do vermelho em " + str(tc) + "s.");
                    buzzer.toggle()
            buzzer.low();
            goToPedestrianMode = False
            state = 0
            break

# ------------------------- main ------------------------ #
def main():
    buzzer.low();
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
  
