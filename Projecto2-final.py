# Nome: Jorge Miguel Pereira do Carmo, Numero: 79702
# Nome: Ricardo Jorg Moreira Tavares, Numero: 78198
# Grupo: al021


from random import random
def cria_coordenada(l, c):
    """
    funcao construtora do tipo coordenada
    Argumentos: dois inteiros; o primeiro corresponde a linha (l) e o segundo 
    corresponde a coluna (c)
    Devolve: um elemento do tipo coordenada (tuplo) correspondente a posicao (l,c),
    ou um erro caso algum argumento seja invalido
    Exemplo:
    >>>cria_coordenada(1,2)
    (1,2)
    """    
    if isinstance(l,int) and isinstance(c,int) and l>0 and l<5 and c>0 and c<5:
        return (l, c)
    else:
        raise ValueError ('cria_coordenada: argumentos invalidos')

def coordenada_linha(coord):
    """
    funcao seletora do tipo coordenada
    Argumento: elemento do tipo coordenada
    Devolve: um inteiro correspondente a linha da coordenada
    Exemplo:
    >>>coordenada_linha(1,2)
    1
    """     
    return coord[0]

def coordenada_coluna(coord):
    """
    funcao seletora do tipo coordenada
    Argumento: elemento do tipo coordenada
    Devolve: um inteiro correspondente a coluna da coordenada
    Exemplo:
    >>>coordenada_coluna(1,2)
    2
    """           
    return coord[1]

def e_coordenada(coord):
    """
    funcao reconhecedora que verifica se o argumento e uma coordenada
    Argumento: elemento a testar
    Devolve: true caso seja uma coordenada, false caso contrario
    Exemplo:
    >>>e_coordenada((1,2))
    true
    """        
    return isinstance(coord, tuple) and len(coord)==2 and \
isinstance(coordenada_linha(coord),int) and \
isinstance(coordenada_coluna(coord),int) and coordenada_linha(coord)>0 and \
coordenada_linha(coord)<=4 and coordenada_coluna(coord)>0 and \
coordenada_coluna(coord)<=4

def coordenadas_iguais(coord1, coord2):
    """
    funcao que testa se duas coordenadas pertencem a mesma posicao do tabuleiro
    Argumentos: dois elementos do tipo coordenada
    Devolve: true caso pertencam a mesma posicao, false caso contrario
    Exemplo:
    >>>coordenadas_iguais((1,2),(1,3))
    false
    """       
    return coordenada_linha(coord1)==coordenada_linha(coord2) and \
           coordenada_coluna(coord1)==coordenada_coluna(coord2)


def cria_tabuleiro():
    """
    funcao construtora do tipo tabuleiro
    Nao recebe argumentos
    Devolve: um elemento do tipo tabuleiro (lista), com todas as posicoes a zero
    Exemplo:
    >>>cria_tabuleiro()
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 0]
    """        
    tab=list(range(5))
    for i in range(4):
        tab[i]=list(range(4))
        for j in range(4):
            tab[i][j]=0
    tab[4]=0
    return tab

def tabuleiro_posicao(tab, coord):
    """
    funcao seletora do tipo tabuleiro
    Argumentos: um elemento do tipo tabuleiro e um elemento do tipo coordenada
    Devolve: o valor correspondente a posicao da coordenada no tabuleiro ou um erro
    caso a coordenada seja invalida
    Exemplo:
    >>>t=cria_tabuleiro()
    >>>tabuleiro_posicao(t,(1,1))
    0
    """    
    if e_coordenada(coord):
        return tab[coordenada_linha(coord)-1][coordenada_coluna(coord)-1]
    else:
        raise ValueError ('tabuleiro_posicao: argumentos invalidos')
         
    
def tabuleiro_pontuacao(tab):
    """
      funcao seletora do tipo tabuleiro
      Argumento: um elemento do tipo tabuleiro
      Devolve: um inteiro correspondente a pontuacao actual do tabuleiro
      Exemplo:
      >>>t=cria_tabuleiro()
      >>>tabuleiro_pontuacao(t)
      0
      """    
    return tab[4]

def tabuleiro_preenche_posicao(tab, coord, valor):
    """
       funcao modificadora do tipo tabuleiro que preenche uma posicao com um dado valor
       Argumentos: um elemento do tipo tabuleiro, um elemento do tipo coordenada e um
       inteiro correspondente a um valor
       Devolve: o tabuleiro modificado com o valor dado aplicado a posicao
       correspondente a coordenada
       Exemplo:
       >>>t=cria_tabuleiro()
       >>>tabuleiro_preenche_posicao(t,(1,2),2)
       [[0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 0]
       """    
    if e_tabuleiro(tab) and e_coordenada(coord) and isinstance(valor, int):
        tab[coordenada_linha(coord)-1][coordenada_coluna(coord)-1]=valor
        return tab
    else:
        raise ValueError ('tabuleiro_preenche_posicao: argumentos invalidos')
    
def tabuleiro_actualiza_pontuacao(tab, valor):
    """
    funcao modificadora do tipo tabuleiro que soma um valor a pontuacao actual do
    tabuleiro
    Argumentos: um elemento do tipo tabuleiro e o inteiro a somar a pontuacao, que
    deve ser nao negativo e multiplo de 4
    Devolve: o tabuleiro modificado com o valor dado somado a pontuacao actual do
    tabuleiro, ou um erro caso algum argumento seja invalido
    Exemplo:
    >>>t=cria_tabuleiro()
    >>>tabuleiro_actualiza_pontuacao(t,4)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 4]
    """    
    if e_tabuleiro(tab) and isinstance(valor, int) and valor>=0 and valor%4==0:
        tab[4]=tabuleiro_pontuacao(tab)+valor
        return tab
    else:
        raise ValueError ('tabuleiro_actualiza_pontuacao: argumentos invalidos')
    
def tabuleiro_reduz(tab, mov):
    """
    funcao modificadora do tipo tabuleiro que o reduz na direccao indicada segundo
    as regras do jogo 2048
    Argumentos: um elemento do tipo tabuleiro e uma cadeia de caracteres ou, mais
    especificamente, 'N', 'S', 'W' ou 'E'
    Devolve: o tabuleiro modificado com a reduccao, incluindo a actualizacao da
    pontuacao, ou um erro caso a jogada seja invalida
    Exemplo:
    >>>t=cria_tabuleiro()
    >>>tabuleiro_preenche_posicao(t,(1,2),2)
    >>>tabuleiro_reduz(t,'W')
    [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 0]
    """    
    if mov=='W':
        tab=tabuleiro_move_esquerda(tab)
        tab=tabuleiro_adiciona_esquerda(tab)
        return tab
    elif mov=='N':
        tab=tabuleiro_move_cima(tab)
        tab=tabuleiro_adiciona_cima(tab)
        return tab
    elif mov=='S':
        tab=tabuleiro_move_baixo(tab)
        tab=tabuleiro_adiciona_baixo(tab)
        return tab
    elif mov=='E':
        tab=tabuleiro_move_direita(tab)
        tab=tabuleiro_adiciona_direita(tab)        
        return tab
    else:
        raise ValueError ('tabuleiro_reduz: argumentos invalidos')
    
def tabuleiro_move_esquerda(tab):
    """
    funcao auxiliar a reduz que "empurra" os valores nao nulos de cada linha
    para o inicio da linha, passando os valores nulos para o final da linha
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com a modificacao mencionada
    """    
    j=0
    vazias=tabuleiro_posicoes_vazias(tab)
    for i in range(4): 
        if not cria_coordenada(i+1, j+1) in vazias or not cria_coordenada(i+1, j+2) in vazias or not cria_coordenada(i+1, j+3) in vazias or not cria_coordenada(i+1, j+4) in vazias:
            if cria_coordenada(i+1, j+1) in  vazias:
                while cria_coordenada(i+1, j+1) in vazias:
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),tabuleiro_posicao(tab, cria_coordenada(i+1, j+2)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),tabuleiro_posicao(tab, cria_coordenada(i+1, j+4)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+4),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
           
                 
            if cria_coordenada(i+1, j+2) in vazias and (not cria_coordenada(i+1, j+3)in vazias or not cria_coordenada(i+1, j+4) in vazias):
                while cria_coordenada(i+1, j+2) in vazias:
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),tabuleiro_posicao(tab, cria_coordenada(i+1, j+4)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+4),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
 
            if cria_coordenada(i+1, j+3) in vazias and (not cria_coordenada(i+1, j+4) in vazias): 
                while cria_coordenada(i+1, j+3) in vazias: 
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),tabuleiro_posicao(tab, cria_coordenada(i+1, j+4)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+4),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
    return tab

def tabuleiro_adiciona_esquerda(tab):
    """
    funcao auxiliar a reduz que soma primeiros valores consecutivos de
    cada linha, passando o resultado para a posicao do primeiro valor,
    "empurrando" a linha uma posicao para a esquerda e colocando um valor nulo
    no final da linha
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com a modificacao mencionada
    """    
    j=0
    global points
    for i in range(0,4):
        if tabuleiro_posicao(tab, cria_coordenada(i+1, j+1))==tabuleiro_posicao(tab, cria_coordenada(i+1, j+2)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),(tabuleiro_posicao(tab, cria_coordenada(i+1, j+1))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),tabuleiro_posicao(tab, cria_coordenada(i+1, j+4)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+4),0)
            
        if tabuleiro_posicao(tab, cria_coordenada(i+1, j+2))==tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),(tabuleiro_posicao(tab, cria_coordenada(i+1, j+2))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+1, j+2)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),tabuleiro_posicao(tab, cria_coordenada(i+1, j+4)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+4),0)
 
        if tabuleiro_posicao(tab, cria_coordenada(i+1, j+3))==tabuleiro_posicao(tab, cria_coordenada(i+1, j+4)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),(tabuleiro_posicao(tab, cria_coordenada(i+1, j+3))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+4),0)
            
    return tab

def tabuleiro_move_direita(tab):
    """
    funcao auxiliar a reduz que "empurra" os valores nao nulos de cada linha
    para o final da linha, passando os valores nulos para o inicio da linha
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com a modificacao mencionada
    """    
    j=0
    vazias=tabuleiro_posicoes_vazias(tab)
    for i in range(4): 
        if not cria_coordenada(i+1, j+1) in vazias or not cria_coordenada(i+1, j+2) in vazias or not cria_coordenada(i+1, j+3) in vazias or not cria_coordenada(i+1, j+4) in vazias:
            if cria_coordenada(i+1, j+4) in  vazias:
                while cria_coordenada(i+1, j+4) in vazias:
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+4),tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),tabuleiro_posicao(tab, cria_coordenada(i+1, j+2)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
           
                 
            if cria_coordenada(i+1, j+3) in vazias and (not cria_coordenada(i+1, j+2)in vazias or not cria_coordenada(i+1, j+1) in vazias):
                while cria_coordenada(i+1, j+3) in vazias:
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),tabuleiro_posicao(tab, cria_coordenada(i+1, j+2)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
 
            if cria_coordenada(i+1, j+2) in vazias and (not cria_coordenada(i+1, j+1) in vazias): 
                while cria_coordenada(i+1, j+2) in vazias: 
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
    return tab

def tabuleiro_adiciona_direita(tab):
    """
    funcao auxiliar a reduz que soma os dois ultimos valores consecutivos de
    cada linha, passando o resultado para a posicao do ultimo valor,
    "empurrando" a linha uma posicao para a direita e colocando um valor nulo no
    inicio da linha
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com a modificacao mencionada
    """       
    j=0
    global points
    for i in range(0,4):
        if tabuleiro_posicao(tab, cria_coordenada(i+1, j+4))==tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+4),(tabuleiro_posicao(tab, cria_coordenada(i+1, j+3))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+1, j+4)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),tabuleiro_posicao(tab, cria_coordenada(i+1, j+2)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
            
        if tabuleiro_posicao(tab, cria_coordenada(i+1, j+3))==tabuleiro_posicao(tab, cria_coordenada(i+1, j+2)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+3),(tabuleiro_posicao(tab, cria_coordenada(i+1, j+2))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+1, j+3)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
 
        if tabuleiro_posicao(tab, cria_coordenada(i+1, j+2))==tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+2),(tabuleiro_posicao(tab, cria_coordenada(i+1, j+1))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+1, j+2)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
            
    return tab

def tabuleiro_move_cima(tab):
    """
    funcao auxiliar a reduz que "empurra" os valores nao nulos de cada coluna
    para o inicio da coluna, passando os valores nulos para o final da coluna
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com a modificacao mencionada
    """        
    i=0
    vazias=tabuleiro_posicoes_vazias(tab)
    for j in range(4): 
        if not cria_coordenada(i+1, j+1) in vazias or not cria_coordenada(i+2, j+1) in vazias or not cria_coordenada(i+3, j+1) in vazias or not cria_coordenada(i+4, j+1) in vazias:
            if cria_coordenada(i+1, j+1) in  vazias:
                while cria_coordenada(i+1, j+1) in vazias:
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),tabuleiro_posicao(tab, cria_coordenada(i+2, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),tabuleiro_posicao(tab, cria_coordenada(i+3, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),tabuleiro_posicao(tab, cria_coordenada(i+4, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+4, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
           
                 
            if cria_coordenada(i+2, j+1) in vazias and (not cria_coordenada(i+3, j+1)in vazias or not cria_coordenada(i+4, j+1) in vazias):
                while cria_coordenada(i+2, j+1) in vazias:
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),tabuleiro_posicao(tab, cria_coordenada(i+3, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),tabuleiro_posicao(tab, cria_coordenada(i+4, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+4, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
 
            if cria_coordenada(i+3, j+1) in vazias and (not cria_coordenada(i+4, j+1) in vazias): 
                while cria_coordenada(i+3, j+1) in vazias: 
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),tabuleiro_posicao(tab, cria_coordenada(i+4, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+4, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
    return tab

def tabuleiro_adiciona_cima(tab):
    """
    funcao auxiliar a reduz que soma os dois primeiros valores consecutivos de
    cada coluna, passando o resultado para a posicao do primeiro valor,
    "empurrando" a coluna uma posicao para cima e colocando um valor nulo no
    final da coluna
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com a modificacao mencionada
    """      
    i=0
    global points
    for j in range(0,4):
        if tabuleiro_posicao(tab, cria_coordenada(i+1, j+1))==tabuleiro_posicao(tab, cria_coordenada(i+2, j+1)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),(tabuleiro_posicao(tab, cria_coordenada(i+1, j+1))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),tabuleiro_posicao(tab, cria_coordenada(i+3, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),tabuleiro_posicao(tab, cria_coordenada(i+4, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+4, j+1),0)
            
        if tabuleiro_posicao(tab, cria_coordenada(i+2, j+1))==tabuleiro_posicao(tab, cria_coordenada(i+3, j+1)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),(tabuleiro_posicao(tab, cria_coordenada(i+2, j+1))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+2, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),tabuleiro_posicao(tab, cria_coordenada(i+4, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+4, j+1),0)
 
        if tabuleiro_posicao(tab, cria_coordenada(i+3, j+1))==tabuleiro_posicao(tab, cria_coordenada(i+4, j+1)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),(tabuleiro_posicao(tab, cria_coordenada(i+3, j+1))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+3, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+4, j+1),0)
            
    return tab    

def tabuleiro_move_baixo(tab):
    """
    funcao auxiliar a reduz que "empurra" os valores nao nulos de cada coluna
    para o final da coluna, passando os valores nulos para o inicio da coluna
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com a modificacao mencionada
    """    
    i=0
    vazias=tabuleiro_posicoes_vazias(tab)
    for j in range(4): 
        if not cria_coordenada(i+1, j+1) in vazias or not cria_coordenada(i+2, j+1) in vazias or not cria_coordenada(i+3, j+1) in vazias or not cria_coordenada(i+4, j+1) in vazias:
            if cria_coordenada(i+4, j+1) in  vazias:
                while cria_coordenada(i+4, j+1) in vazias:
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+4, j+1),tabuleiro_posicao(tab, cria_coordenada(i+3, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),tabuleiro_posicao(tab, cria_coordenada(i+2, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
           
                 
            if cria_coordenada(i+3, j+1) in vazias and (not cria_coordenada(i+2, j+1)in vazias or not cria_coordenada(i+1, j+1) in vazias):
                while cria_coordenada(i+3, j+1) in vazias:
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),tabuleiro_posicao(tab, cria_coordenada(i+2, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
 
            if cria_coordenada(i+2, j+1) in vazias and (not cria_coordenada(i+1, j+1) in vazias): 
                while cria_coordenada(i+2, j+1) in vazias: 
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
                    tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
                    vazias=tabuleiro_posicoes_vazias(tab)
    return tab

def tabuleiro_adiciona_baixo(tab):
    """
    funcao auxiliar a reduz que soma os dois ultimos valores consecutivos de
    cada coluna, passando o resultado para a posicao do ultimo valor,
    "empurrando" a coluna uma posicao para baixo e colocando um valor nulo no
    inicio da coluna
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com a modificacao mencionada
    """      
    i=0
    global points
    for j in range(0,4):
        if tabuleiro_posicao(tab, cria_coordenada(i+4, j+1))==tabuleiro_posicao(tab, cria_coordenada(i+3, j+1)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+4, j+1),(tabuleiro_posicao(tab, cria_coordenada(i+3, j+1))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+4, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),tabuleiro_posicao(tab, cria_coordenada(i+2, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
            
        if tabuleiro_posicao(tab, cria_coordenada(i+3, j+1))==tabuleiro_posicao(tab, cria_coordenada(i+2, j+1)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+3, j+1),(tabuleiro_posicao(tab, cria_coordenada(i+2, j+1))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+3, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
 
        if tabuleiro_posicao(tab, cria_coordenada(i+2, j+1))==tabuleiro_posicao(tab, cria_coordenada(i+1, j+1)):
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+2, j+1),(tabuleiro_posicao(tab, cria_coordenada(i+1, j+1))*2))
            tab=tabuleiro_actualiza_pontuacao(tab, tabuleiro_posicao(tab, cria_coordenada(i+2, j+1)))
            tab=tabuleiro_preenche_posicao(tab, cria_coordenada(i+1, j+1),0)
            
    return tab  

def e_tabuleiro(tab):
    """
    funcao que verifica se o argumento e do tipo tabuleiro, sem verificar se as
    posicoes do tabuleiro sao potencias de 2
    Argumento: elemento a testar
    Devolve: true caso o elemento corresponda a um tabuleiro, false caso contrario
    Exemplo:
    >>>t=cria_tabuleiro()
    >>>e_tabuleiro(t)
    True
    """    
    if isinstance(tab, list) and len(tab)==5:
        for i in range(4):
            if isinstance(tab[i], list) and len(tab[i])==4:
                for j in range(4):
                    if not isinstance(tabuleiro_posicao(tab, \
                    cria_coordenada(i+1, j+1)), int):
                        return False
            else:
                return False
        if not isinstance(tab[4], int) and tab[4]<0:
            return False
        return True
    else:
        return False
            


def tabuleiro_posicoes_vazias(tab):
    """
    funcao seletora das posicoes vazias de um tabuleiro
    Argumento: um elemento do tipo tabuleiro
    Devolve: uma lista que contem as coordenadas de todas as posicoes com valor 0 do
    tabuleiro
    Exemplo:
    >>>t=cria_tabuleiro()
    >>>tabuleiro_posicoes_vazias(t)
    [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2),
    (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]
    """        
    resultado=[]
    for i in range(4):
        for j in range(4):
            if tabuleiro_posicao(tab, cria_coordenada(i+1, j+1))==0:
                resultado=resultado + [cria_coordenada(i+1, j+1)]
    return resultado


def tabuleiro_terminado(tab):
    """
    funcao que verifica se um tabuleiro esta terminado, ou seja, esta cheio e nao
    apresenta movimentos possiveis
    Argumento: um elemento do tipo tabuleiro
    Devolve: true caso o tabuleiro esteja terminado, false em caso contrario
    Exemplo:
    >>>t=cria_tabuleiro()
    >>>tabuleiro_terminado(t):
    False
    """        
    terminado=False
    for i in range(4):
        for j in range(4):
            if i>=1:
                terminado=(tabuleiro_posicao(tab, cria_coordenada(i+1,j+1))\
                            !=tabuleiro_posicao(tab, cria_coordenada(i+1,j+1)))
                if j >=1:
                    terminado=(tabuleiro_posicao(tab, cria_coordenada(i+1,j+1))\
                                !=tabuleiro_posicao(tab,\
                                                    cria_coordenada(i+1,j)))
            elif i<=2:
                terminado=(tabuleiro_posicao(tab, cria_coordenada(i+1,j+1))\
                          !=tabuleiro_posicao(tab, cria_coordenada(i+2,j+1))) 
                if j <=1:
                    terminado=(tabuleiro_posicao(tab, cria_coordenada(i+1,j+1))\
                                !=tabuleiro_posicao(tab,\
                                                    cria_coordenada(i+1,j+2)))
    if len(tabuleiro_posicoes_vazias(tab))==0 and terminado==True:
        return True
    return False
    
                            
                        
def tabuleiros_iguais(tab1, tab2):
    """
    funcao que testa se dois tabuleiros apresentam a mesma configuracao e pontuacao
    Argumentos: dois elementos do tipo tabuleiro
    Devolve: true caso os tabuleiros sejam iguais, false caso contrario
    Exemplo:
    >>>t1=cria_tabuleiro()
    >>>t2=cria_tabuleiro()
    >>>tabuleiros_iguais(t1,t2)
    True
    """    
    return tab1==tab2

def escreve_tabuleiro(tab):
    """
    funcao que escreve no ecra a representacao externa de um tabuleiro de 2048
    Argumento: um elemento do tipo tabuleiro
    Devolve: a representacao externa do tabuleiro, ou um erro caso o argumento nao
    seja um tabuleiro valido
    Exemplo:
    >>>t=cria_tabuleiro()
    >>>escreve_tabuleiro(t)
     [  0  ]  [  0  ]  [  0  ]  [  0  ]
     [  0  ]  [  0  ]  [  0  ]  [  0  ]
     [  0  ]  [  0  ]  [  0  ]  [  0  ]
     [  0  ]  [  0  ]  [  0  ]  [  0  ]
     Pontuacao:  0
    """    
    if e_tabuleiro(tab):
        print('[', tabuleiro_posicao(tab, cria_coordenada(1,1)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(1,2)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(1,3)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(1,4)), '] ')
              
        print('[', tabuleiro_posicao(tab, cria_coordenada(2,1)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(2,2)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(2,3)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(2,4)), '] ')              
        
        print('[', tabuleiro_posicao(tab, cria_coordenada(3,1)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(3,2)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(3,3)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(3,4)), '] ')
              
        print('[', tabuleiro_posicao(tab, cria_coordenada(4,1)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(4,2)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(4,3)), ']',\
              '[', tabuleiro_posicao(tab, cria_coordenada(4,4)), '] ')
        print('Pontuacao:', tabuleiro_pontuacao(tab))
    else:
        raise ValueError ('escreve_tabuleiro: argumentos invalidos')
    
def preenche_posicao_aleatoria(tab):
    """
    funcao que preenche um tabuleiro com o valor 2 (80% chance) ou 4 (20% chance)
    numa posicao aleatoria
    Argumento: um elemento do tipo tabuleiro
    Devolve: o tabuleiro com uma posicao aleatoria preenchida com o valor 2 ou 4
    Exemplo:
    >>>t=cria_tabuleiro()
    preenche_posicao_aleatoria(t)
    [[0, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 0]
    """        
    vazias=tabuleiro_posicoes_vazias(tab)
    if len(tabuleiro_posicoes_vazias(tab))!=0:    
        posicao=vazias[int(random()*len(vazias))]
        probabilidade=int(random()*10)
        if probabilidade == 0 or probabilidade == 1:
            return tabuleiro_preenche_posicao(tab, posicao, 4)
        else:
            return tabuleiro_preenche_posicao(tab, posicao, 2)
    else:
        return tab

def copia_tabuleiro(tab1):
    """
    funcao que copia um tabuleiro
    Argumento: um elemento do tipo tabuleiro
    Devolve: um segundo elemento do tipo tabuleiro, semelhante ao tabuleiro dado
    Exemplo:
    >>>t=cria_tabuleiro()
    >>>tabuleiro_preenche_posicao(t,(1,2),4)
    [[0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 0]
    >>>copia_tabuleiro(t)
    [[0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 0]
    """      
    tab2=cria_tabuleiro()
    for i in range(4):
        for j in range(4):
            tab2[i][j]=tab1[i][j]
    tab2[4]=tab1[4]
    return tab2

def pede_jogada():
    """
    funcao que pede ao utilizador uma direccao
    Nao recebe argumentos
    Devolve: uma cadeia de caracteres correspondente a direccao escolhida pelo
    utilizador, ou escreve no ecra um aviso e pede nova jogada
    Exemplo:
    >>>pede_jogada()
    Introduza uma jogada (N, S, E, W): W
    'W'
    """    
    jogada='Inv'
    N='N'
    W='W'
    E='E'
    S='S'
    while jogada=='Inv':
        jogada=eval(input('Introduza uma jogada (N, S, E, W): '))
        if jogada=='N' or jogada=='W' or jogada=='E' or jogada=='S':
            return jogada
        else:
            jogada='Inv'
            print('Jogada invalida')

def jogo_2048():
    """
    funcao principal do jogo 2048 que permite a um jogador jogar um jogo completo.
    em cada turno, a funcao escreve o tabuleiro actual no ecra e pede uma jogada ao
    jogador, actualizando o tabuleiro e repetindo o ciclo ate o tabuleiro se
    encontrar terminado
    Nao recebe argumentos
    Devolve: sucessivos tabuleiros e pedidos de jogadas ate o jogo terminar
    """    
    tab=cria_tabuleiro()
    tab=preenche_posicao_aleatoria(tab)
    escreve_tabuleiro(tab)
    while not tabuleiro_terminado(tab):
        jogada=pede_jogada()
        tabaux=copia_tabuleiro(tab)
        tab=tabuleiro_reduz(tab,jogada)
        if not tabuleiros_iguais(tab,tabaux):
            tab=preenche_posicao_aleatoria(tab)
        escreve_tabuleiro(tab)