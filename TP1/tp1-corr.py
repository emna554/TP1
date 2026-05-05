def calculer_valeur_stock(inventaire, prix_unitaires):
    total = 0
    indices = 0

    while indices < len(inventaire):
        produit = inventaire[indices]
        prix = prix_unitaires[produit.lower()]
        total += prix
        indices += 1

    return total

def main():
    mon_stock = ["Console", "Manette", "Jeu"]
    catalogue = {
        "console": 300,
        "manette": 50,
        "jeu": 60
    }
    print("Analyse du stock en cours...")
    resultat = calculer_valeur_stock(mon_stock, catalogue)
    print(f"Valeur totale du stock : {resultat}dt")

if __name__ == "__main__":
    main()