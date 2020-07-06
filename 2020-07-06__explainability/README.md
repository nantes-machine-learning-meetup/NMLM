# Explainability; Human-driven deep learning

Gabriele Ciravegna and Nicola Picchiotti (University of Siena) will
talk about explainability and human driven FOL explanations of deep
learning and some other current research of theirs. The evening will
be divided into two talks of roughly a half hour each.

## Resume (Nicola) :

In the foreseeable future, a fundamental challenge of Artificial
Intelligence will be the need to explain, in a human-comprehensible
manner, the working of a black-box model. In fact, it has been shown
that this interpretability requirement is strongly connected with the
more general concept of model trustworthiness, particularly crucial
for high-stakes applications like diagnostic techniques, autonomous
guide, etc. There are currently many different approaches to tackle
the explainability problem; the talk provides both a review of general
interpretability concepts and a discussion of the mathematical
framework for the popular approaches exploited by the scientific
community i.e. LIME, SHAP, etc. The ultimate goal is trying to
establish a link between explainability and trustworthiness, for
instance by including the notion of feature importance in the
mathematical design of the Machine Learning model.

## Resume (Gabriele) :

### Human-Driven FOL Explanations of Deep Learning

Deep neural networks are usually considered black-boxes due to their
complex internal architecture, that cannot straightforwardly provide
human-understandable explanations on how they behave. Indeed, Deep
Learning is still viewed with skepticism in those real-world domains
in which incorrect predictions may produce critical effects. This is
one of the reasons why in the last few years Explainable Artificial
Intelligence (XAI) techniques have gained a lot of attention in the
scientific community.

In this work, we focus on the case of multi-label classification,
proposing a neural network that learns the relationships among the
predictors associated to each class, yielding First-Order Logic
(FOL)-based descriptions. Both the explanation-related network and the
classification-related network are jointly learned, thus implicitly
introducing a latent dependency between the development of the
explanation mechanism and the development of the classifiers. Our
model can integrate human-driven preferences that guide the
learning-to-explain process, and it is presented in a unified
framework. Different typologies of explanations are evaluated in
distinct experiments, showing that the proposed approach discovers new
knowledge and can improve the classifier performance.

## Bio :

Nicola Picchiotti is a second-year Executive Ph.D. student in
"Computational mathematics and decision sciences" at the University of
Pavia under the external supervision of professor Marco Gori. Nicola
holds a master’s degree in physics and works as a senior quantitative
analyst in the Internal validation team of "Banco BPM" Bank, where he
applies both statistical and advanced machine learning techniques on
real data coming from finance. The main objective of his research is
to make machine learning models more explainable and more reliable for
business applications.

Gabriele Ciravegna is a PhD student at the University of Siena since
2018 under the supervision of professor Marco Gori. In 2018 he
received the master’s degree in Computer Engineering at the
Polytechnic University of Turin. He focuses on overcoming the
intrinsic limits of machine learning and neural networks, above all
understandability.

Reading:

* Interpretable Machine Learning https://christophm.github.io/interpretable-ml-book/
* Guidotti, Riccardo, et al. "A survey of methods for explaining black box models." ACM computing surveys (CSUR) 51.5 (2018): 1-42. https://kdd.isti.cnr.it/sites/kdd.isti.cnr.it/files/csur2018survey.pdf
* Marco Tulio Ribeiro, et al. “Why Should I Trust You?” Explaining the Predictions of Any Classifier https://arxiv.org/pdf/1602.04938.pdf

* https://www.aaai.org/Papers/AAAI/2020GB/AAAI-CiravegnaG.4997.pdf
