import RPi.GPIO as GPIO


chan_list = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
GPIO.setmode(GPIO.BCM)

def num2dec(x):
    y = list(str(bin(x)))
    for i in range(len(y)):
        if y[i] == 'b':
            y = [0]*(8 - len(y[i + 1:])) + list(map(int, y[i + 1:]))
            return y
            break


def akinator(x):
    GPIO.output(chan_list, num2dec(x))
    print('{} = {}'.format(x, round(x/255 * 3.3, 2)))

GPIO.setup(chan_list, GPIO.OUT)
while True:
    x = input('Enter value(-1 to exit): ')
    try:
        x = int(x)
        if x < 0:
            GPIO.output(chan_list, [0 for _ in range(8)])
            GPIO.cleanup()
            break
        else:
            akinator(x)
    except:
        GPIO.output(chan_list, [0 for _ in range(8)])
        GPIO.cleanup()