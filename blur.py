from PIL import Image, ImageFilter


before = Image.open("st_peter.jpeg")
after = before.filter(ImageFilter.BoxBlur(5))

after.save("out_st_peter.jpeg")