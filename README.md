
<p style="color: blue;"> Tp transaction</p> <br>

MAACHOU Abderazak <br>
GUENDOUL Massinissa <br>

 1 ere partie le commit <br>

On a crée une base de données et on a lancé une requête pour afficher la table module comme le montre cette première capture:<br>
![1](https://user-images.githubusercontent.com/75087496/100525626-95b4c280-31c2-11eb-9282-1d6063ab289a.PNG) <br>

Ensuite on a connecté notre base de données a python. <br>
En deuxième lieu on a écrit un code pour lancer une requête avec le commit pour apporter des changements à notre base de données <br>
La capture suivante représente le code réalisé.<br>
![3](https://user-images.githubusercontent.com/75087496/100525959-b716ae00-31c4-11eb-9b1a-c1107a73aaa9.PNG) <br>
Dans la requête précédente on a rajouté une ligne a notre base de données,la capture suivante nous montre les changements dans notre base de données. <br>
![2](https://user-images.githubusercontent.com/75087496/100526001-53d94b80-31c5-11eb-91f6-6779f9e733fc.PNG)<br>


2 eme partie rollback <br>

Cette deuxième partie est consacrée au rollback <br>
On a lancé une requête pour rajouter une autre ligne avec le rollback, comme le montre la capture suivante : <br>
![4](https://user-images.githubusercontent.com/75087496/100526415-0a8afb00-31c9-11eb-9bfd-75092fc0616f.PNG) <br>
On a remarqué que la requête n'a pas été exécuté comme on peut le voir sur cette capture : <br>
![5](https://user-images.githubusercontent.com/75087496/100526417-0e1e8200-31c9-11eb-9141-a245afdf3b99.PNG) <br>
On peut mème le vérrifier sur notre base de données en utilisant SQL server. <br>
![6](https://user-images.githubusercontent.com/75087496/100526526-ebd93400-31c9-11eb-9155-90ecb465a4a8.PNG) <br>

On voit bien que la ligne n'a pas été rajouté.

