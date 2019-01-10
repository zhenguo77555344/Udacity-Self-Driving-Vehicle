import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('Lesson5_4 Picture.jpg')
print("This image is: ", type(image), "with dimension:", image.shape)
print('image[0,0,0]) =', image[0, 0, 0])

ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)

red_threshold = 0
green_threshold = 0
blue_threshold = 0
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

thresholds = (image[:, :, 0] < rgb_threshold[0]) | (image[:, :, 1] < rgb_threshold[1]) | (image[:, :, 2] < rgb_threshold[2])


color_select[thresholds] = [0, 0, 0]

# Display the image
#plt.imshow(color_select)

plt.figure(1)
plt.imshow(image[:,:,2])

plt.figure(2)
plt.imshow(image[:, :,0])



plt.show()


print('Hello Udacity ！！！')

















