import random
import string
from captcha.image import ImageCaptcha
import PIL.Image
import IPython.display as display

def generate_Captcha() :

    # Generate random string
    random_string = string.digits + string.ascii_lowercase
    captcha_text = ''.join( random.choice(random_string) for _ in range(5) )

    # Genrate Captcha from text
    image = ImageCaptcha(width = 400, height=200 )
    image.generate(captcha_text)

    # Save Captcha image and diaplay it
    image.write(captcha_text,"captcha.png")
    img = PIL.Image.open("captcha.png")
    display.display(img)
    return captcha_text

def verify_Captcha() :
    flag = False

    while(flag != True) :
        captcha_text = generate_Captcha()
        # print(captcha_text)
        user_input = input("Enter CAPTCHA Text \n")
        if( user_input == captcha_text ) :
            print("\nCaptcha Verified Sucessfully ")
            flag = True
        else :
            print("\nInvalid Captcha Entry!!!!!!!!!!!!!!!!!! ")

verify_Captcha()

    