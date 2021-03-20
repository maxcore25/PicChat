from PIL import Image
from random import seed, randint


def encrypt(im_path, text):
    img = Image.open(im_path)
    pix = img.load()
    x, y = img.size
    res = Image.new('RGB', (x, y), (255, 255, 255))
    pixres = im_copy(im_path, res)
    ntext = text + chr(0)
    seed(123456789)
    pixs = []

    for ltr in ntext:
        cx, cy = randint(0, x-1), randint(0, y-1)
        while (cx, cy) in pixs:
            cx, cy = randint(0, x - 1), randint(0, y - 1)
        pixs.append((cx, cy))
        cur_char = ord(ltr) - 890 if ord(ltr) > 1000 else ord(ltr)
        cr, cg, cb = pix[cx, cy]
        cr, cg, cb = cr & 248, cg & 252, cb & 248
        pixres[cx, cy] = cr | ((cur_char & 224) >> 5),\
                         cg | ((cur_char & 24) >> 3),\
                         cb | (cur_char & 7)

    res.save('img_with_text.png')


def decrypt(dec_im_path):
    dec_img = Image.open(dec_im_path)
    pix = dec_img.load()
    x, y = dec_img.size
    seed(123456789)
    pixs = []
    text = ''

    while True:
        cx, cy = randint(0, x - 1), randint(0, y - 1)
        while (cx, cy) in pixs:
            cx, cy = randint(0, x - 1), randint(0, y - 1)
        pixs.append((cx, cy))

        r, g, b = pix[cx, cy]
        cur_char = ((r & 7) << 5) | ((g & 3) << 3) | (b & 7)
        if cur_char > 130:
            cur_char += 890

        if cur_char == 0:
            break

        text += chr(cur_char)

    return text


def im_copy(im_path, res):
    img = Image.open(im_path)
    pix = img.load()
    x, y = img.size
    pixres = res.load()
    for i in range(x):
        for j in range(y):
            pixres[i, j] = pix[i, j]
    return pixres


encrypt('koti.jpg', 'Даня')
t = decrypt('img_with_text.png')
print(t)
