
# Step 7
text = 'Hello World'
print(len(text))

# Step 5
text = 'Hello World'
print(text[6])

# Step 5
text = 'Hello World'
print(text[-1])

#Step 8
text = 'Hello World'
print(type(text))

#Step 15
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index) # traz a posição 7
shifted = alphabet[index + shift]
print(shifted) # traz a letra 