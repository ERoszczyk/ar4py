import time
from machine import Pin, I2C, ADC
import ssd1306
from time import sleep
import network
import urequests
"""
First i create display
"""
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
adc = ADC(0)

time.sleep(0.000001)

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text("switching on", 0, 10)
oled.show()
time.sleep(1.5)


def do_connect():
    oled.fill(0)
    oled.show()
    time.sleep(0.25)
    oled.text("connecting", 0, 10)
    oled.show()
    sta_if = network.WLAN(network.STA_IF); 
    sta_if.active(True)
    print(sta_if.scan())
    sta_if.connect("wififree", "test1234")
    while not sta_if.isconnected():                         
        pass
    oled.fill(0)
    oled.show()
    time.sleep(0.25)
    oled.text("connected", 0, 10)
    oled.show()

def make_request():
    oled.fill(0)
    oled.show()
    time.sleep(0.1)
    oled.text("requesting", 10, 0)
    oled.show()
    response = urequests.get('https://ar4py.herokuapp.com/api/appointments/next/')
    print(type(response))
    print(response)
    data = response.json()
    data = data['msg']
    oled.fill(0)
    oled.show()
    time.sleep(0.1)
    oled.text("request succesful", 10, 0)
    oled.show()
    time.sleep(0.75)
    return data

def draw_input(message, adc_read):
    if len(message) > 13:
        message = message.split()
        first_line = str(message[0] + " " + message[1])
        second_line = str(message[2])
        oled.fill(0)
        oled.show()
        time.sleep(0.01)
        oled.text(adc_read, 0, 0)
        oled.text(first_line, 0, 10)
        oled.text(second_line, 0, 20)
        oled.show()




do_connect()
message = make_request()
draw_input


while True:

    adc_value = adc.read()
    adc_value_show = str(adc_value)
    # oled.text(adc_value_show, 0, 0)
    # oled.text(str(data[current_user]), 0, 10)
    draw_input(message, str(adc_value))
    oled.show()
    print(adc_value)
    time.sleep(2)
    oled.fill(0)
    oled.show()
    time.sleep(0.001)

    if adc_value > 800:
        # current_user = current_user + 1
        oled.text("next", 30, 0)
        oled.show()
        time.sleep(2)
        oled.fill(0)
        oled.show()
        time.sleep(0.25)
        while(adc_value > 800):
            adc_value = adc.read()
            adc_value_show = str(adc_value)
            oled.text(adc_value_show, 0, 0)
            oled.text("turn back", 30, 0)
            oled.show()
            time.sleep(0.5)
            oled.fill(0)
            oled.show()
            time.sleep(0.05)
        time.sleep(0.1)
        message = make_request()
        draw_input(message, str(adc_value))



    # elif adc_value < 100:
    #     # current_user = current_user - 1
    #     oled.text("previous", 12, 0)
    #     time.sleep(1)
    #     while(adc_value < 800):
    #         adc_value = adc.read()
    #         oled.text("turn back", 12, 0)
    #         oled.show()
    #         time.sleep(0.25)
    #     oled.fill(0)
    #     time.sleep(0.1)



# time.sleep(0.5)


# do_connect()

# time.sleep(2)

# message = make_request()
# print(message)
# draw_input(message)






