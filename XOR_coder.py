import random
code = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890 !"#$%&’()*+,-./:;<>=?@[ ^_`{}| ~꿈꿉꿊꿋꿌꿍꿎꿏꿐꿑꿒꿓꿔꿕꿖꿗꿘꿙꿚꿛꿜꿝꿞꿟꿠꿡꿢꿣꿤꿥꿦꿧꿨꿩꿪꿫꿬꿭꿮꿯꿰꿱꿲꿳꿴꿵꿶꿷꿸꿹꿺꿻꿼꿽꿾꿿뀀뀁뀂뀃뀄뀅뀆뀇뀈뀉뀊뀋뀌뀍뀎뀏뀐뀑뀒뀓뀔뀕뀖뀗뀘뀙뀚뀛뀜뀝뀞뀟뀠뀡뀢뀣뀤뀥Ԉ'

def xor(i1,i2):
    return ['1' if int(i1[i]) + int(i2[i]) == 1 else '0' for i in range(0, len(i1))]

while True:
    block = '10'
    input_ = input()
    key = input()
    block_t = ""#блок, только длиной с текст
    block_k = ""
    inp_k = ""
    output = ""
    #всё с _k - зашированные копии
    if key == "":
        for i in range(len(input_)):
           key += code[random.randint(0,256)]
        
    c_inp = ""#закодированный инпут
    c_key = ""#акодированный ключ
    
    if len(key) < len(input_):
        len_test = len(input_) - len(key)
        for i in range(len_test):
            key += key[i]#приравнивание ключа к тексту
        print("")
        print('True key - ',key)
        print("")

    if len(key) > len(input_):
        len_test = len(key) - len(input_)
        key = key[:-(len_test)]
        print("")
        print('True key - ',key)
        print("")
            

    for i in range(len(input_)):
        c_inp += '0' * (8 - len((str(bin(code.find(input_[i]))[2::])))) + str(bin(code.find(input_[i]))[2::])#Как я это сделал?
        c_key += '0' * (8 - len((str(bin(code.find(key[i]))[2::])))) + str(bin(code.find(key[i]))[2::])#кодирование ключа и текста
        #сука боже. Честно. Я минуту танцевал после того как написал это.

    if len(block) < len(c_inp):
        len_test = len(c_inp) - len(block)
        for i in range(len_test):
            block += block[i]#приравнивание блока к тексту

    if len(block) > len(c_inp):
        len_test = len(block) - len(c_inp)
        block = block[:-(len_test)]
        #приравнивание блока к тексту
            

    block_k = xor(c_key, block)
    inp_k = xor(block_k, c_inp)
    for i in range(int(len(inp_k) / 8)):
        output += code[int(inp_k[i:i+8],base = 2)]
    print(output)
        
    print(code.find(output))


                

