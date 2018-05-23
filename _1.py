


source = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "



length =len(source)

lst =list(source)
for i in range(length):
    if ord(lst[i])>ord('z') or ord(lst[i])<ord('a'):
        continue
    elif (ord(lst[i])+2>ord('z')):
        lst[i]=chr(ord(lst[i])+2-26)
    else:
        lst[i]=chr(ord(lst[i])+2)




print("".join(lst))

#it recommend you use the method string.maketrans()

string1 ='map'

x='abcdefghijklmnopqrstuvwxyz'
y='cdefghijklmnopqrstuvwxyzab'

trans=str.maketrans(x,y)


print(string1.translate(trans))
print(source.translate(trans))

