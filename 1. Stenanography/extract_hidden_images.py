#!/usr/bin/python3

# Lab #1: Steganography
# Image processing through bit manipulation.
#
# @date: 25-Aug-2023
# @authors:
#           A01754574 Luis Fernando De León Silva
#           A01746999 Luis Eduardo Landeros Hernandez
#
# Repo: https://github.com/Its-Yayo/Activities-TC2038
# Code under free license.
# ----------------------------------------------------------

import sys
from PIL import Image
from os import path


def extract_hidden_images(input_file: str) -> None:
    # 3 exceptions will be raised if the input arg has an error
    try:
        img = Image.open(input_file)
    except Exception as e:
        print("File not found:", e)
        sys.exit(1)

    if img.mode != 'RGB':
        print("Image is not RGB")
        sys.exit(1)

    if not input_file.lower().endswith('.png'):
        print("Image is not PNG")
        sys.exit(1)

    # Each channel (R, G, B) will obtain the less significant bit inside the hidden image.
    channels = img.split()

    for i, channel in enumerate(channels):
        width, height = channel.size

        channel_name = ["red", "green", "blue"][i]
        base_path, _ = path.splitext(input_file)
        output_file = f"{base_path}_channel_{i + 1}_{channel_name}.png"

        hidden = Image.new('1', (width, height))

        pixin = channel.load()
        pixout = hidden.load()

        for y in range(0, height):
            for x in range(0, width):
                pixout[x, y] = pixin[x, y] & 1

        hidden.save(output_file)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 extract_hidden_images.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    extract_hidden_images(input_file)


if __name__ == '__main__':
    main()
    sys.exit(1)
