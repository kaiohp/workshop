from datetime import date
from datetime import datetime

extensao = ['RA','RP','RR','RV']
arquivo = ['RA.CSV','RP.CSV','RR.CSV','RV.CSV']
tamanhoLinha = [361,349,42,119]
tipoArquivoHeader = ['1','4','2','3']

j=0

for j in range(len(arquivo)):
    linhas = []
    with open(arquivo[j]) as f:
        linhas = f.readlines()

    count = 0

    for line in linhas:
        count += 1
        
    data = str(date.today())
    dataNova = data[2]+data[3]+data[5]+data[6]+data[8]+data[9]
    hora = str(datetime.now())
    horaNova = hora[11]+hora[12]+hora[14]+hora[15]
    
    i=0
    lista_final=[]
    header = 'TO'+ tipoArquivoHeader[j]+'20'+ dataNova
    
    k=0
    for k in range(500):
        header+=' '
    lista_final.append(header[0:tamanhoLinha[j]]+'\n')
    
    for i in range(len(linhas)):      
      if j==3:
        linhaAtual=(((linhas[i].replace(';','')).replace('CONSIDERAR LINHA','')).replace('DESCONHECIDO',''))
      else:
        linhaAtual=(linhas[i].replace(';',''))
     
      if (linhaAtual[0])=='I':
        lista_final.append(linhaAtual)
        
      if (len(lista_final[-1])-1)!=tamanhoLinha[j]:
        print('Erro ',arquivo[j],' linha ',i+1)    
      i+=1

    contagem = '0000000'+str(len(lista_final)-1)
    trailer = contagem[-6]+contagem[-5]+contagem[-4]+contagem[-3]+contagem[-2]+contagem[-1]
    lista_final.append(trailer)

    i=0   

    nomeArquivo = 'K3244.H29830TO.D'+dataNova+'.V'+horaNova+'.'+extensao[j]
    arquivoFinal = open(nomeArquivo,'w+')
    for i in range(len(lista_final)):
        arquivoFinal.write(lista_final[i])
    arquivoFinal.close()
    
    print(arquivo[j])
    j+=1

pause = input('ARQUIVOS GERADOS')