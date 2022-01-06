
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

# iterating through fortunes
for i in fortunes:
  print(i)
