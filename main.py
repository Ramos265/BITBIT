# Our main file

import speech_recognition as sr

# Criar um reconhecedor
r = sr.Recognizer()

# Abrir o microfone para captura
with sr.Microphone() as source:  
    audio = r.listen(source) #Define microfone como fonte de áudio
    
    while True:
    print(r.recognize_google(audio, language= "pt"))
    import  speech_recognition  as  sr 
for  index ,  name  in  enumerate ( sr . Microphone . list_microphone_names ()): 
    print ( "Microphone with name \" {1} \ " encontrado para` Microphone (device_index = {0} ) `" . format ( index ,  nome ))