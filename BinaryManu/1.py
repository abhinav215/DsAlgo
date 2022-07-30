

def binToDeci(binary_num):
  # binary_num = input('Enter a binary string:')
  dec_num = int(binary_num, 2)
  return dec_num



def deciToBin( dec_num):
  # dec_num = int(input('Enter a decimal number:'))
  binary_num= bin(dec_num).replace('0b', '')
  return binary_num


b = deciToBin(9)
print(b)
print(type(b))


ele = 122
xInB = '{:032b}'.format(ele)
print("xInB=",xInB)