

#Definição das variáveis

text = 'Hello Zaira'
shift = 3

def cesar(message , offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Adicione espaço a mensagem
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print( 'encrypted text:', encrypted_text)

cesar(text, shift)
cesar(text, 13)
 