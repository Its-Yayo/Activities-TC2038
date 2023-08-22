#!/usr/bin/python3

#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# @date: 25-Aug-2023
# @authors:
#           A01754574 Luis Fernando De León Silva
#           A01746999 Luis Eduardo Landeros Hernandez
#----------------------------------------------------------

import sys
from PIL import *

def extract_hidden_images(input_file: str) -> None:
    """ Extracts hidden images from a file """
    try:
        img = open(input_file)
    except Exception as e:
        print("File not found:", e)
        sys.exit(1)

    if img.mode != 'RGB':
        print("Image is not RGB")
        sys.exit(1)
    
    if not input_file.lower().endsWith('.png'):
        print("Image is not PNG")
        sys.exit(1)
    
    width, height = img.size
    channels = img.split()
    



def main() -> None:
    pass

if __name__ == '__main__':
    main()
    sys.exit(1)

