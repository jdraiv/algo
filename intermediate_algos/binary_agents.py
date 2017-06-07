#Return an English translated sentence of the passed binary string.
def binary_translator(zeros_and_ones):
    zeros_and_ones = zeros_and_ones.replace(" ","")
    words = []
    result = ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(zeros_and_ones)]*8))
    print(result)
    

binary_translator("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111")
binary_translator("01000010 01100101 00100000 01110100 01101000 01100001 01110100 00101110 00100000 01010011 01101111 00100000 01100010 01100101 00100000 01110100 01101000 01100101 00100000 01101111 01101110 01101100 01111001 00100000 01111001 01101111 01110101 00100000 01110100 01101000 01100001 01110100 00100111 01110011 00100000 01110100 01110010 01110101 01101100 01111001 00100000 01111001 01101111 01110101 00100000 01101111 01101110 00100000 01000101 01100001 01110010 01110100 01101000 00101110")

    