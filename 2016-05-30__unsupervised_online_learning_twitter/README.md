# Unsupervised and Online Learning - Twitter API usecase

## Résumé

L'apprentissage statistique (statistical learning) est à l'origine de nombreux algorithmes de prédiction/classification/clustering ces 30 dernières années (Linear Regression, SVM, Random Forest, k-means).  Le principe de ce genre d'algorithmes est le suivant : à partir d'un jeu de données d'apprentissage (training set), l'algorithme construit sa décision (classifieur, prédicteur, ...).

Dans cet exposé, nous aborderons une autre type d'apprentissage appelée apprentissage en ligne (online learning), qui donne lieu à un nouveau type d'algorithmes capable de réagir en temps réel à un flux de données.  Nous explorerons en particulier un problème assez peu traité mais très intéressant d'un point de vue pratique : l'apprentissage en ligne non-supervisée (online clustering) avec une partie pratique (notebook python) sur un usecase "sentiment analysis from Twitter API". 

## Bio

Sébastien Loustau a travaillé dix ans à l'université comme chercheur en machine learning.  Il vient de créer artfact (twitter : @artfact64), jeune pousse innovante qui conçoit des algorithmes d'aide à la décision en temps réel.

## Lecture

Ulrike von Luxburg, Robert C. Williamson, Isabelle Guyon, Clustering: Science or Art, JMLR: Workshop and Conference Proceedings (Workshop on Unsupervised and Transfer Learning) 27:65-79, 2012.  [pdf](http://www.jmlr.org/proceedings/papers/v27/luxburg12a/luxburg12a.pdf)

We  examine  whether  the  quality  of  di erent  clustering  algorithms  can  be  compared  by a general, scienti cally sound procedure which is independent of particular clustering algorithms.  We  argue  that  the  major  obstacle  is  the  di culty  in  evaluating  a  clustering algorithm without taking into account the context:  why does the user cluster his data in the  rst place, and what does he want to do with the clustering afterwards?  We argue that clustering should not be treated as an application-independent mathematical problem, but should  always  be  studied  in  the  context  of  its  end-use.  Di erent  techniques  to  evaluate clustering algorithms have to be developed for di erent uses of clustering.  To simplify this procedure  we  argue  that  it  will  be  useful  to  build  a  taxonomy  of  clustering  problems"
to identify clustering applications which can be treated in a uni ed way and that such an e ort will be more fruitful than attempting the impossible developing optimal" domain-
independent clustering algorithms or even classifying clustering algorithms in terms of how they work.

Breiman, Leo. _Statistical Modeling: The Two Cultures_ (with comments and a rejoinder by the author). Statist. Sci. 16 (2001), no. 3, 199--231. doi:10.1214/ss/1009213726. http://projecteuclid.org/euclid.ss/1009213726. ; [page avec pdf](https://projecteuclid.org/euclid.ss/1009213726#abstract)

There are two cultures in the use of statistical modeling to reach conclusions from data. One assumes that the data are generated by a given stochastic data model. The other uses algorithmic models and treats the data mechanism as unknown. The statistical community has been committed to the almost exclusive use of data models. This commitment has led to irrelevant theory, questionable conclusions, and has kept statisticians from working on a large range of interesting current problems. Algorithmic modeling, both in theory and practice, has developed rapidly in fields outside statistics. It can be used both on large complex data sets and as a more accurate and informative alternative to data modeling on smaller data sets. If our goal as a field is to use data to solve problems, then we need to move away from exclusive dependence on data models and adopt a more diverse set of tools.

(Approfondi, 403 pages, présence de maths)

Nicolò Cesa-Bianchi, Gábor Lugosi, Prediction, Learning, and Games, Cambridge University Press, 2006.  [pdf](http://www.ii.uni.wroc.pl/~lukstafi/pmwiki/uploads/AGT/Prediction_Learning_and_Games.pdf)

## Video

[ici](https://youtu.be/_K1J8vskn00)
