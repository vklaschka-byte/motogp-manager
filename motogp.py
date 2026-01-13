import json
import os

SOUBOR_DATA = "okruhy.json"

def nacist_data():
    """Načte data ze souboru. Pokud soubor neexistuje, vytvoří základní data."""
    if not os.path.exists(SOUBOR_DATA):
        zakladni_okruhy = {
            "brno": {"nazev": "Automotodrom Brno", "stat": "🇨🇿 ČR", "delka_m": 5403, "rekord_kola": "1:55.687"},
            "jerez": {"nazev": "Circuito de Jerez", "stat": "🇪🇸 Španělsko", "delka_m": 4423, "rekord_kola": "1:36.170"}
        }
        ulozit_data(zakladni_okruhy)
        return zakladni_okruhy
    else:
        with open(SOUBOR_DATA, "r", encoding="utf-8") as f:
            return json.load(f)

def ulozit_data(data):
    """Uloží aktuální slovník do souboru JSON."""
    with open(SOUBOR_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    print("--- 🏍️ MotoGP MANAGER 2.0 (S pamětí) 🏍️ ---")
    
    okruhy = nacist_data()
    print(f"✅ Načteno {len(okruhy)} okruhů.")

    while True:
        print("\nCO CHCEŠ UDĚLAT?")
        print("1. 🔍 Hledat okruh")
        print("2. ➕ Přidat nový okruh")
        print("3. 🏁 Konec")
        
        volba = input("Vyber (1-3): ")

        if volba == "3":
            break
        
        elif volba == "1":
            print("\nDOSTUPNÉ OKRUHY: " + ", ".join(okruhy.keys()))
            vyber = input("Zadej jméno okruhu: ").lower().strip()
            
            if vyber in okruhy:
                data = okruhy[vyber]
                print(f"\n📍 {data['nazev']} ({data['stat']})")
                print(f"📏 Délka: {data['delka_m']} m | ⏱️ Rekord: {data['rekord_kola']}")
            else:
                print("❌ Tento okruh neznám.")

        elif volba == "2":
            print("\n--- PŘIDÁNÍ NOVÉHO OKRUHU ---")
            klic = input("Zadej krátké jméno (bez mezer, např. 'katar'): ").lower().strip()
            
            if klic in okruhy:
                print("⚠️ Tento okruh už existuje!")
            else:
                nazev = input("Celý název okruhu: ")
                stat = input("Stát (i s vlaječkou): ")
                delka = int(input("Délka v metrech: "))
                rekord = input("Rekord kola (např. 1:53.00): ")
                okruhy[klic] = {
                    "nazev": nazev,
                    "stat": stat,
                    "delka_m": delka,
                    "rekord_kola": rekord
                }
                
                ulozit_data(okruhy)
                print("✅ Uloženo! Okruh je v databázi.")

if __name__ == "__main__":
    main()