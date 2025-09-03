

#Definição das variáveis

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

#Operações

for char in text.lower():
    if char == ' ':
        encrypted_text += char 
    else:
        index = alphabet.find(char)
        new_index = index + shift
        encrypted_text += char + alphabet[new_index] 
    print('char:', char, 'encrypted text:', encrypted_text)
    