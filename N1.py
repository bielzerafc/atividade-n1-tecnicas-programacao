#Técnicas de Programação
#Atividade N1

#Grupo 3:
#Alunos: Gabriel Ferreira Cavalhieri - RA: 21515695 / João Lucas de Souza Yonéa - RA: 21598575 / Roberta Duprat - RA: 21551006

caminhoPv = 0  
sala = 1        
interacaoCam = 0  

while True: 
    if sala == 9 and interacaoCam <7:
        print("\nVocês completaram o labirinto com {} interações, você e sua guilda venceram, parabens!".format(interacaoCam))
        break
    elif sala == 9 and interacaoCam >= 7:
        print("\n\tVocê levou 7 ou mais interações para chegar na sala 9")
        print ("Você perdeu, tente novamente!")
        print ("Total de Interações: {}".format(interacaoCam))
        break
    else:
        print ("Você está na sala: {}".format(sala))    
        print ("Escolha seu caminho: ")
        print ("[1] - Caminho vermelho")
        print ("[2] - Caminho preto")
        caminhoPv = int(input())
