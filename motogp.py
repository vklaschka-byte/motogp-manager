def main():
    print("--- 🏍️ MotoGP RACE MANAGER 🏍️ ---")
    
    okruhy = {
        "brno": {
            "nazev": "Automotodrom Brno",
            "stat": "🇨🇿 Česká republika",
            "delka_m": 5403,
            "rekord_kola": "1:55.687"
        },
        "jerez": {
            "nazev": "Circuito de Jerez",
            "stat": "🇪🇸 Španělsko",
            "delka_m": 4423,
            "rekord_kola": "1:36.170"
        },
        "mugello": {
            "nazev": "Autodromo del Mugello",
            "stat": "🇮🇹 Itálie",
            "delka_m": 5245,
            "rekord_kola": "1:45.187"
        },
        "assen": {
            "nazev": "TT Circuit Assen",
            "stat": "🇳🇱 Nizozemsko",
            "delka_m": 4542,
            "rekord_kola": "1:31.504"
        }
    }

    while True:
        print("\nDOSTUPNÉ OKRUHY:")
        for klic in okruhy.keys():
            print(f"- {klic}")

        print("-" * 30)
        vyber = input("Zadej jméno okruhu (nebo 'konec'): ").lower().strip()

        if vyber == "konec":
            print("🏁 Ukončuji závodní systém. Ahoj!")
            break

        if vyber in okruhy:
            data = okruhy[vyber] 
            
            print(f"\n📍 {data['nazev']} ({data['stat']})")
            print(f"📏 Délka: {data['delka_m']} metrů")
            print(f"⏱️ Rekord kola: {data['rekord_kola']}")
            
            print("\n--- Telemetrie ---")
            odpoved = input("Chceš spočítat průměrnou rychlost? (ano/ne): ")
            
            if odpoved == "ano":
                cas_str = input("Zadej čas na kolo v sekundách (např. 115.5): ")
                try:
                    cas_sekundy = float(cas_str)
                    rychlost_kmh = (data['delka_m'] / cas_sekundy) * 3.6
                    
                    print(f"🚀 Průměrná rychlost jezdce: {rychlost_kmh:.2f} km/h")
                except ValueError:
                    print("❌ Chyba: Musíš zadat číslo (pro desetinné číslo použij tečku).")

        else:
            print(f"❌ Okruh '{vyber}' v databázi nemám. Zkus to znovu.")

if __name__ == "__main__":
    main()