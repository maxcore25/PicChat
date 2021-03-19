from PIL import Image
from random import seed, randint


def encrypt(im_path, text):
    img = Image.open(im_path)
    pix = img.load()
    x, y = img.size
    text_size = len(text) + 1
    ntext = text + '0'
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixres = res.load()
    seed(123456789)
    pixs = []
    for ltr in text:
        cx, cy = randint(0, x-1), randint(0, y-1)
        while (cx, cy) in pixs:
            cx, cy = randint(0, x - 1), randint(0, y - 1)
        pixs.append((cx, cy))
        bchar = f'{ord(ltr) - 890 if ord(ltr) > 1000 else ord(ltr):b}'
        if len(bchar) < 8:
            bchar = '0' * (8-len(bchar)) + bchar
        cur_color = pix[cx, cy]
        new_color =
    # for i in range(x):
    #     for j in range(y):
    #         r, g, b = pix[i, j]
    #         factor = (r + g + b) // 3
    #         if factor >= 128:
    #             pixres[i, j] = 255, 255, 255
    #         else:
    #             pixres[i, j] = 0, 0, 0
    # res.save('img_with_text.jpg')
