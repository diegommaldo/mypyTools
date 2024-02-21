
"""""""""""

Batch check image size consistency
by Diego Maldonado
http://www.diegomaldonado.com.br
https://github.com/diegommaldo

PIL module is needed
you can download PIL here:
https://pypi.org/project/Pillow/


"""""""""""

import PIL
import os
from PIL import Image

#------------------------#



## Adjust here ##

# Paste your path folder
pathFolder = "paste path here"


# Insert the image size you need to check in pixels
correctWidth = 200
correctHeight = 300




#------------------------#

# Let the code flow

print ("Checking Files...")
print ( )


for file in os.listdir(pathFolder):
	supportedFiles = ('.jpg', '.jpeg', '.png')
	
	if file.endswith(supportedFiles):
		filePath = pathFolder + file
		

		im = Image.open(filePath)
	  	
		
	w, h = im.size
	
	if im.size == (correctWidth, correctHeight):
		print(" 🟢 " + file)

	else:
		print(" 🔴 " + file)

		if w == correctWidth:
		
			print ("	🟢	width")
		else:
			print (" 	🔴	width is", w )

		if h == correctHeight:
			print ("	🟢	height")
		else:
			print ("	🔴	height is", h )





print (" ")
print ("Done")
