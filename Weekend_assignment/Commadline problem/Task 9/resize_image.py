''' 9. Read a binary file (e.g., an image or audio file) in Python and perform an operation, such as resizing an image or modifying audio data. '''
from PIL import Image

# Open the image file
with Image.open('Task 9/hd') as img:
    # Define the new size (width, height)
    new_size = (300, 200)

    # Resize the image
    resized_img = img.resize(new_size)

    # Save the resized image
    resized_img.save('output_image.jpg')

print('Image resized and saved as output_image.jpg')
