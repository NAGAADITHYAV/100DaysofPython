from caeser_cipher import CaeserCipher

cc = CaeserCipher()
message = input("Enter Your message: ")
encoder = input('Enter your encoder(Leave Blank for default Encoder):')
if encoder != '':
    encoder = int(encoder)
    encrypted_message = cc.encode(message, encoder)
    print(encrypted_message)
    message = cc.decode(encrypted_message, encoder)
    print(message)
else:
    encrypted_message = cc.encode(message)
    print(encrypted_message)
    message = cc.decode(encrypted_message)
    print(message)
