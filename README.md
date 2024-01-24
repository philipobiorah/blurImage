# blurImage
Python module that blurs image
This utility is a simple, yet powerful Python script that applies a box blur effect to images. Leveraging the capabilities of the Pillow library, it offers an easy way to enhance your photos by blurring them with a specified intensity. Whether you're looking to soften backgrounds, create artistic effects, or simply experiment with your images, this tool provides a quick and effective solution.



- Loading the Image: before = Image.open('path_to_your_image.jpg') loads your original image into memory.
- Applying Edge Detection: after_edges = before.filter(ImageFilter.FIND_EDGES) applies the FIND_EDGES filter to the loaded image. This operation detects and highlights the edges throughout the image.
- Saving or Displaying the Image: The final image, which now contains just the edges of the original image, can be saved to a new file or displayed directly.