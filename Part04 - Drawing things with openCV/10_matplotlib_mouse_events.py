import cv2
import numpy as np
import matplotlib.pyplot as plt
from Utils import constant_colors

# We create the canvas to draw: 400 x 400 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros():
image = np.zeros((400, 400, 3), dtype="uint8")

# If you want another background color you can do the following:
image[:] = constant_colors.LIGHT_GRAY


def update_img_with_matplotlib():
    """Updates an image using matplotlib capabilities"""

    # Convert BGR to RGB image format:
    img_RGB = image[:, :, ::-1]

    # Display the image:
    plt.imshow(img_RGB)

    # Redraw the Figure because the image has been updated:
    figure.canvas.draw()


# We define the event listener for the 'button_press_event':
def click_mouse_event(event):
    # (event.xdata, event.ydata) contain the float coordinates of the mouse click event:
    cv2.circle(image, (int(round(event.xdata)), int(round(event.ydata))), 30, constant_colors.BLUE, cv2.FILLED)
    # Call 'update_image()' method to update the Figure:
    update_img_with_matplotlib()


# We create the Figure:
figure = plt.figure()
figure.add_subplot(111)

# To show the image until a click is performed:
update_img_with_matplotlib()

# 'button_press_event' is a MouseEvent where a mouse botton is click (pressed)
# When this event happens the function 'click_mouse_event' is called:
figure.canvas.mpl_connect('button_press_event', click_mouse_event)

# Display the figure:
plt.show()
