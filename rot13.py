
# String -> String
# Encrypt the given string with the ROT13 cipher


char_lookup = {}
for nn in range(26):
    char_up = chr(ord('A') + nn)
    char_low = chr(ord('a') + nn)
    if nn < 13:
        char_lookup[char_up] = chr(ord(char_up) + 13)
        char_lookup[char_low] = chr(ord(char_low) + 13)
    else:
        char_lookup[char_up] = chr(ord(char_up) - 13)
        char_lookup[char_low] = chr(ord(char_low) - 13)


def rot13(string):
    cipher = ''
    for char in string:
        # if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
        # char in "abcd..."
        if ord(char) in range(ord('A'), ord('Z')+1) or\
           ord(char) in range(ord('a'), ord('z')+1):
            cipher += char_lookup[char]
        else:
            cipher += char

    return cipher

            
            
