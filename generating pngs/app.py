from PIL import Image, ImageDraw, ImageFont
import os.path

# opening text and reading text file
with open('fortunes.txt') as f:
  text = f.read()
  
  # creating empty string and list
  fortunes = []
  newfortune = ""

  # replacing delimiter with '' and appending fortune to list 
  for char in text:
    if char == '%':
      char = ''

      if newfortune != "":
        fortunes.append(newfortune)
        newfortune = ""
      else:
        fortunes.append(newfortune)

    newfortune = newfortune + char


# setting imgage count
imgcount = 0

# iterating through fortunes
for text in fortunes:
  imgcount = imgcount + 1

  wordlist = []
  charcount = 0
  newstring = ""
  iteration = 0

  for char in text:
    # incrementing count of current charaters, loop count, and adding char to string
    charcount = charcount + 1
    iteration = iteration + 1
    newstring = newstring + char 

    # appening string to list if of charaters greater than 20 and equal to and empty space
    if charcount > 20 and char == ' ':
      wordlist.append(newstring)
      newstring = ""
      charcount = 0
    elif iteration == len(text):
      wordlist.append(newstring)
  
  # setting text position
  x = 40
  y = 600

  iteration = 0

  
  for words in wordlist:
    
    # checking if file exists
    if iteration != 0:
      fn = f'{imgcount}.png'
      img = Image.open('pngs/{}'.format(fn))
      d = ImageDraw.ImageDraw(img)

      # setting font
      fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
      d.text((x , y), words, font=fnt, fill=(255,255,255))

      # saving image
      img.save('pngs/{}'.format(fn))

      # moving down pixels if another sentences needs to be printed
      y = y + 75
    else:
      img = Image.open('testpng.png')
      d = ImageDraw.ImageDraw(img)

      # setting font
      fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
      d.text((x , y), words, font=fnt, fill=(255,255,255))

      # saving image
      fn = f'{imgcount}.png'
      img.save('pngs/{}'.format(fn))

      # moving down pixels if another sentences needs to be printed
      y = y + 75
      iteration = iteration + 1

    



