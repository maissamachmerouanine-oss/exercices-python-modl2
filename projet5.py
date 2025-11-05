tasks = []
tasks.append('Faire les courses')
tasks.append('Aller à la gym')
tasks.append('Lire un livre')

#Affichage des Tâches
print('--- VOS TÂCHES ACTUELLES ---')
if not tasks:
    print('Vous n\'avez aucune tâche !')
else:
    for index, task in enumerate(tasks):
        print(f'{index + 1}. {task}')

#Finalisation d'une Tâche
completed_task = tasks.pop(0)
print(f'Tâche terminée : "{completed_task}"')
print('--- VOS TÂCHES ACTUELLES ---')
if not tasks:
    print('Vous n\'avez aucune tâche !')
else:
    for index, task in enumerate(tasks):
        print(f'{index + 1}. {task}')