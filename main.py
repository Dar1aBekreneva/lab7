def q1():
    from PIL import Image

    pic = "gvozd.jpg"
    with Image.open(pic) as img:
        img.load()
    img.show()
    w, h = img.size
    f = img.format
    m = img.mode

    print("ширина: ", w)
    print("высота:  ", h)
    print("формат: ", f)
    print("цвет модель:", m)

def q2():
    from PIL import Image
    file = "gvozd.jpg"
    with Image.open(file) as img:
            img.load()

    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("newgvozd.jpg")

    c1_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    c1_img.save("top.jpg")
    c2_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    c2_img.save("netop.jpg")

    new_img.show()
    c1_img.show()
    c2_img.show()

def q3():
    from PIL import Image, ImageFilter
    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.FIND_EDGES)
            new_img.save("new_" + file)
            new_img.show()

def q4():
    from PIL import Image

    w = "watermark.png"
    with Image.open(w) as img_w:
        img_w.load()

    img_w = Image.open(w)
    img_w = img_w.resize((img_w.width // 2, img_w.height // 2))

    filename = "chto.jpg"
    with Image.open(filename) as img:
        img.load()

    img.paste(img_w, (150, 250), img_w)
    img.save("watermark_chto.jpg")
    img.show()

q1()