from PIL import Image
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
images = []
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.png'):
            URL = str(root) + "\\" + str(file)
            images.append(URL)
hsize = min(5, len(images))
vsize = (len(images)/5) + 1

vspace = 2
hspace = 2

(h, w) = Image.open(images[0]).size
gavno = int((vsize*(w+vspace)))
im = Image.new('RGB', ((hsize*(h+hspace)), gavno))

for i, filename in enumerate(images):
    imin = Image.open(filename).convert('RGB')
    xpos = i % hsize
    ypos = i / hsize
    ypos = int(ypos)
    im.paste(imin, (xpos*(h+hspace), ypos*(w+vspace)))
print('Готово!')
im.save('output.tiff')
