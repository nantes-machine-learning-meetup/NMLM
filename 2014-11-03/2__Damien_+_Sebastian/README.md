# TALN et ML

Présentation au meetup Présentation Machine Learning Nantes 2014

3 novembre 2014

par *Sebastián Peña Saldarriaga* et *Damien Raude-Morvan* de [Dictanova](http://www.dictanova.com)

## Abstract
   En partant d'une petite introduction sur des concepts basiques,
   nous essaieront de répondre à la question, que peuvent faire
   le TAL (traitement automatique des langues) et le ML (Machine Learning) pour moi ?

   A travers un retour d'expérience sur l'utilisation de ces outils dans le
   cadre d'un projet industriel, nous montreront les
   possibilités, les limites, et pourquoi il ne faut pas avoir peur de se
   lancer dans le ML.

   Si la théorie derrière le ML est complexe, son
   utilisation peut se révéler bénéfique et aisée à condition de se poser
   les bonnes questions par rapport au contexte applicatif visé.

## Reveal.js
Cette présentation utilise le framework [Reveal.js](https://github.com/hakimel/reveal.js).
Il permet d'utiliser un simple fichier HTML5 aggrémenter de quelques balises spécialisées pour obtenir un rendu graphique de bonne qualité.

## Afficher la présentation
Ce répertoire contient un [submodule git](http://git-scm.com/book/en/v2/Git-Tools-Submodules):
Ceci permet d'inclure un repository Git distant (en l'occurence reveal.js) comme un fragment du repository courrant.

1. Récupération des
```
git submodule init
git submodule update
```

NOTE: Si le flag `--recursive` n'est pas ajouter, vous ne ferez pas un clone du sous-module `reveal.js`

2. Ouvrir le fichier index.html
```
xdg-open index.html
```

