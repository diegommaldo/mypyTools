"""""""""""

Batch Resize Images
by Diego Maldonado and a lot of other forums posts

PIL module is needed
you can download PIL here:
https://pypi.org/project/Pillow/


"""""""""""

import PIL
import os
import os.path
import subprocess

from PIL import Image


dirname = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(dirname)

# Choose reducing factor – 1 is 100%
factor = 0.5

for file in os.listdir(f):
    supportedFiles = ('.jpg', '.jpeg', '.png', '.JPG')

    # Search for Images on folder
    if file.endswith(supportedFiles):
        f_img = f+"/"+file
        print("#")
        print(file)
        
        # Open Image    
        img = Image.open(f_img)

        # Check Image size
        srcW, srcH = img.size     
        print('original size', srcW, "×", srcH)
        
            
        # Calculate new size
        resW = round(srcW * factor) 
        resH = round(srcH * factor)
        newsize = resW, resH
        
        # Resize and save        
        newS = img.resize(
            newsize,
            resample = 1 # Anti-Alias
            )
        newS.save(f_img)
        print('resized to', resW, "×", resH)

    # Alert for script's not supported files
    
    else:
        print("#")
        print("!!! ", file, " !!!" )
        print("not supported file")

        if file.endswith(('.py')):
           continue


print()    
print('Done')