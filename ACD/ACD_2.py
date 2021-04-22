import RPi.GPIO as GPIO
import time


chan_list = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
GPIO.setmode(GPIO.BCM)


GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)

def num2dec(x):
    y = list(str(bin(x)))
    for i in range(len(y)):
        if y[i] == 'b':
            y = [0]*(8 - len(y[i + 1:])) + list(map(int, y[i + 1:]))
            return y



GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
while True:
    time.sleep(0.5)
    for i in range(255):
        GPIO.output(chan_list, num2dec(i))
        y_1 = GPIO.input(4)
        GPIO.output(chan_list, num2dec(i + 1))
        y_2 = GPIO.input(4)
        if y_1 != y_2:
            print(i)
            break

