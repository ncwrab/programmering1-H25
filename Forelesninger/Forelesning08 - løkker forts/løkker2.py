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

#------------------------------------#
# Vi ønsker å legge til spillene 'Pandemic Legacy: Season <tall> i spillisten vår dersom de ikke allerede finnes der.
# Oppretter først en variabel med første del av navnet:
pandemic_legacy_season = "Pandemic Legacy: Season"

# Løkke som først legger til sesongnummeret i en egen lokal variabel (pandemic_legacy)
# range(1, 4) vil ta med tallene 1, 2 og 3, men ikke 4 og over
for nummer_i_serien in range(1,4):
    pandemic_legacy = f"{pandemic_legacy_season} {nummer_i_serien}"
    # For hver iterasjon sjekker vi om gjeldende spill IKKE finnes i lista fra før
    # Dersom det ikke finnes (not in) skal vi legge det til bakerst i lista (med append() )
    if pandemic_legacy not in brettspill:
        brettspill.append(pandemic_legacy)
        print(f"Legger til {pandemic_legacy} i lista")

print("Vi skriver ut den nye lista:")
for spill in brettspill:
    print(spill)
## ---------------------------------------------##
# Vi legger til Monopol 3 ganger på slutten av lista, og skal så fjerne alle forekomster
# av Monopol ved hjelp av en while-løkke
brettspill.append("Monopol")
brettspill.append("Monopol")
brettspill.append("Monopol")

# Skriver ut lista før fjerning av Monopol
print(brettspill)

# Så lenge "Monopol" fins i lista skal løkka gå, og fjerne denne verdien ("Monopol"). Lista skrives ut for hver iterasjon av løkka.
while "Monopol" in brettspill:
    brettspill.remove("Monopol")
    print(brettspill)
