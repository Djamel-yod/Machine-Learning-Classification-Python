# Prédiction du désabonnement des client d'une société de télécommunication

![Mon image]('[https://miro.medium.com/max/844/1*MyKDLRda6yHGR_8kgVvckg.png](https://github.com/Djamel-yod/Prediction-Desabonnement-Clients/blob/main/Images/Image%20Mlflow.png)')

A travers ce projet, je renforce mes compétences en analyse exploratoire de données avec **python**, en développement de modèles de machine learning pour résoudre des problèmes métier concrets, en construction de pipeline de machine learning, en tracking des performances de modèles ML avec l'outil **Mlflow** et en déploiement de modèle de machine learning via une interface graphique web avec **streamlit**.

## Contexte: 
Le churn correspond au désabonnement d'un client à un service. Les entreprises adoptent souvent une approche classique pour contrer cette perte de clients : les remplacer ou les reconquérir. Cette stratégie implique des coûts importants et du temps : e-mailing, publicité, cadeaux, primes, etc. L'anticipation par l'approche prédictive permet d'éviter ces dépenses et de prévenir la perte de clients. Pourtant, Grace aux techniques d'apprentissage automatique, il est possible de développer des algorithmes possédants une grande précision à identifier les clients susceptibles de se désabonner d'un service et ainsi d'anticiper leur désabonnement en menant des actions marketing dans le but de maintenir les maintenir.

Dans ce projet, j'ai développé un algorithme de Machine Learning (Classification) qui permet de prédire avec une grande précision si un client lambda d'une société de téléphonie mobile est susceptible de se désabonner des services de la société ou non. J’ai utilisé une base de données de 7043 clients avec 14 variables mise à disposition par la multinationale américaine IBM https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113. Les types de données clients sont:

- Le genre (Homme ou Femme)
- L’âge (sénior ou non)
- La situation familiale (partenaire et/ou personnes à charge)
- L'ancienneté (durée de l'abonnement en mois)
- Les services souscrits (téléphonie, sécurité en ligne,accès internet )
- Le montant des charges mensuelles et totales
- Le type de contrat (mensuel, Annuel, etc)
- La méthode de paiement (Carte bancaire, chèque, etc)

## Méthodologie

J'ai effectué une analyse statistiques approfondis de ces données à travers une analyse exploratoire incluant des statistiques univariées et bivariées. J'ai ensuite construit des pipelines de Machine Learning afin d'automatiser le préprocessing et l'estimation des modèles. J’ai estimé sur les données quatre algorithmes de classifications que sont La **Régréssion Logistique**, Le **Support Vector Machine (SVM)**, le **Random Forest Classifier** et le **XGBoost Classifier**. Ces quatre algorithmes sont comparés et le plus performant est choisi. Pour le tracking des performances de mes modèles, j'utilise **MLflow**. Le meilleur modèle est déployé sur une application web streamlit exploitable via ce **lien**

## Résultats
Les visualisations et statistiques descriptives sont disponibles à travers le fichier notebook.ipynb et l'application web pour effectuer des simulations de prévisions à travers le **lien** 


<a href="#">#MachineLearning</a>
<a href="#">#Classification</a>
<a href="#">#Mlflow</a>
<a href="#">#Streamlit</a>

