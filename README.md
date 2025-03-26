# Prédiction du désabonnement des clients d'une société de télécommunication

**[Cliquez ici pour prédire si un client a une forte probabilité de se désabonner](https://prediction-desabonnement-clients-fcmdpzd8cappjh9hteynv3t.streamlit.app/)**
<img width="1000" alt="Capture_Churn" src="https://github.com/Djamel-yod/Prediction-Desabonnement-Clients/assets/60408184/7fa9156d-ef50-47e5-92cc-983140590cf9">


Dans le cadre de ce projet, j'ai utilisé **Python**, **Mlflow** et **Streamlit** pour construire un pipeline de machine learning complet, depuis l'exploration des données jusqu'à la mise en production et le suivi des performances.


## Contexte: 
Le churn correspond au désabonnement d'un client à un service. Les entreprises adoptent souvent une approche classique pour contrer cette perte de clients : les remplacer ou les reconquérir. Cette stratégie implique des coûts importants et du temps : e-mailings, publicités, cadeaux, primes, etc. L'anticipation par l'approche prédictive permet d'éviter ces dépenses et de prévenir la perte de clients. Grâce aux techniques d'apprentissage automatique, il est possible de développer des algorithmes possédant une grande précision à identifier les clients susceptibles de se désabonner d'un service et ainsi d'anticiper leur désabonnement en menant des actions marketing ciblées dans le but de les maintenir.

Dans ce projet, j'ai développé un algorithme de Machine Learning (Classification) qui permet de prédire avec une grande précision si un client lambda d'une société de téléphonie mobile est susceptible de se désabonner des services de la société ou non. J’ai utilisé une base de données de 7043 clients avec 14 variables mise à disposition par la multinationale américaine IBM https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113. Les types de données clients sont :

- Le genre (Homme ou Femme)
- L’âge (sénior ou non)
- La situation familiale (partenaire et/ou personnes à charge)
- L'ancienneté (durée de l'abonnement en mois)
- Les services souscrits (téléphonie, sécurité en ligne,accès internet )
- Le montant des charges mensuelles et totales
- Le type de contrat (mensuel, Annuel, etc)
- La méthode de paiement (Carte bancaire, chèque, etc)

## Méthodologie

J'ai effectué une analyse statistique approfondie de ces données à travers une analyse exploratoire incluant des statistiques univariées et bivariées. J'ai ensuite construit des pipelines de Machine Learning afin d'automatiser le préprocessing et l'estimation des modèles. J’ai estimé sur les données quatre algorithmes de classification que sont La **Régression Logistique**, Le **Support Vector Machine (SVM)**, le **Random Forest Classifier** et le **XGBoost Classifier**. Ces quatre algorithmes sont comparés et le plus performant est choisi. Pour le tracking des performances de mes modèles, j'utilise **MLflow**. Le meilleur modèle est déployé sur une application web streamlit.

## Résultats
Les visualisations et statistiques descriptives sont disponibles à travers le fichier notebook.ipynb et l'application web pour effectuer des simulations de prévisions est disponible à travers le 
**[lien](https://prediction-desabonnement-clients-fcmdpzd8cappjh9hteynv3t.streamlit.app/)**




## Outils

<img width="391" alt="Capture Python" src="https://github.com/user-attachments/assets/8cbf78c6-fce0-4c98-811b-4c9af951805b" />
<img width="623" alt="Capture Docker" src="https://github.com/user-attachments/assets/072544c4-eac0-4130-b2d6-1a4795689420" />
<img width="319" alt="Capture Mlflow" src="https://github.com/user-attachments/assets/c07005c0-ed9e-4a5b-a89a-d5c6431bccdd" />
<img width="354" alt="Capture Streamlit" src="https://github.com/user-attachments/assets/4811e4e3-bef4-4a1b-bf55-908fe2abb8c0" />

<a href="#">#MachineLearning</a>
<a href="#">#Classification</a>
<a href="#">#Mlflow</a>
<a href="#">#Streamlit</a>

