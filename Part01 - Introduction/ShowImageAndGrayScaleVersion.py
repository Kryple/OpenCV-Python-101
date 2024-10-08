import cv2
import numpy as np
def load_image(path):
    # cv2.imread(): read an image.
    # The image should be in the working directory or a full path of image should be provided.
    # load OpenCV logo image: 
    return cv2.imread(path)


def show_image(image):
    # cv2.imshow(): show an image in a window.
    # The window automatically fits to the image size.
    # First argument: window name.
    # Second argument: image to be displayed.
    # Each created window should have different window names.
    cv2.imshow("image", image)

    # cv2.waitKey() is a keyboard binding function.
    # Argument: time in milliseconds.
    # The function waits for specified milliseconds for any keyboard event.
    # If any key is pressed in that time, the program continues.
    # If 0 is passed, it waits indefinitely for a key stroke.
    # Wait indefinitely for a key stroke (in order to see the created window):
    cv2.waitKey(0)

    # To destroy all the windows we created
    cv2.destroyAllWindows()

def write_image_to_disk(path, image):
    """this function writes to disk an image given the image to be written"""
    cv2.imwrite(path, image)
    
def show_gray_scale_version(image):
    # Use cv2.cvtColor() to convert an image from one color format to another
    # In this case we use cv2.cvtColor() to convert the loaded image to grayscale (BGR to GRAY):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray scale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_binary_version(image): 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Display the binary image
    cv2.imshow('Binary Image', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image = load_image("../images/wukong.jpg")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # binary_image = cv2.bitwise_and(image, image, mask=gray_image)
    binary_image = gray_image > 0.6
    
    
    # image = cv2.resize(image, (400, 300))
    
    show_image(image)
    show_gray_scale_version(image)
    show_binary_version(image)
    
    
    # binary_matrix = binary_image.astype(np.uint8)
    # np.set_printoptions(threshold=np.inf)
    # print(binary_matrix)
    
    # write_image_to_disk("../images/gray_wukong.jpg", image)
