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


def bin_search():
    left = 2
    right = 253
    while True:
        print(str(left) + '--' + str(right))
        mid = (left + right) // 2

        GPIO.output(chan_list, num2dec(left))
        time.sleep(0.1)

        y_left = GPIO.input(4)
        time.sleep(0.1)

        GPIO.output(chan_list, num2dec(right))
        time.sleep(0.1)

        y_right = GPIO.input(4)
        time.sleep(0.1)

        GPIO.output(chan_list, num2dec(mid))
        time.sleep(0.1)

        y_mid = GPIO.input(4)
        time.sleep(0.1)

        if abs(right - left) <= 4:
            return left

        if y_mid == 0:
            if y_left == 0:
                right = mid
            else:
                left = mid
        else:
            left = mid



 
GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

while True:
    s = time.time()
    res = bin_search()
    f = time.time()
    print('Val = {}'.format(round(res/255 * 3.3, 2)))
    print('Time = {}'.format(f - s))

