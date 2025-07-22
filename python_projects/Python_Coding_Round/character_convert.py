input_s = 'hello'

def convert_string(s):
    output_s = ''
    for i in input_s:
        output_s += chr(ord(i)-32)
    print(output_s)
convert_string(input_s)
