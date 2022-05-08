import os
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False) #para não exibir mensagens de erro
reader = SimpleMFRC522()#fazendo cópia da função

while(1):
    os.system("clear")
    x = input("APERTE 1 PARA VER A IDENTIFICAÇÃO\nOU 2 PARA INSERIR NOVA IDENTIFICAÇÃO\n")#leitura da opção desejada
    os.system("clear")
    if x=="1":
        print("\nMODO DE LEITURA SELECIONADO:\nAPROXIME O CARTÃO.\n")
        try:
            id, text = reader.read() #id não muda, o que podemos mudar é o text
            #print(id)
            print("IDENTIFICAÇÃO DO CARTÃO:")
            print(text) #exibe o que está na variável text da TAG
        finally:
            GPIO.cleanup()
            nova = input("\n\nNOVA OPERAÇÃO? 1-SIM 2-NÃ0 : ")
            if nova == "2":
                os.system("clear")
                break
            
            print("\n\n")
    
    else:
        print("NOVA IDENTIFICAÇÃO SELECIONADA:\n")
        try:
            text = input('INSIRA A NOVA ID: ') #escreve novo texto na TAG
            os.system("clear")
            print("APROXIME O CARTÃO.\n")
            reader.write(text)
            print("NOVA IDENTIFICAÇÃO INSERIDA COM SUCESSO:")
            print(text)
        finally:
            GPIO.cleanup()
            nova = input("\n\nNOVA OPERAÇÃO? 1-SIM 2-NÃ0 : ")
            if nova == "2":
                os.system("clear")
                break
            print("\n\n")
        
        
