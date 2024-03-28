import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Image Background de mon appli

# URL de l'image
page_bg_img = '''
<style>
body {
background-image:url("https://images.unsplash.com/photo-1462206092226-f46025ffe607?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1353&q=80")
;
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Charger le modèle pickle
model = pickle.load(open("model.pkl", "rb"))

# Titre de l'application
st.title("Prédiction de la résiliation de contrat des abonnées d'une société de télécommunication")
st.subheader('Auteur: Ismael YODA')
st.write("Cette application est destinée a prédire si un client d'une société de télécommunication est susceptible de résilier son contract ou non en utilisant un algorithme de Machine Learning qui offre une grande présicion. Elle prend en entrées certaines données sur l'abonné(e) et renvoie en sortie la classe de l'abonné(e)(S'il est susceptible de résilier ou pas son contrat).")
st.write("Entrez les informations du client ou de la cliente pour prédire s'il(elle) a une grande probabilité de résilier son contrat")

col1, col2 = st.columns(2)

# Fonction de prédiction
def predict_churn(gender, SeniorCitizen, Partner, Dependents, tenure,
       PhoneService, OnlineSecurity, PaperlessBilling, MonthlyCharges,
       TotalCharges, InternetService_Fiber_optic,
       InternetService_No, Contract_One_year, Contract_Two_year,
       PaymentMethod_Credit_card_automatic,
       PaymentMethod_Electronic_check, PaymentMethod_Mailed_check):
    
    new_data = [[
                gender, SeniorCitizen, Partner, Dependents, tenure,
                PhoneService, OnlineSecurity, PaperlessBilling, MonthlyCharges,
                TotalCharges, InternetService_Fiber_optic,
                InternetService_No, Contract_One_year, Contract_Two_year,
                PaymentMethod_Credit_card_automatic,
                PaymentMethod_Electronic_check, PaymentMethod_Mailed_check
    ]]


    colonnes=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'OnlineSecurity', 'PaperlessBilling', 'MonthlyCharges',
       'TotalCharges', 'InternetService_Fiber optic',
       'InternetService_No', 'Contract_One year', 'Contract_Two year',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']
    new_data = pd.DataFrame(new_data, columns=colonnes)

    prediction = model.predict(new_data)
    return prediction

# Formulaire pour saisir les données d'entrée
with col1:
   gender = st.selectbox("Genre de l'abonné(e)", options=["Homme", "Femme"])
   SeniorCitizen = st.selectbox("Est-il(elle) sénior ?", options=["Oui", "Non"])
   Partner = st.selectbox("A t-il(elle) un(e) compagnon ?", options=["Oui", "Non"])
   Dependents=st.selectbox("A t-il(elle) des personnes à sa charge ?", options=["Oui", "Non"])
   tenure = st.number_input("Depuis combien de mois est-il(elle) abonné(e) ?", min_value=0)
   PhoneService=st.selectbox("Est-il(elle) abonné(e) au service de téléphonie résidentielle ?", options=["Oui", "Non"])
   InternetService = st.selectbox("A quel type de forfait internet a t-il(elle) souscrit ? Choisissez 'Non' s'il(elle) n'a souscrit a aucun forfait: ",options=["Non", "DSL", "Fibre Optique", "Câble"])



with col2:
   OnlineSecurity=st.selectbox("A t-il(elle) souscrit à un service de sécurité en ligne ?", options=["Oui", "Non"])
   Contract=st.selectbox("Quel est le type de contract ?: ",options=["Mensuel", "Annuel", "Biannuel"])
   PaperlessBilling= st.selectbox("A t-il(elle) choisi la facturation dématérialisée ?", options=["Oui", "Non"])
   PaymentMethod=st.selectbox("Quel est la méthode de payement utilisée ?: ", options=["Chèque électronique", "Chèque postal", "Retrait bancaire", "Carte de crédit"])
   MonthlyCharges=st.number_input("Quel est le montant mensuel en dollars $ de ses charges ?",step=1.,format="%.2f")
   TotalCharges=np.sqrt(st.number_input("Quel est le montant de ses charges totales en dollars$ depuis le début de son abonnement ?",step=1.,format="%.2f"))
   
# Convertion des variables catégorielles en entrées compris par le modèle
gender = "Male" if gender == "Homme" else "Female"
SeniorCitizen = "Yes" if SeniorCitizen == "Oui" else "No"
Partner = "Yes" if Partner == "Oui" else "No"
Dependents = "Yes" if Dependents == "Oui" else "No"
Partner = "Yes" if Partner == "Oui" else "No"
PhoneService = "Yes" if PhoneService == "Oui" else "No"
OnlineSecurity = "Yes" if OnlineSecurity == "Oui" else "No"
PaperlessBilling = "Yes" if PaperlessBilling == "Oui" else "No"


InternetService_Fiber_optic="Yes" if InternetService=="Fibre Optique" else "No"
InternetService_No= "Yes" if InternetService=="Non" else "No"
Contract_One_year= "Yes" if Contract=="Annuel" else "No"
Contract_Two_year= "Yes" if Contract=="Biannuel" else "No"
PaymentMethod_Credit_card_automatic="Yes" if PaymentMethod=="Carte de crédit" else "No"
PaymentMethod_Electronic_check= "Yes" if PaymentMethod=="Chèque électronique" else "No"
PaymentMethod_Mailed_check= "Yes" if PaymentMethod=="Chèque postal" else "No"


# Bouton pour effectuer la prédiction
if st.button('Prédire'):
   predictions = predict_churn(gender, SeniorCitizen, Partner, Dependents, tenure,
       PhoneService, OnlineSecurity, PaperlessBilling, MonthlyCharges,
       TotalCharges, InternetService_Fiber_optic,
       InternetService_No, Contract_One_year, Contract_Two_year,
       PaymentMethod_Credit_card_automatic,
       PaymentMethod_Electronic_check, PaymentMethod_Mailed_check)
   
   churn_label = predictions[0]

   if churn_label == 1:
      st.success("Le client a une forte probabilité de résilier son contrat.")
   else:
      st.success("Le client (cliente) a une forte probabilité de rester abonné(e).")
      


