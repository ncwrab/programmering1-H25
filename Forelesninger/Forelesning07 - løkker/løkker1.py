# Oppretter en liste med forskjellige brettspill:
brettspill = ["Ubongo", "Pandemic", "Ludo", "Monopol", "Mysterium", "Ludo"]

# Går gjennom hvert element i listen og skriver ut elementet i en passende utskrift.
# Merk at 'spill' kan ses på som en lokal variabel som kun er tilgjengelig i for-løkken. Praktisk talt vil
# 'spill' fungere som en referanse til et gitt element for en gitt iterasjon i løkken
# 'spill' kan hete hva som helst, men det er lurt å ha et beskrivende navn.
for spill in brettspill:
    print(f"{spill} er et bra spill!") # spill vil ha en unik verdi for hver iterasjon i løkken (for hvert element i listen)
    #print("2 er et fint tall")        # Fjern '#' foran print, så vil du se at denne utskriften kommer med i hver iterasjon av løkka

# Itererer gjennom hver bokstav i en tekststreng og skriver den ut
for bokstav in "Risk":
    print(bokstav)

# Løkken under vil gi lik utskrift som den over, men her har vi lagt tekststrengen i en variabel istedenfor å hardkode den i løkka:
tekst = "Risk"
for bokstav in tekst:
    print(bokstav)

# Merk forskjellen mellom de to utskriftene under (man må være obs på hva man itererer gjennom med en løkke):

print(brettspill)            # brettspill peker til hele listen
print(brettspill[0])         # brettspill[0] peker bare til første element i listen (som vil fungere i en løkke siden tegnene i en string har hver sin indeks også)
