from PIL import Image, ImageDraw
import random


def clr(num):
    if num == 1:
        return (random.randint(150, 255), 0, 0)
    elif num == 2:
        return (0, random.randint(150, 255), 0)
    elif num == 3:
        return (0, 0, random.randint(150, 255))


def clr2(num):
    ret = num % 766
    x0 = 0
    x1 = 0
    x2 = 0
    if ret < 256:
        x0 = ret
    elif ret < 511:
        x0 = 255
        x1 = ret - 255
    else:
        x0 = 255
        x1 = 255
        x2 = ret - 510
    if x0 < 30:
        x0 = 30
    elif x1 < 30:
        x1 = 30
    elif x2 < 30:
        x2 = 30
    return (x2, x1, x0)

size = 1000
line = 10

img = Image.new('RGBA', (size, size), color=(0, 0, 0))
tmp = ImageDraw.Draw(img)

end = size / 10
it = 0
for i in range(0, int(end)):
    for j in range(0, int(end)):
        c0 = clr(random.randint(1, 3))
        c1 = clr2(it)
        it += 1
        x0 = (j * line, i * line)
        y0 = (x0[0] + line, x0[1] + line)
        x1 = (j * line + line, i * line)
        y1 = (x0[0], x0[1] + line)
        tab = [tmp.line(random.choice([(x0, y0), (x1, y1)]), fill=random.choice([c0, c1]), width=random.randint(1, 1)), tmp.line(random.choice([(x0, x1), (x0, y1)]),
               fill=random.choice([c0, c1]), width=random.randint(1, 1))]
        random.choice(tab)
img.save('out.png')
