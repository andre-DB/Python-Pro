meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "HATER": "Persona que se dedica a difamar o criticar negativamente.",
            "ANGRY" : "Estado de estar enojado por tener hambre."
            }


for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    
    else:
        print("Esa palabra no está en el diccionario.")
