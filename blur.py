from PIL import Image, ImageFilter


before = Image.open("st_peter.jpeg")
after = before.filter(ImageFilter.BoxBlur(5))

after.save("out_st_peter.jpeg")


after_edges = before.filter(ImageFilter.FIND_EDGES)
after_edges.save("out_edges_st_peter.jpeg")