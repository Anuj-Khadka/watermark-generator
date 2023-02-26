from PIL import ImageDraw, Image, ImageFont
from pathlib import Path
import os

folder_path = Path('C-Programming')

for i in range(1, 33):
    if i<10:
        file_path = folder_path / f'C-Programming (1)-0{i}'
    else:   
        file_path = folder_path / f'C-Programming (1)-{i}'


    img = Image.open(f'{file_path}.png').convert('RGBA')
    font_face = "arial.ttf"
    font_size = 100
    color = (0,0,0, 25)

    txt = "@theclassnote"
    coordinates = [(img.size[0]/2)- (img.size[0]/6), (img.size[1])/2]
    trans_txt = Image.new('RGBA', img.size, (255,255,255,0))

    print(img.size)

    # fnt = ImageFont.load_default()
    canvas = ImageDraw.Draw(trans_txt)
    fnt =ImageFont.truetype(font_face, font_size)

    canvas.text((coordinates[0], coordinates[1]), text=txt, font=fnt, fill=color, )
    trans_txt = trans_txt.rotate(20)
    combined = Image.alpha_composite(img, trans_txt)  
    from pathlib import Path


    new_folder = Path("generated")

    if os.path.exists(new_folder):
        combined.save(f'./generated/Page-{i}.png')
    else:
        os.mkdir(new_folder)
        combined.save(f'./generated/Page-{i}.png')
    
