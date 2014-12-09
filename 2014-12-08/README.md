# Comment faire un crawl thématique efficacement dans un espace inconnu ?

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
[Hypertext 2014].

[Hypertext 2014]: http://ht.acm.org/ht2014/index.php?conference.accepted_papers

______________________________________________________________________________

Georges Gouriten est ingénieur de formation, il s’est lancé pleinement dans
l’informatique en 2011. Depuis, il a travaillé pendant quelques années au sein
de l’équipe [DBWeb] sur le projet européen d’archivage [arcomem] puis sur un
début de thèse.

Début 2014, il a arrêté son doctorat pour créer une société, [betasweets],
qui lance un site de rencontre pas comme les autres, [bisimila].

[DBWeb]: http://dbweb.enst.fr
[arcomem]: http://www.arcomem.eu/
[betasweets]: http://betasweets.com/
[bisimila]: http://bisimila.com/

______________________________________________________________________________

Cet évènement était organisé via [meetup] et la [cantine].

[cantine]: http://www.meetup.com/Nantes-Machine-Learning-Meetup/events/218699250/
[meetup]: http://cantine.atlantic2.org/evenements/nantes-machine-learning-meetup-2/
