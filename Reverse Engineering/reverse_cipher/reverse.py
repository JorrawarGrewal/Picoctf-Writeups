import string
string = 'picoCTF{w1{1wq85jc=2i0<}'
flag = 'picoCTF{'

j = 8
for j in range(8,24):
    if (j&1) == 0:
        flag+= chr(ord(string[j])-0x5)
        print('1')
    else:
        flag += chr(ord(string[j])+2)
        print('2')
flag += "}"

print(flag)

 


