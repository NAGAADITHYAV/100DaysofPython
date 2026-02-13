from CHIPHER import DEFAULT_ENCODER, CHARSET, CHARSET_LEN
class CaeserCipher:
    def __init__(self):
        print('Default Encoder Key is', DEFAULT_ENCODER, 'To change it pass it with methods, Dont forget the key')

    def encode(self, message, encoder = DEFAULT_ENCODER):
        encrypted_message = []
        for x in message:
            encrypted_message.append(CHARSET[(CHARSET.index(x)+encoder)%51])
        return ''.join(encrypted_message)

    def decode(self, encrypted_message, encoder = DEFAULT_ENCODER):
        message = []
        for x in encrypted_message:
            message.append(CHARSET[(CHARSET.index(x)-encoder)%51])
        return ''.join(message)