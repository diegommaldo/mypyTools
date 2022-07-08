""""
Convert image to Grayscale
by Diego Maldonado and a lot of forum posts

You will need to install PIL module
	pip install Pillow

https://github.com/diegommaldo/mypyTools

"""


from PIL import Image
from pathlib import Path
import os


#select file in Folder
filePath = "In Path"

#select file out folder
outFolder = "Out Path"



## - auto - ##

# explit file name and extension
fileName, ext = os.path.splitext(filePath)
pureName = Path(filePath).stem

# Add _BW to the converted file name
outFile = pureName + "_BW" + ext

# Convert and save with new name
img = Image.open(filePath)
img.convert("L").save(outFolder + "/" + outFile)

print(pureName + " -> converted!")
print("Done")
