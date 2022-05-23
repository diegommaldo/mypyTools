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
f = "Path Here"

for file in os.listdir(f):

    # Search for Images on folder
    if file.endswith(('.jpg', '.jpeg', '.png')):
        f_img = f+"/"+file
        print("#")
        print(file)
        
        # Open Image    
        img = Image.open(f_img)

        # Check Image size
        srcW, srcH = img.size     
        print('original size', srcW, "×", srcH)
        
        # Reducing Factor
        factor = 0.5
        
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

print()    
print('Done')