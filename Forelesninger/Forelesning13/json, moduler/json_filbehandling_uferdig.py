
# Dette er 'programmet' vårt. Vi importerer modulen vi laget, jsonmodul.py, og bruker funksjonene vi definerte der.

import jsonmodul


# Lager en dictionary, som vi ønsker å skrive til en json-fil senere
planet = {"navn" : "Merkur", "tyngdekraft" : 3.73}

# Lagrer filnavnet vi ønsker å bruke i en variabel
file_name = "planet.json"

# Bruker skriv_json()-funksjonen vi definerte i vår jsonmodul, og sender med variablene vi akkurat opprettt som argumenter
# Vi får nå opprettet en ny fil med navnet planet.json, og som inneholder en string med vår dictionary 
jsonmodul.skriv_json(planet, file_name)
