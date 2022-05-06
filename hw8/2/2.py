from PIL import Image, ImageDraw, ImageFont


img = Image.new('RGBA', (200, 200), 'white')
idraw = ImageDraw.Draw(img)
idraw.line((40, 95, 130, 95), fill='pink',width=14)
# idraw.rectangle((40, 40, 110, 110), outline='yellow', width=5)

text = 'Your Code'
idraw.text((40, 105), text, fill='black')

img.save('your_code.png')
