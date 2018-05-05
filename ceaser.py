from sys import argv, exit
import string

def alphabet_position(letter):
    return string.ascii_lowercase.find(letter.lower())

def rotate_character(char, rot):
    if char.islower():
        char = chr(((alphabet_position(char) + rot) % 26) + ord('a'))
    elif char.isupper():
        char = chr(((alphabet_position(char) + rot) % 26) + ord('A'))
    return char

def encrypt(text,rot):
    new_pos = (rotate_character(i, rot)for i in text)
    return ''.join(new_pos)

'''
def user_input_is_valid(cl_args):
    return len(cl_args) == 2 and cl_args[1].isdigit()
def main():
    if user_input_is_valid(argv):
        text = input("Type a message:")
        print(encrypt(text, int(argv[1])))
if __name__ == '__main__':
    main()
    '''
