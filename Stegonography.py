import cv2
import numpy as np

def binaryConverter(message):
    if type(message) == str:
        return ''.join([format(ord(i), '08b') for i in message])
    elif type(message) == np.ndarray or type(message) == bytes:
        return [format(i, '08b') for i in message]
    elif type(message) == int:
        return format(message, "08b")

def Encoder():
    pic_input = input("Please enter the image name with the extension: \n")
    pic_open = cv2.imread(pic_input)
    print(type(pic_open))


    text = input("Please input the message you want to encrypt: \n")
    if len(text) == 0:
        return ValueError("Message is empty")
    
    image_copy = pic_open.copy()
    
    encodedImage = leastSigByte(image_copy, text)

    newimg = input("Enter the name of the new image with extension: ")
    cv2.imwrite(newimg, encodedImage)
    

def Decoder():
    pass

def leastSigByte(image,message):
    
    max_bytes = image.shape[0] * image.shape[1] * 3 //8

    if len(message) > max_bytes:
        raise ValueError("The Message is too big for the picture")

    
    message += "##"
    
    message_binary = binaryConverter(message)

    message_len = len(message_binary)

    index = 0

    for data in image:
        for pixel in data:
            r,g,b = binaryConverter(pixel)
            if index < message_len:
                pixel[0] = int(r[:-1] + message_binary[index], 2)
                index += 1
            if index < message_len:
                pixel[1] = int(g[:-1] + message_binary[index], 2)
                index += 1
            if index < message_len:
                pixel[2] = int(b[:-1] + message_binary[index], 2)
                index += 1
            if index >= message_len:
                break
    return image


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