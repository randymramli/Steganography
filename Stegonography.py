import cv2
import numpy as np

def binaryConverter(message):
    if type(message) == str:
        return ''.join([format(ord(i), '08b') for i in message])
    elif type(message) == np.ndarray or type(message) == bytes:
        return [format(i, '08b') for i in message]
    elif type(message) == int:
        return format(message, "08b")
    else:
        raise TypeError("Input not supported")

def Encoder():
    pic_input = input("Please enter the image name with the extension: \n")
    pic_open = cv2.imread(pic_input)

    text = input("Please input the message you want to encrypt: \n")
    if len(text) == 0:
        return ValueError("Message is empty")
    
    image_copy = pic_open.copy()
    
    encodedImage = leastSigByte(image_copy, text)

    newimg = input("Enter the name of the new image with extension: ")
    cv2.imwrite(newimg, encodedImage)
    

def Decoder():
    pic_input = input("Please enter name of the image you want to decode with the extension: \n")
    pic_open = cv2.imread(pic_input)

    result = showText(pic_open)
    print(result)

def showText(image):
    BIT = 8
    binary_value = ""
    for values in image:
        for pixel in values:
            r,g,b = binaryConverter(pixel)
            binary_value += r[-1]
            binary_value += g[-1]
            binary_value += b[-1]
    
    separated_bytes = [binary_value[i: i+BIT] for i in range(0, len(binary_value), BIT)]


    text_result = ""

    for byte in separated_bytes:
        text_result += chr(int(byte,2))
        if text_result[-2:] == "##":
            break
    
    return text_result[:-2]

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