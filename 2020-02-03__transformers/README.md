# Faisons connaissance avec les Transformeurs : Bert, Albert, Roberta…

## Présentation

Une fois le dépôt git cloné (avec ses submodules) :

    git clone --recurse-submodules git@github.com:nantes-machine-learning-meetup/NMLM.git

Vous pouvez simplement ouvrir `index.html` dans votre navigateur préféré.

## Résumé

On ne parlera pas d'Optimus Prime dans ce meetup mais bien des dizaines de papiers sortis récemment qui poursuivent l'étude de l'approche décrite dans “Attention Is All You Need”, qui a introduit les transformeurs il y a plus de deux ans.

Ces modèles, qui traitent le cas crucial de l'apprentissage séquence à séquence, n'utilisent pas les réseaux récurrents mais plutôt des mécanismes d'attention.

Nous passerons en revue les différentes variantes et quelques papiers sympas liés à cette famille de modèles.

## Speaker

Hugo Mougard sort d'une aventure avec source{d} où il appliquait le Machine Learning sur du code pour créer des outils de développement et est maintenant freelance sur Nantes.

# Lecture

Si vous voulez vous plonger dans l'univers en très rapide expansion des transformeurs, voilà quelques papiers ou billets de blog à considérer :

- [papier] Attention is all you need https://arxiv.org/abs/1706.03762
- [blog] The illustrated transformer http://jalammar.github.io/illustrated-transformer/
- [blog] The Transformer – Attention is all you need. https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/
- [papier] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding https://arxiv.org/abs/1810.04805
- [papier] ALBERT: A Lite BERT for Self-supervised Learning of Language Representations https://arxiv.org/abs/1909.11942
- [blog] From BERT to ALBERT: Pre-trained Language Models https://medium.com/@hamdan.hussam/from-bert-to-albert-pre-trained-langaug-models-5865aa5c3762
- [papier] XLNet: Generalized Autoregressive Pretraining for Language Understanding https://arxiv.org/abs/1906.08237
- [papier] CamemBERT: a Tasty French Language Model https://arxiv.org/abs/1911.03894
- [papier] Universal Language Model Fine-tuning for Text Classification https://arxiv.org/abs/1801.06146
- [papier] Deep contextualized word representations https://arxiv.org/abs/1802.05365
- [papier] Language Models are Unsupervised Multitask Learners https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- [blog] Better Language Models
  and Their Implications https://openai.com/blog/better-language-models/
- [papier] Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context https://arxiv.org/abs/1901.02860
- [papier] RoBERTa: A Robustly Optimized BERT Pretraining Approach https://arxiv.org/abs/1907.11692
- [demo] https://talktotransformer.com/
