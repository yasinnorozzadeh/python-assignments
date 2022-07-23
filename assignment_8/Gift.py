import os
import imageio

myfiles = os.listdir("img")

images = []
for i in range(len(myfiles)):
    image = imageio.imread("img/" + myfiles[i])
    images.append(image)

imageio.mimsave("panda9.gif" , images)
