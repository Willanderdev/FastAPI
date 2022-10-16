from math import nextafter


Bandas = {
    2: {'Banda': "Angra",
        "músicos": ['Rafael', 'Kiko', 'Felipe Andreoli', 'Aquiles', 'Falaski'],
        "vertente": 'power metal'
        },
    3: {
        "Banda": "Almah",
        "músicos": ['Falaski', 'Felipe Andreoli', 'Marcelo Barbosa', 'Paulo', 'Aquiles'],
        "vertente": 'Power Metal'
    }
}


# next_id: int = Bandas[len(Bandas)] + 1
# Bandas[next_id] = banda
# banda.id = next_id
# return banda
next_id = [*Bandas]
next_id = next_id[len(next_id)-1]
next_id=next_id+1
print(next_id)