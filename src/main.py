# Desenvolvivo por @lucns

print("Teste") # Sem isso o Github Actions rejeita a importação de arquivos secundários.

import network
import time
from machine import Pin, PWM
from neopixel import NeoPixel
import dht
import ujson
from umqtt.simple import MQTTClient

# Parametros do servidor MQTT
MQTT_CLIENT_ID = "lucns_pnaat"
MQTT_BROKER    = "broker.emqx.io"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC_TX  = "/lucns/estacao_metereologica/android"                            # Topico do MQTT subscrito no android
MQTT_TOPIC_RX  = "/lucns/estacao_metereologica/esp32"                              # Topico do MQTT subscrito no embarcado

servo = PWM(Pin(12), freq=50, duty=0)
purpleLed = PWM(Pin(22), freq=50, duty=0)
sensor = dht.DHT22(Pin(13))
relay = Pin(15, Pin.OUT)
ledRgb = NeoPixel(Pin(23), 1)
switch1 = Pin(34, Pin.IN, Pin.PULL_UP)
switch2 = Pin(35, Pin.IN, Pin.PULL_UP)
switch3 = Pin(32, Pin.IN, Pin.PULL_UP)
switch4 = Pin(33, Pin.IN, Pin.PULL_UP)
switch5 = Pin(25, Pin.IN, Pin.PULL_UP)
switch6 = Pin(26, Pin.IN, Pin.PULL_UP)
switch7 = Pin(27, Pin.IN, Pin.PULL_UP)
switch8 = Pin(14, Pin.IN, Pin.PULL_UP)

relayState = False
pwmLed = 0
servoAngle = 0

def mapValue(inMax, outMax, value):    
    inMin = 0
    outMin = 0
    return (value - inMin) * (outMax - outMin) / (inMax - inMin) + outMin

def moveServo(angle):
    #servo.duty(int(mapValue(180, 1023, angle)))
    servo.duty(int(((angle) / 180 * 2 + 0.5) / 20 * 1023))

def onReceive(topic, message):
    data = ujson.loads(message.decode("utf-8"))
    print(data)
    if "relay_state" in data:
        if data["relay_state"]:
            print("Rele ativado.")
            relay.on()
        elif not data["relay_state"]:
            print("Rele desativado.")
            relay.off()
    if "servo_angle" in data:
        servoAngle = data["servo_angle"]
        moveServo(servoAngle)        
        print("Angulo do servo ajustado para {}".format(servoAngle))
    if "pwm_led" in data: 
        pwmLed = data["pwm_led"]
        purpleLed.duty(int(mapValue(255, 100, pwmLed)))
        print("PWM do led roxo ajustado para {}".format(pwmLed))

def connectWifi():
    print("Conectando ao WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Wokwi-GUEST', '')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.1)
    print(" Conectado!")

def updateLed(temp):    
    temp += 40
    r = temp * 4
    g = 0
    b = 255 - temp * 4
    if temp == 60:
        g = 255
    elif temp > 60:
        g = 255 - ((temp * 4) - 255)
    else:
        g = temp * 4
    ledRgb[0] = (int(r), int(g), int(b))
    ledRgb.write() 

def main():
    connectWifi()
    print("Conectando ao servidor MQTT... ")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
    client.connect()
    print("Subscrevendo topico...", end="")
    client.set_callback(onReceive)
    client.subscribe(MQTT_TOPIC_RX)
    print("Subscrito!")

    prev_weather = ""
    while True:
        sensor.measure() 
        temperature = sensor.temperature()
        updateLed(temperature)
        
        message = ujson.dumps({
            "temperature": temperature,
            "humidity": int(sensor.humidity()),
            "switch_1": switch1.value() == 0, # Nivel logico LOW é considerado HIGH
            "switch_2": switch2.value() == 0, # pois os pinos de entrada estão
            "switch_3": switch3.value() == 0, # configurados para usar o resistor
            "switch_4": switch4.value() == 0, # interno como PULL_UP
            "switch_5": switch5.value() == 0,
            "switch_6": switch6.value() == 0,
            "switch_7": switch7.value() == 0,
            "switch_8": switch8.value() == 0,
            "relay_state": relayState,
            "pwm_led": pwmLed,
            "servoAngle": servoAngle
        })
        if message != prev_weather:
            print("Enviando novos valores {}".format(message))
            client.publish(MQTT_TOPIC_TX, message)
            prev_weather = message
        else:
            print("Nenhuma alteracao ocorrida nos valores dos sensores.")
        client.check_msg() # checa se há novas mensagens recebidas no topico
        time.sleep(1) # Menor que 1 pode fazer o servidor MQTT desconectar o cliente.

if __name__ == '__main__':
    main()
