from CHIPHER import DEFAULT_ENCODER, CHARSET, CHARSET_LEN
class CaeserCipher:
    def __init__(self):
        print('Default Encoder Key is', DEFAULT_ENCODER, 'To change it pass it with methods, Dont forget the key')

    def encode(self, message, encoder = DEFAULT_ENCODER):
        return self._change(message, encoder, 1)

    def decode(self, encrypted_message, encoder = DEFAULT_ENCODER):
        return self._change(encrypted_message, encoder, -1)
    
    def _change(self, message, encoder, encode_or_decode):
        encoder *= encode_or_decode
        changed_message = []
        for x in message:
            changed_message.append(CHARSET[(CHARSET.index(x)+encoder)%CHARSET_LEN])
        return ''.join(changed_message)