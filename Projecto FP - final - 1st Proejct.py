# Nome: Jorge Miguel Pereira do Carmo, Numero: 79702, Grupo: al79702
import random


def verifica_cc(numcartao):
    """
    
    Verifica se um numero de cartao de credito e verdadeiro e retorna "" se 
    o cartao e falso ou ("Categoria do cartao", "Rede do cartao") se 
    o cartao e verdadeiro. 
    
    Argumentos:
    
        numcartao (inteiro) = Numero de cartao de credito
    
    Devolve:
    
        respostafinal (tuplo) = (Categoria do cartao, Rede do cartao)
        Categoria do cartao (string)
        Rede do cartao (string)
        
    Exemplo:
        
        >>> verifica_cc(38153682601755)
        ('Viagens e entretenimento e bancario', 'Diners Club International')
        
    """
    
    
    numcartao=str(numcartao)
    if luhn_verifica(numcartao) and valida_iin(numcartao):                    
        respostafinal=(categoria(numcartao), valida_iin(numcartao))           
    else:                                                                      
        respostafinal="cartao invalido" 
    return respostafinal

    
    

def calc_soma(numverfinal):
    """
    
    Calcula o valor da soma usada no algoritmo de Luhn usando 
    um numero de cartao de credito sem o ultimo digito.
    
    Argumentos:
    
        numverfinal (string) = Numero de cartao de credito sem o ultimo digito
    
    Devolve:
    
        soma (inteiro) = Valor da soma usada na verificao de luhn

        
    Exemplo:
        
        >>> calc_soma('3248')
        18
        >>> calc_soma("412389432511")
        47
        
    """
    numverfinal2=""                                                         
    for i in range(len(numverfinal)):                        #ciclo de inversao
        numverfinal2=numverfinal2 + numverfinal[len(numverfinal)-1-i] 
    numverfinal=numverfinal2                   
    soma=0                                       
    pos=1                                     
    while pos<len(numverfinal)+1:
        if pos % 2 != 0:                #verifica se a posicao da lista e impar
            num = eval(numverfinal[pos-1]) * 2   
        else: 
            num = eval(numverfinal[pos-1])      
        if num>9:                                
            soma = soma + num - 9 
        else:
            soma = soma + num      
        pos = pos + 1                            
    return soma        






def luhn_verifica(numcartao):
    """
       Usa o algoritmo de Luhn para verificar a validade o cartao.
       
       Argumentos:
       
           numcartao (string) = Numero de cartao de credito
       
       Devolve:
       
           Boleano = True se o cartao e verdadeiro, False se for falso
   
           
       Exemplo:
           
          >>> luhn_verifica('4556245018079')
          True
          >>> luhn_verifica('4556245018072')
          False
           
       """    
    numverifica = eval(numcartao)                   
    ultnum = (numverifica % 10)                       
    numverifica = numverifica // 10                 
    numverifica = str(numverifica)                  
    numcartfinal = calc_soma(numverifica) + ultnum  
    
    if numcartfinal%10==0:                         
        return True 
    else:                                           
        return False





def comeca_por(cad1, cad2): 
    """
       Verifica se um numero (cad1) comeca por outro (cad2).
       
       Argumentos:
       
           cad1 (string) = Numero de cartao de credito
           
           cad2 (string) = Numero a verificar
       
       Devolve:
       
           Boleano = True se cad1 comeca por cad2, False se nao comecar.
   
           
       Exemplo:
           
           >>> comeca_por('12345678', '123')
           True
           >>> comeca_por('12345678', '23')
           False
           >>> comeca_por('123', '12345678')
           False
           
       """        
    if len(cad2)>len(cad1):                     
        return False                            
    if cad2 in cad1[0:len(cad2)]:               
        #se os numeros desde o inicio do cc ate ao tamanho do numero disponivel
        #forem iguais ao numero disponivel entao e o cc comeca pelo numero
        return True                             
    return False






def comeca_por_um(cad, t_cads):                                               
    """
    
       Verifica se um numero (cad) comeca por alguns dos numeros presentes 
       no tuplo (t_cads).
       
       Argumentos:
       
           cad (string) = Numero de cartao de credito
           
           t_cads (tuplo) = Tuplo com strings iniciais para verificar
       
       Devolve:
       
           Boleano = True se o numero (cad) comeca por alguma string presente 
           no tuplo (t_cads), False se nao comecar.
           
       Exemplo:
           
          >>> comeca_por_um('36238462919584', ('309',' 36', '38', '39'))
          True
          >>> comeca_por_um('36238462919584', ('34', '37'))
          False
           
       """          
    for i in t_cads:
        if comeca_por(cad, i):
            return True
    return False




def valida_iin(cadeiacc):
    """
    
       Verifica se um numero de cartao de credito pertence a alguma rede.
       
       Argumentos:
       
           cadeiacc (string) = Numero de cartao de credito
       
       Devolve:
       
           Nome da rede (string) = Nome da rede a que o cartao pertence, 
           ou caso nao pertence a nenhuma "".
           
       Exemplo:
           
           >>> valida_iin('4508654345231273')
           'Visa Electron'
           >>> valida_iin('45086')
           ''
           
       """       
    AE=("34", "37")                                                      
    DCI=("309", "36", "38", "39")                                            
    DC=('65', '65')                                                         
    M=('5018', '5020',  '5038')
    MC=('50', '51', '52', '53', '54', '19')
    VE= ('4026', '426', '4405', '4508')
    V=('4024', '4532', '4556')
    rede=(AE, DCI, DC, M, MC, VE, V)
    tama=((15,), (14,), (16,), (13, 19), (16,), (16,), (13, 16))
    nomes=("American Express", "Diners Club International", "Discover Card", 
           "Maestro", "Master Card", "Visa Electron", "Visa")  
    i = len(rede)-1                                                             
    while i>=0:                                                                 
            if comeca_por_um(cadeiacc, rede[i]) and (len(cadeiacc) in tama[i]):     
            #verifica se o cc comeca com algum dos valores das redes e se tem 
            #o comprimento de cc definido pela rede, retorna o nome da rede se
            #verificar as hipoteses
                return nomes[i]                                                     
            
            i=i-1                                                                   
    return ""




def categoria(catcc): 
    """
    
       Determina a que categoria a que um numero de cartao de credito pertence.
       
       Argumentos:
       
           catcc (string) = Numero de cartao de credito
       
       Devolve:
       
           Categoria de cartao (string) = Categoria a que o cartao pertence, ou
           caso nao pertenca a nenhuma "".
           
       Exemplo:
           
           >>> categoria('193')
           'Companhias aereas'
           >>> categoria('1')
           'Companhias aereas'
           
       """           
    cate=("Companhias aereas",
          "Companhias aereas e outras tarefas futuras da industria", 
          "Viagens e entretenimento e bancario / financeiro",
          "Servicos bancarios e financeiros", 
          "Servicos bancarios e financeiros",
          "Merchandising e bancario / financeiro", 
          "Petroleo e outras atribuicoes futuras da industria",
          "Saude, telecomunicacoes e outras atribuicoes futuras da industria",
          "Atribuicao nacional")  
    return cate[eval(catcc[:1])-1]  #verifica o primeiro numero do cc (catcc) e 
             #escolhe a determinada categoria em relacao a posicao no tuplo cate
        





#recebe uma string com a abreviatura da rede
def gera_num_cc(abrev):
    """
    
       Gera um numero de cartao de credito de acordo com a abreviatura da 
       rede fornecida (abrev).
       
       Argumentos:
       
           abrev (string) = Abreviatura da rede de cartao de credito
       
       Devolve:
       
           novocc (inteiro) = Numero de cartao de credito da rede especificada
           gerado aleatoriamente
           
       Exemplo:
           
           >>> gera_num_cc("AE")
           '377773175518387'
           >>> gera_num_cc("V")
           '4532214267951388'
           >>> gera_num_cc("MC")
           '5077642753931324'
           
           
       """            
    AE=("34", "37")
    DCI=("309", "36", "38", "39")
    DC=('65', )
    M=('5018', '5020',  '5038')
    MC=('50', '54', '19')
    VE= ('4026', '426', '4405', '4508')
    V=('4024', '4532', '4556')
    rede=(AE, DCI, DC ,M , MC, VE, V)
    redenome=("AE", "DCI", "DC" ,"M" , "MC", "VE", "V")
    tama=((15,), (14,), (16,), (13, 19), (16,), (16,), (13, 16))
    num=0
    inicio=0
    for i in range(len(redenome)):
        if abrev==redenome[i]:
            num=i                                                              
    inicio=rede[num][int(random.random()*len(rede[num]))]                      
    #escolhe um valor inicial da rede definida usando o random
    
    tamanho=tama[num][int(random.random()*len(tama[num]))] - len(str(inicio))-1        
    #numero de algarismos a serem gerados
    novocc=eval(inicio)
    while tamanho>0:                                                           
        novnum=round(random.random()*9)                                       
        novocc = novocc*10 + novnum                                            
        tamanho-=1
    novocc=str(novocc) + digito_verificacao(str(novocc))                    
        
    return novocc 



def digito_verificacao(quasenovo):                                          
    """
    
       Gera o ultimo digito do novo numero de cartao de credito gerado 
       em gera_num_cc.
       
       Argumentos:
       
           quasenovo (string) = Numero de cartao de credito sem o ultimo digito
       
       Devolve:
       
           digito (string) = Digito final de verificacao
           
       Exemplo:
           
           >>> digito_verificacao("30229065652764")
           '7'
           >>> digito_verificacao("503874548929")
           '9'
           >>> digito_verificacao("656291367888525")
           '3'
           
           
       """                
    digito = 10 - (calc_soma(quasenovo))%10                                 
    if digito==10:
        digito=0
    return str(digito)

    
