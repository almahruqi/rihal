# rihal
A Solution to Programming Challenge
# Introduction : 

The solution needs to do the following steps:
1.Input/Upload this PDF document
2.Use page 2 for the data.
3.OCR the page
4.Extract the following as outputs:
	a. Find all dates. Standardize the finding to this format MM/DD/YY
	b. All serial numbers
	i. Should be separated as 1 st value 2 nd value 3 rd value 4 ht value
	c. All cities
	d. All ages
	e. All cat names

# My Solution : 

1) Convert PDF to image using : 

pdf2image: https://github.com/Belval/pdf2image

2) Convert image to text using :

pytesseract: https://github.com/madmaze/pytesseract

3) Find The Matches and Display The Result

You need to install these packages before ruining the code : 

Note*:I used the following commands to install the packages on Ubuntu 18.
```bash
pip install pillow
pip install pytesseract
pip install pdf2image
pip install pathlib
sudo apt-get install tesseract-ocr tesseract-ocr
```
# To run the code :

1) First make sure the PDF file is named "rihal.pdf". Note* : You can edit the name of the file in code in line 17 (PDF_file).
2) Make sure the python file is in the same folder with the PDF file.
3) Type the following command in the terminal : 
	python main.py 

# The Output : 
```output
Dates:
28/12/2012
2/02/2019

Serial Numbers:
100 222 222 111
123 557 546 111
225 546 748 565
645 485 597 597
595 428 458 526
125 544 545 662

Cities:
Muscat
Bahla
Chicago

Ages:
7
5
8
6
9
2.5
4
9

Cat's Names:
Clowy
Sharen
```
