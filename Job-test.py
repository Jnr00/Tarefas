comparativos = ["qwertyuiop","asdfghjkl","zxcvbnm"]
words = ["ola","gas", "col"]

def analisa_letras(palavra):
       for i in range(0,len(palavra)-1):
           count = 0
           for palavra[i] in comparativos[0]:
               count += 1
        if count == len(palavra):
            print(f'a palavra {palavra} está em {comparativos[0]}')
       for j in range(0,len(palavra)-1):
           count1 = 0
           for palavra[j] in comparativos[1]:
               count += 1
        if count1 == len(palavra):
            print(f'a palavra {palavra} está em {comparativos[1]}')
       for k in range(0,len(palavra)-1):
           count2 = 0
           for palavra[k] in comparativos[2]:
               count1 += 1
        if count2 == len(palavra):
            print(f'a palavra {palavra} está em {comparativos[2]}')
        m = len(palavra)
        if (count or count1 or count2) != m) :
            print(f"{palavra} nao esta em unica linha")
          
    for v in range(0, len(words)-1):
        analisa_letras(word[v])
