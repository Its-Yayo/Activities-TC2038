#!/usr/bin/python3

#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# @date: 15-Aug-2023
# @authors:
#           A01754574 Luis Fernando De León Silvas
#----------------------------------------------------------

from PIL import Image

INPUT_FILE_NAME = 'scarlett.png'
OUTPUT_FILE_NAME = 'gray.png'

def process_image() -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load()
        width, height = input_file.size
    output_image = Image.new('RGB', (width, height))

    pixout = output_image.load()

    for y in range(0, height):
        for x in range(0, width):
            r, g, b = pixin[x, y]
            avg = (r + g + b) // 3
            pixout[x, y] = (avg, avg, avg)

    output_image.save(OUTPUT_FILE_NAME)

if __name__ == '__main__':
    process_image()