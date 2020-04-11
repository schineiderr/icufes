##############################################
# Funcao para imprimir as listas de listas
# A funcao le a lista elemento por elemento
# e imprime no modelo do arquivo enviado

def imprime_ll(ll):
    for i in ll:
        if not i == []:
            print('[', end=' ')
            for j in i:
                if type(j) == int:
                    print(j, end='  ')
                else:
                    print("%5.3f" %j, end=' ')
            print("]\n")
##############################################

#################################################################
#Função de leitura de arquivo no modelo enviado para a tarefa
#Cria variaveis para cada tipo de dado
#le o arquivo e e preenche as estruturas

def Leitura(entrada):
    #VARIAVEIS LOCAIS A FUNCAO LEITURA
    texto = []      #lista q vai armazenar dados dos textos inuteis no arquivo
    nos, nosf, m, ncp, M, ot, N = 0, 0, 0, 0, 0, 0, 0       #variaveis simples (inteiros ou floats)
    distancia = []  #lista de listas que vai armazenar as distancias dispostas no arq
    t = []          #lista de lsitas floats
    prop = []       #lista de listas inteiros ( 0 ou 1 )
    vlc = []        #lista de listas int ou float
    wti = []        #lista simples que armazena inteiros
    wtf = []        #lista simples que armazena inteiros
    vlb = []        # lista simples para floats
    ck = []         #para inteiros
    cd = []         # int e float
    fhand = open(entrada, encoding = "ISO-8859-1")
    linha = fhand.readline()
    #texto = []
    #nos = 0
    #inicio leitura
    while linha:
            valor = linha.split() #transformo linha em lista de strings
            if valor: #se nao for vazio
                    if (valor[0] == 'nos'): #Se encontrei a secao com valores dos 'nos' na primeira string da lista
                            #print(valor)
                            #print(valor[len(valor)-1])
                            aux = valor[len(valor)-1] #ultima string da lista contem valor numerico seguido de ';'
                            aux = aux[:-1] #removo ';'
                            nos = int(aux) #guardo valor na memoria
                            #print(nos)
                            texto.append([valor[0]]) #guardo texto inutil para marcar lugar da secao 'nos'
                    elif (valor[0] == 'nosf'): #procuro o valor 'nosf' na primeira string da lista
                            #print(valor)
                            #print(valor[len(valor)-1]) #print para verificar a alteração necessária
                            aux = valor[len(valor)-1] #aux recebeu o ultimo valor da string
                            aux = aux[:-1] #removo o ';'
                            nosf = int(aux) #transformo em inteiro e guardo na variavel de mesmo nome do arq original
                            #print(nosf)
                            texto.append(valor[0]) #string da lista é guardada na lista texto para retornar valor
                    elif (valor[0] == 'm'): #procuro valor 'm' na primeira string
                            #print(valor)   
                            #print(valor[len(valor)-1])
                            aux = valor[len(valor)-1]
                            aux = aux[:-1]
                            m = int(aux)
                            #print(m)
                            texto.append(valor[0])
                    elif (valor[0] == 'ncp'):
                            #print(valor)
                            #print(valor[len(valor)-1])
                            aux = valor[len(valor)-1]
                            aux = aux[:-1]
                            ncp = int(aux)
                            #print(ncp)
                            texto.append(valor[0])
                    elif (valor[0] == 'M'):
                            #print(valor)
                            #print(valor[len(valor)-1])
                            aux = valor[len(valor)-1]
                            aux = aux[:-1]
                            M = int(aux)
                            #print(M)
                            texto.append(valor[0])
                    elif (valor[0] == 'ot'):
                            #print(valor)
                            #print(valor[len(valor)-1])
                            aux = valor[len(valor)-1]
                            aux = aux[:-1]
                            ot = float(aux) #nesse caso a variável é um flutuante
                            #print(ot)
                            texto.append(valor[0])
                    elif (valor[0] == 'N'):
                            #print(valor)
                            #print(valor[len(valor)-1])
                            aux = valor[len(valor)-1]
                            aux = aux[:-1]
                            N = int(aux)
                            #print(N)
                            texto.append(valor[0])
                    elif (valor[0] == 'distancia'): #procuro a lista de listas 'distancia'
                            texto.append(valor[0]) #guardo na memoria para chamar na saida
                            #distancia = []          #crio uma lista vazia para colocar as listas
                            while valor[len(valor)-1] != '];': #enquanto não acho a linha que termina a lista 'distancia'
                                    linha = fhand.readline()    #continuo a leitura dentro do loop
                                    valor = linha.split()       #transformo a linha numa lista de strings
                                    #print(valor)                #imprimo apenas para conferir as strings
                                    listadist = []              # crio uma lista para cada lista dentro de distancia
                                    for i in range(1, len(valor)-1):    #loop dentro de cada string da lista 'valor'
                                            #print (valor[i])
                                            try:
                                                listadist.append(int(valor[i]))   #tento transformar em inteiro.
                                            except:
                                                try:
                                                    listadist.append(float(valor[i])) #se não funciona, tenta em float (caso dos numeros em que há ponto). RESOLVER!!
                                                except: continue                      #continua nos '['
                                    #print(listadist)
                                    distancia.append(listadist)     #armazeno na lista de listas
                            #imprime_ll(distancia)
                    elif (valor[0] == 't'):     #procuro pela lista de listas 't'
                            texto.append(valor[0])  #adiciono em texto para procurar na escrita depois
                            #t = []              #crio lista de listas para armazenar dados
                            while valor[len(valor)-1] != '];':  #leio até a ultima linha das listas
                                    linha = fhand.readline()    #continuo a leitura das linhas
                                    valor = linha.split()       #transforma em lista
                                    listat = []         
                                    for i in range(1, len(valor)-1):    #percorro a lista de strings 'valor'
                                            #print (valor[i])
                                            try:
                                                listat.append(int(valor[i]))
                                            except:
                                                try:
                                                    listat.append(float(valor[i]))
                                                except: continue
                                    #print(listat)
                                    t.append(listat)
                            #imprime_ll(t)
                    elif (valor[0] == 'prop'):      #procuro lista de listas novamente
                            texto.append(valor[0])
                            #prop = []
                            while valor[len(valor)-1] != '];':  #fim da lista de listas
                                    linha = fhand.readline()
                                    valor = linha.split()
                                    listaprop = []
                                    for i in range(1, len(valor)-1):
                                            #print (valor[i])
                                            try:
                                                listaprop.append(int(valor[i]))
                                            except: continue
                                    #print(listaprop)
                                    prop.append(listaprop)
                            #imprime_ll(prop)
                    elif (valor[0] == 'vlc'):           #ultima lista de listas
                            texto.append(valor[0])
                            texto.append(' '.join(valor[3:]))   #caso particular que adiciono texto dentro da variavel vlc (lista de listas)
                            #print(' '.join(valor[3:]))
                            #vlc = []
                            while valor[len(valor)-1] != '];':  #fim da lista de listas 'vlc'
                                    linha = fhand.readline()
                                    valor = linha.split()
                                    listavlc = []
                                    for i in range(1, len(valor)-1):
                                            #print (valor[i])
                                            try:
                                                listavlc.append(int(valor[i]))
                                            except: continue
                                    #print(listavlc)
                                    vlc.append(listavlc)
                            #imprime_ll(vlc)
                    elif (valor[0] == 'wti'):       #procuro pela lista 'wti'
                        texto.append(valor[0])      #guardo na memoria para chamar na escrita
                        #wti = []                    #crio lista para guardar dados
                        for i in range(len(valor)): #percorro a lista de strings
                            try:
                                wti.append(int(valor[i]))   #transformo em inteiro e adiciona na lista
                            except:
                                try:
                                    rem = valor[i]      #cheganod no ultimo elemento da lista atribuo ele a uma variavel
                                    rem = rem[:-2]      #removo os '];'
                                    wti.append(int(rem))    #adiciono na lista
                                except: continue
                        #print(wti)
                    elif (valor[0] == 'wtf'): #idem 'wti'
                        texto.append(valor[0])
                        #wtf = []
                        for i in range(len(valor)):
                            try:
                                wtf.append(int(valor[i]))
                            except:
                                try:
                                    rem = valor[i]
                                    rem = rem[:-2]
                                    wtf.append(int(rem))
                                except: continue
                        #print(wtf)
                    elif (valor[0] == 'vlb'):   #idem anteriores
                        texto.append(valor[0])
                        #vlb = []
                        for i in range(len(valor)):
                            try:
                                vlb.append(float(valor[i])) #nesse caso é float
                            except: 
                                try:
                                    rem = valor[i]
                                    rem = rem[:-2]
                                    vlb.append(float(rem))
                                except: continue
                        #print(vlb)
                    elif (valor[0] == 'ck'): #idem anteriores
                        texto.append(valor[0])
                        #ck = []
                        for i in range(len(valor)):
                            try:
                                ck.append(int(valor[i]))
                            except: 
                                try:
                                    rem = valor[i]
                                    rem = rem[:-2]
                                    ck.append(int(rem))
                                except:
                                    try:                    #em ultimo caso removo o '[' inical caso não tenha espaços no primeiro integrante da lista
                                        rem = valor[i]
                                        rem = rem[1:]
                                        ck.append(int(rem))
                                    except: continue
                        #print(ck)
                    elif (valor[0] == 'cd'):
                        texto.append(valor[0])
                        #cd = []
                        for i in range(len(valor)):
                            try:
                                cd.append(float(valor[i]))
                            except: 
                                try:
                                    rem = valor[i]
                                    rem = rem[:-2]
                                    cd.append(float(rem))
                                except:
                                    try:
                                        rem = valor[i]
                                        rem = rem[1:]
                                        cd.append(int(rem))         #para esse caso e inteiro, mais generico seria float, por enquanto manterei assim
                                    except: continue
                        #print(cd)
                    #Se nao eh uma secao de dados
                    else:
                            #print(valor)
                            texto.append(valor) # armazeno texto inutil para replicar arquivo mais tarde
            #leitura da proxima linha
            linha = fhand.readline()
    fhand.close()
    return (texto, nos, nosf, m, ncp, M, ot, N, distancia, t, prop, vlc, wti, wtf, vlb, ck, cd)
#fim leitura
#####################################################################################################


#####################################################################################################
# Funcao de escrita em um novo arquivo dos dados obtidos na funcao leitura
# Abro um arquivo de saida e percorro todo o arquivo texto
# Escrevo como copia identica do arquivo original
# Inicio escrita

def Escrita(saida, texto, nos, nosf, m, ncp, M, ot, N, distancia, t, prop, vlc, wti, wtf, vlb, ck, cd):
    fout = open(saida, 'w')
    #percorrer todo o texto inutil
    for linha in texto: # linha eh uma lista de strings
        #print(' '.join(linha)) # reconstruo linha com strings da lista concatenadas e separadas por espaco
        if (linha[0] == 'nos'): # se encontro a secao de dados 'nos' recupero dados da memoria (variavel nos)
            fout.write(linha[0]+ " = " + str(nos) +';\n\n') # crio linha igual arquivo de origem
        elif (linha == 'nosf'):
            fout.write(linha+ " = " + str(nosf) +';\n\n')   
        elif (linha[0] == 'm'):
            fout.write(linha[0]+ " = " + str(m) +';\n\n')
        elif (linha == 'ncp'):
            fout.write(linha+ " = " + str(ncp) +';\n\n')
        elif (linha[0] == 'M'):
            fout.write(linha[0]+ " = " + str(M) +';\n\n')
        elif (linha == 'ot'):
            fout.write(linha+ " = " + str(ot) +';\n\n')
        elif (linha[0] == 'N'):
            fout.write(linha[0]+ " = " + str(N) +';\n\n')
        elif (linha == 'distancia'):            #recuperando a lista de listas na memoria
            #print(linha)
            fout.write(linha+ " = [\n")     #crio linha igual a de entrada
            for i in distancia:             #percorro cada lista da lista distancia
                if i != []:
                    fout.write('[	')         
                    for j in i:                 #percorro cada item da lista
                        if type(j) == int:
                            fout.write(str(j)+'	')
                        else:
                            fout.write("%.3f	" %j)   #transformo cada item de cada lista em string e escrevo no arq de saida
                    fout.write(']\n')           #ao final de cada lista fecho e pulo uma linha    
            fout.write("            ];\n\n")    #reproduzo linha igual arquivo original
        elif (linha == 't'):
            #print(linha)
            fout.write(linha+ " = [\n")
            for i in t:
                if i != []:
                    fout.write('[	')
                    for j in i:
                        if type(j) == int:
                            fout.write(str(j)+'  ')
                        else:
                            fout.write("%.3f   " %j)
                    fout.write(']\n')
            fout.write("            ];\n\n")
        elif (linha == 'prop'):
            #print(linha)
            fout.write(linha+ " = [\n")
            for i in prop:
                if i != []:
                    fout.write('[	')
                    for j in i:
                        fout.write(str(j) + '	')
                    fout.write(']\n')
            fout.write("];\n\n")
        elif (linha == 'vlc'):
            fout.write(linha+ " = [ " + texto[texto.index('vlc')+1] + "\n") #reproduzo linha igual arquivo original
            for i in vlc:
                if i != []:
                    fout.write('[ ')
                    for j in i:
                        fout.write(str(j) + '  ')
                    fout.write(']\n')
            fout.write("];\n\n")
        elif (linha == 'wti'):  #acho lista no texto
            fout.write(linha+" = "+'[ ')    #começo a escrever linha igual arq original
            for i in wti:     #percorro lista 'wti'
                fout.write(str(i)+'	')  #escrevo cada item na forma de str
            fout.write('];\n\n')            #fecho a lista
        elif (linha == 'wtf'):
            fout.write(linha+" = "+'[ ')
            for i in wtf:
                fout.write(str(i)+'	')
            fout.write('];\n\n')
        elif (linha == 'vlb'):
            fout.write(linha+" = "+'[ ')
            for i in vlb:
                fout.write(str(i)+' ')
            fout.write('];\n\n')
        elif (linha == 'ck'):
            fout.write(linha+" = "+'[')
            for i in ck:
                fout.write(str(i)+' ')
            fout.write('];\n')
        elif (linha == 'cd'):
            fout.write(linha+" = "+'[')
            for i in cd:
                fout.write(str(i)+' ')
            fout.write('];\n\n')
        elif not(' '.join(linha).startswith('/ / ( s')):    #caso particular de texto inutil que surge dentro da variavel 'vlc'
            fout.write(' '.join(linha)+'\n') # reconstruo linha com strings da lista concatenadas e separadas por espaco e pula linha
    fout.close()
    print("\n\nFIM - verificar arquivo de saida.\n")
#fim escrita
#####################################################################################################

    
#####################################################################################################
# Funcao para criar um arquivo de saida '.dot'
# Gera um grafo para a lista de listas 'distancia' pelo graphviz

def Grafo_distancia(name, distancia):
    arq = open(str(name) + '.dot', 'w')             #abro um arquivo '.dot' para escrever na linguagem do graphviz
    arq.write('strict graph ' + name + ' {\n')             #escrevo a primeira linha como é padrao da linguagem
    for i in range(len(distancia)-1):               #percorro cada lista dentro de distancia
        for j in range(len(distancia[i])-1):        # e percorro cada elemento da lista
            if not i == j and distancia[i][j] != 9999:      #ignoro as distancias entre os mesmos elementos e as distancias 'infinitas' ditas '9999'
                arq.write(str(i) + '--' + str(j) + ' [label =  "' + "%.3f" %distancia[i][j] + 'km"]' + ';\n')   #escrevo uma aresta como vertice os indices da matriz distancia
    arq.write('}')
    arq.close()
    print("\nVerificar arquivo de saída.\n")

    #executar no terminal -> dot nomedoarquivo.dot -Tpng -o nomedografo.png
#####################################################################################################

#####################################################################################################
# Funcao principal para controle do fluxo do programa

def main():
    ### VARIAVEIS LOCAIS A FUNCAO MAIN ### chamo a funcao de leitura e
    ### estabeleco as variaveis para usar como atributo na funcao de escrita
    texto, nos, nosf, m, ncp, M, ot, N, distancia, t, prop, vlc, wti, wtf, vlb, ck, cd = Leitura(input("Entre com o nome do arquivo de entrada: "))
    #Escrita(input("Entre com o nome do arquivo de saída: "), texto, nos, nosf, m, ncp, M, ot, N, distancia, t, prop, vlc, wti, wtf, vlb, ck, cd)
    Grafo_distancia(input("Nome do Grafo: "), distancia)
#####################################################################################################

# Roda o programa chamando main()
main()
