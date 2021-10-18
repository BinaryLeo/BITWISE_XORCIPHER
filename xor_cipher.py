import header_str
header=''
header_str.title(header)

cp_data = input('Insira o texto a ser criptografado: ')
cp_key = ((input('Insira a chave criptográfica: ')))

def table():
    print("+---------------+----------------+")
    print(" | Tabela verdade XOR  | Resultado |")
    print(" A = 0, B = 0 | A XOR B = 0 | ")
    print(" A = 0, B = 1 | A XOR B = 1 | ")
    print(" A = 1, B = 0 | A XOR B = 1 | ")
    print(" A = 1, B = 1 | A XOR B = 0 | ")

def cipher():
    st_f = "-" *100
    unicode_f = ('\u2193' * 8) + '   '
    cipher_operat =  len(cp_key) -  len(cp_data) #Pega diferença Data/Key e valida chaves
    cipher_operat_ad =  len(cp_data) -len(cp_key) #Pega diferença Key/Data e valida chaves
    nkey_cp = cp_key[cipher_operat:] 
    n_key = cp_key + (cipher_operat_ad * str(int(cp_key[-1:])))

    #Gera Lista c/ representaç.tabela ASCII
    lst_data_main=[ord(ch) for ch in cp_data]
    cipher_key = [ord(vl) for vl in cp_key]
    cipher_key_rm = [ord(vl) for vl in nkey_cp] 
    cipher_key_ad = [ord(vl) for vl in n_key] 
    #Gera Lista c/ representaç.em binário
    conv_op = [bin((ch))[2:].zfill(8) for ch in lst_data_main ] 
    key_convert = [bin((ch))[2:].zfill(8) for ch in cipher_key ]
    key_convert_rm = [bin((ch))[2:].zfill(8) for ch in cipher_key_rm]
    key_convert_ad = [bin((ch))[2:].zfill(8) for ch in cipher_key_ad ]
    # Passa dados listados em ASCII pela porta XOR e exibe representaç. binária
    xor =list(a^b for a,b in zip(lst_data_main,cipher_key))
    xor_dt_rm =list(a^b for a,b in zip(lst_data_main,cipher_key_rm))
    xor_dt_ad =list(a^b for a,b in zip(lst_data_main,cipher_key_ad)) 
    data_done = [bin((ch))[2:].zfill(8) for ch in xor ] 
    data_done_rm = [bin((ch))[2:].zfill(8) for ch in xor_dt_rm] 
    data_done_ad = [bin((ch))[2:].zfill(8) for ch in xor_dt_ad ] 
    

    if cipher_operat == 0:# Se não houver dif. entre string e key
        print ('Chave criptográfica ok')
        print(st_f)
        print("Valores da tabela ASCII para:", cp_data, "são:", lst_data_main, ".")
        print("Valores da tabela ASCII para:", cp_key, "são:", cipher_key, ".")
        print(st_f)
        print("Agora vamos converter os valores em binário.")
        print(st_f)
        print('Ref binária para: {} >>>>>>>>>>>'.format(cp_data),conv_op) 
        print('Ref binária para: {} >>>>>>>>>>>'.format(cp_key),key_convert) 
        print('Operação bit a bit na porta XOR ...', " ".join([unicode_f]*len(cp_data)))
        print('Dados criptografados >>>>>>>>>>>>',data_done)
        print(st_f)
    elif cipher_operat > 0: # Se key for maior remove chars
     print('Chave criptografica excede limite')
     print('A nova chave criptografica é : {}'.format(nkey_cp))

     print(st_f)
     print("Valores da tabela ASCII para:", cp_data, "são:", lst_data_main, ".")
     print("Valores da tabela ASCII para:", nkey_cp, "são:", cipher_key_rm, ".")
     print(st_f)
     print("Agora vamos converter os Valores em binário.")
     print(st_f)
     print('Ref binária para: {} >>>>>>>'.format(cp_data),conv_op) 
     print('Ref binária para: {} >>>>>>>'.format(nkey_cp),key_convert_rm) 
     print('Operação bit a bit na porta XOR ...', " ".join([unicode_f]*len(cp_data)))
     print('Dados criptografados >>>>>>>>>>>>',data_done_rm)
     print(st_f)

    else: # Se key for menor ad. chars
     print(st_f)
     print("Valores da tabela ASCII para:", cp_data, "são:", lst_data_main, ".")
     print("Valores da tabela ASCII para:", n_key, "são:", cipher_key_ad, ".")
     print(st_f)
     print("Agora vamos converter os Valores em binário.")
     print(st_f)
     print('Ref binária para: {} >>>>>>>'.format(cp_data),conv_op) 
     print('Ref binária para: {} >>>>>>>'.format(n_key),key_convert_ad) 
     print('Operação bit a bit na porta XOR ...', " ".join([unicode_f]*len(cp_data)))
     print('Dados criptografados >>>>>>>>>>>>',data_done_ad)
     print(st_f)
cipher()  
table()





   