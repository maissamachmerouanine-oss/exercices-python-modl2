produits= [
    ('p01', 'T-shirt', 19.99) 
    ('p02', 'pentalent', 20.50)
    ('p03', 'talent' , 45.20)
]
stock_levels= {
    'p01': 50,  #en stock
    'p02': 30,  
    'p03': 20   
}

product_id_to_sell = 'p01'
for pid, name, price in produits:
    if pid == product_id_to_sell:
        break  # Si on trouve le bon produit, on sort de la boucle

#Mettre à jour le niveau de stock
stock_levels[product_id_to_sell] -= 1

# Affichage de message de confirmation 
print(f"Vendu : {name} pour {price} €. Stock restant : {stock_levels[product_id_to_sell]}.")

print("--- RAPPORT D'INVENTAIRE ACTUEL ---")
#Parcourir la liste products
for pid, name, price in produits:
    stock_quantity = stock_levels[pid]
    print(f'ID: {pid} | Produit: {name} | Prix: {price} € | Stock: {stock_quantity}')
