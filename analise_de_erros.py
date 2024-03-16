from datetime import date
from datetime import datetime
from collections import Counter

def unique(list1):
    x = np.array(list1)
    print(np.unique(x))


extensao = ['RA','RP','RR','RV']
idArquivo = 'D240307.V1130'
tipoArquivo = 'K3249.H29830TO.'

#arquivo = ['K3249.P29830TO.D231207.V0953.RA.txt','K3249.P29830TO.D231206.V0847.RP.txt','K3249.P29830TO.D231206.V0847.RR.txt','K3249.P29830TO.D231206.V0847.RV.txt']
arquivo = [tipoArquivo+idArquivo+'.RA.txt',tipoArquivo+idArquivo+'.RP.txt',tipoArquivo+idArquivo+'.RR.txt',tipoArquivo+idArquivo+'.RV.txt']
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
    erros = []
    lista_final=[]
    header = 'TO'+ tipoArquivoHeader[j]+'20'+ dataNova
    
    k=0
    for k in range(500):
        header+=' '
    lista_final.append(header[0:tamanhoLinha[j]]+'\n')
    
    for i in range(len(linhas)-2,0, -1):
        linha=linhas[i]
        if linhas[i][-4:-1]!='000':
            erros.append(linhas[i][-4:-1])
            lista_final.append(linha)
    contagem = '0000000'+str(len(lista_final)-1)
    trailer = contagem[-6]+contagem[-5]+contagem[-4]+contagem[-3]+contagem[-2]+contagem[-1]
    lista_final.append(trailer)

    i=0
    
    if len(erros)>0:
        nomeArquivo = 'K3244.P29830TO.D'+dataNova+'.V'+horaNova+'.'+extensao[j]
        arquivoFinal = open(nomeArquivo,'w+')
        for i in range(len(lista_final)):
            arquivoFinal.write(lista_final[i])
        arquivoFinal.close()
    
    print(arquivo[j])
    #unique(erros)

    contagemErros = {i:erros.count(i) for i in erros}
    print(contagemErros,'\n')

pause = input('ARQUIVOS GERADOS')