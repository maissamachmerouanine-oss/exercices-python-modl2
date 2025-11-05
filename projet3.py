contact_numbers=[]
contact_numbers=['0612345678', '0787654321', '0612345678']
print("liste originale:", contact_numbers)
print("nombre de contact:", len(contact_numbers))
unique_contacts_set = set(contact_numbers)
unique_contacts_list= list(unique_contacts_set)
unique_contacts_list.sort()

print("liste des contactes unique triée:", unique_contacts_list)
print('--- RAPPORT DE NETTOYAGE DES CONTACTS ---')
nombre_de_contact_endoubles =len(contact_numbers) - len(unique_contacts_list)
print("nombre de doublon trouvé :", nombre_de_contact_endoubles)
print("liste de contacte finale(propre et trié:)", unique_contacts_list)
print("nouveau nombre de contacts uniques:", len(unique_contacts_list))