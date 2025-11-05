post_text="J'adore #Python ! C'est le meilleur langage. Suivez @python_dev pour plus de conseils."
post_lower=post_text.lower() 
word_list=post_lower.split()
hashtag=['#python']
mentions=['@python_dev']

for word in word_list:  
    if word.startswith('#'):  
        hashtag.append(word) 

for word in word_list:
    if word.startswith('@'):
        mentions.append(word)
                  
nombre_total_de_mots=len(word_list)

print("hashtag:", hashtag)
print("mentions:", mentions)
print("nombre total de mots" , nombre_total_de_mots )
 
print("---RAPPORT D'ANALYSE DE PUBLICATION---")
print("nombre totale de mots :" , nombre_total_de_mots)
 #afficher les hashtags 
if hashtag:
    print("hashtags:" ,','.join(hashtag))
else:
    print("aucun hashtag trouvé")
#afficher les mentions 
if mentions:
   print("mentions:",','.join(mentions))
       