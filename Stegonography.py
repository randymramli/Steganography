import numpy as np
import PIL as pic

def Encoder():
    image = input("Please enter the image name with the extension: \n")
    img = pic.open(image, 'r')
    img.show()


    text = input("Please input the message you want to encrypt: \n")
    if len(text) == 0:
        return ValueError("Message is empty")
    
    encodedImage = pixelManipulate(img, text)

def Decoder():
    pass

def pixelManipulate(image,message):
    
    img_Size = len(image.fp.read())

    if len(message) > img_Size:
        raise ValueError("The Message is too big for the picture")
    
    message_binary = binaryConverter(message)

    message_len = len(message_binary)

def binaryConverter(message):
    if type(message) == str:
        return ''.join([format(ord(i), '08b') for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format (i, '08b') for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, '08b')

def main():
    print("Welcome to Stegonoraphy App")
    goal = int(input("What Would you like to do?\n"
                "1.Encoding\n2.Decoding\n\n"))
    
    if goal == 1:
        Encoder()
    elif goal == 2:
        Decoder()
    else:
        goal = int(input("Please Input The Right Option\n"
                "1.Encoding\n2.Decoding\n"))

if __name__ == '__main__':
    main()