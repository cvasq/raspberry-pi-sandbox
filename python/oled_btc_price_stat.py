#!/usr/bin/env python3

# Copyright (c) 2017 Adafruit Industries
# Authors: Tony DiCola, James DeVito, Carlos Vasquez
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Description: BTC price status script for usage with the Adafruit PiOLED (128x32)
 
import time
import subprocess
 
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import requests, json
 
 
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
 
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
 
# Clear display.
disp.fill(0)
disp.show()
 
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
 
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
 
# Load default font.
font = ImageFont.load_default()
 
while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    price_api_url = "https://api.gemini.com/v1"
    response = requests.get(price_api_url + "/pubticker/btcusd")
    btc_price_data = response.json()
 
    formatted_price = "1 BTC: ${:,.2f}".format(float(btc_price_data['last']))
    print("Updating price...")
 
    draw.text((x, top+25), formatted_price, font=font, fill=255)
 
    # Display image.
    disp.image(image)
    disp.show()
    
    # Delay loop to run every 15 seconds
    time.sleep(15)
