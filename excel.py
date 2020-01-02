# Program extracting all columns 
# name in Python 
import urllib.request
import random
import xlrd 
  
loc = ("C:/Users/gshp/Desktop/imagenes/imagenes.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 
count = 0

for i in range(sheet.nrows):
	if( (sheet.cell_value(i, 12)) == 'TOUCH POINT - EXHIBICIONES'):		
		full_file_name = str(sheet.cell_value(i, 0)) + '_' + str(sheet.cell_value(i, 3)) + '_' + str(count) + '.png'
		image_url = str( sheet.cell_value(i, 15) )
		urllib.request.urlretrieve(image_url,full_file_name)
		count += 1	    	
	#else:
	#	print(sheet.cell_value(i, 15)) 
	#	print(sheet.cell_value(i, 0))
	#	print(sheet.cell_value(i, 3))