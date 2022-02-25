from PIL import Image, ImageDraw, ImageFont
from random import choice, randint
import string

from colored import fg, attr

# COLORS #
red = fg('red')
blue = fg('blue')
yellow = fg('yellow_1')
green = fg('green')
# RESET COLOR #
reset = attr('reset')


def randStr (chars = string.ascii_letters , N=4):
        return ''.join(choice(chars) for _ in range(N))

def captcha_image():
    width = 480
    height = 240

    font = ImageFont.truetype("arial.ttf", size=142)

    img = Image.new('RGB', (width, height), color=
    (randint(0,255),
    randint(0,255),
    randint(0,255)))

    imgDraw = ImageDraw.Draw(img)

    textWidth, textHeight = imgDraw.textsize(captcha_text, font=font)
    xText = (width - textWidth) / 2
    yText = (height - textHeight) / 2

    imgDraw.text((xText, yText), captcha_text, font=font, fill=
    (randint(0,255),
    randint(0,255),
    randint(0,255)))

    img.save('CAPTCHA.jpg')

print()

for x in range (3):
    captcha_text = randStr()
    captcha_image()

    captcha_input = input('Insert Captcha : ')


    if captcha_input == captcha_text :
        print( green + 'Correct!' )
        print( reset )
        break

    else:
        if x == 0:
            print( red + 'Incorrect, retry!')
            print( reset )
        elif x == 1:
            print( red + 'Incorrect, retry! \n')
            print( yellow + 'LAST TRY.' + reset )
        elif x == 2:
            print( red + 'Incorrect, quitting.')
            print( reset )
