#Done by Aiman Al Mahruqi
#Email : aiman.almahruqi@almahruqi.com
#Reference : https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

# Import libraries
# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import re


# Part #1 : Converting PDF to images

# Path of the pdf
PDF_file = "rihal.pdf"

# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, 500,first_page =2)

# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
for page in pages:
	# Declaring filename for each page of PDF as JPG
	filename = "page_"+str(image_counter)+".jpg"

	# Save the image of the page in system
	page.save(filename, 'JPEG')

	# Increment the counter to update filename
	image_counter = image_counter + 1

 # Variable to get count of total number of pages 
filelimit = image_counter-1

# Part #2 - Recognizing text from the images using OCR

for i in range(1, filelimit + 1):
	# Set filename to recognize text from
	filename = "page_"+str(i)+".jpg"
	# Recognize the text as string in image using pytesserct
	text = str(((pytesseract.image_to_string(Image.open(filename)))).encode("utf-8"))
	# The recognized text is stored in variable text
	text = text.replace('-\n', '')

# Part 3 : Find The Matches and Display The Result

#find all the matching
age = re.findall(r'([0-9]+.?[0-9]*) [y|Y]ears old', text) #age match
date = re.findall(r'([0-9]*/[0-9]*/[0-9]*)', text) #date match
cat = re.findall(r'name is ([A-za-z]+)', text) #cat name match
city = re.findall(r'from ([A-Z][a-z]+)', text) #city name match
serial = re.findall(r'([0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{3})', text) #serial match
#convert the list to string
ageF = '\n'.join(age)
dateF = '\n'.join(date)
cityF = '\n'.join(city)
serialF = '\n'.join(serial)
catF = '\n'.join(cat)
#print the string and format the output
print ("Dates:\n" +  dateF)
print ("\nSerial Numbers:\n" +  serialF.replace("-", " "))
print ("\nCities:\n" +  cityF)
print ("\nAges:\n" +  ageF)
print ("\nCat's Names:\n" +  catF )
