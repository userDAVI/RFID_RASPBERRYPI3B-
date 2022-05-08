import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False) #não exibir mensagens de erro

reader = SimpleMFRC522()
		
try:
	id, text = reader.read()
	print(id)
	print(text)
finally:
	GPIO.cleanup()
