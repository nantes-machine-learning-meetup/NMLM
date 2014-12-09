Comment crawler efficacement un espace inconnu ?

Imaginez que vous vouliez récupérer toutes les pages du Web parlant de Lara
Fabian, comment les trouver au milieu d’une masse de pages ne parlant pas de
Lara Fabian ?

Nous nous intéresserons tout d’abord à la formalisation de ce problème à
l’aide de graphes.

Nous étudierons ensuite les techniques d’apprentissage qui permettent de
faciliter l’exploration d’un graphe, dans un contexte où les nœuds sont
découverts un à un, et où le nombre total de nœuds que l’on peut explorer est
contraint.

La présentation est issue de l’article de recherche « Scalable, Generic, and
Adaptive Systems for Focused Crawling » présenté lors de la conférence
Hypertext 2014[0].

[0] http://ht.acm.org/ht2014/index.php?conference.accepted_papers

______________________________________________________________________________

Georges Gouriten est ingénieur de formation, il s’est lancé pleinement dans
l’informatique en 2011. Depuis, il a travaillé pendant quelques années au sein
de l’équipe DBWeb[0] sur le projet européen d’archivage arcomem[1] puis sur un
début de thèse.

Début 2014, il a arrêté son doctorat pour créer une société, betasweets[2],
qui lance un site de rencontre pas comme les autres, bisimila[3].

[0] http://dbweb.enst.fr
[1] http://www.arcomem.eu/
[2] http://betasweets.com/
[3] http://bisimila.com/

______________________________________________________________________________

Cet évènement était organisé via meetup[0] et la cantine[1].

[0]: http://www.meetup.com/Nantes-Machine-Learning-Meetup/events/218699250/
[1]: http://cantine.atlantic2.org/evenements/nantes-machine-learning-meetup-2/
