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

from PIL import Image

# Choose Folder Path
f = "file path"

for file in os.listdir(f):
    supportedFiles = ('.jpg', '.jpeg', '.png')

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
        
        # Reducing Factor
        factor = 0.25
        
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

print()    
print('Done')
