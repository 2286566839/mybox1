word=input('请输入字母串')
a=int(input('请输入偏移量'))
for b in word:
    if'a'<= b <='z':
        print(chr(ord('a')+(ord(b)-ord('a')-a)%26),end="")
    elif'A'<= b <='Z':
        print(chr(ord('A')+(ord(b)-ord('A')-a)%26),end="")
    else:
        print('字母串都不知道是啥么？？？')