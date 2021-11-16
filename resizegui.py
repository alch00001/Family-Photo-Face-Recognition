from itertools import cycle
import tkinter as tk
import PIL
from PIL import Image, ImageTk
#from ImageTk import PhotoImage
import io
import os


images = []
for f in os.listdir("./pictures"):
    if f.endswith(".JPG"):
        images.append("./pictures/" + f)

class Imagewindow(tk.Tk):
    def __init__(self,images):
        tk.Tk.__init__(self)
        self.photos = cycle(
          photo_image(self,image) for image in images
        )
        self.displayCanvas = tk.Label(self)
        self.displayCanvas.pack()
        
    def photo_image(self, jpg_filename):
        basewidth = 400
        with io.open(jpg_filename, 'rb') as ifh:
            pil_image = Image.open(ifh)
            wpercent = (basewidth/float(pil_image.size[0]))
            hsize = int((float(pil_image.size[1])*float(wpercent)))
            pil_image = pil_image.resize((basewidth,hsize), Image.ANTIALIAS)
            return ImageTk.PhotoImage(pil_image)
    def slideShow(self):
        img = next(self.photos)
        self.displayCanvas.config(image=img)
     #print "updated"
    def makeButtons(self):
        prev_button = tk.Button(self, text="Previous", width=10, height=2, command=lambda: prev(panel))
#      next_button = tk.Button(self, text="Next", width=10, height=2, command=lambda: next(panel))
    def run(self):
        self.mainloop()


root = Imagewindow(images)
width = 400
height = 400
root.overrideredirect(True)
root.geometry('%dx%d' % (width*1, height*1))
root.slideShow()
root.run()

