# coding: utf8

# 生成图片验证码

# 首先需要生成一个带有随机字符的图片

from PIL import Image, ImageDraw, ImageFont
import random
import string

size = (120, 30)
bg_color = (255, 255, 255)


def generate_image(mode="RGB"):
    """
    图片需要有图片大小,背景
    """
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)
    text = get_chars()
    font = ImageFont.truetype(text)
    width, length = font.getsize()
    draw.text(((size[0]-width), (size[1]-length)), text, font=font)
    return img


def get_chars():
    return "".join(random.sample(string.ascii_letters + string.digits, 8))

# 对图片处理处理,


generate_image()
