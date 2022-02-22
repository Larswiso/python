inp_text = "Deine Mutter ist richtig fett"

chars = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
cryptochars = ":~.$C'B\dGX=if]r[IN41MkWaH@7T;?}F+ *bhUe^{Yx9`nOE<3JzK6P&%q2pLcw(gv8js_SZou>m-A#RlV/tD,0Q|)y5"

def enkrypter(text):
    result=[]
    for char in text:
        for i, j in enumerate(cryptochars):
            if j == char:
                crychar = chars[i]
                result.append(crychar)
    a = result
    result = "".join(a)
    print(result)

def krypter(text):
    result=[]
    for char in text:
        for i, j in enumerate(chars):
            if j == char:
                crychar = cryptochars[i]
                result.append(crychar)
    a = result
    result = "".join(a)
    print(result)
    return result

b = krypter(inp_text)
enkrypter(b)
