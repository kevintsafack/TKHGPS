import streamlit as st
from database import *
import pandas as pd
import sqlite3
import streamlit as st
from base import *
from base_1 import *
from dataset import DataSet
from dataset import Uplaodss
from Filtrage import *
from distance import *
from vitesse import *
from temps_mis import *
from graph import *
import json
from streamlit_lottie import st_lottie
import numpy as np
import altair as alt
import io
buffer = io.BytesIO()
from streamlit_option_menu import option_menu 

########Calcul de l'horaire d'une journée ##############♦
def c_h(t):
    h=[0]
    y=0
    for i in range(len(t)):
        if t[i].isnumeric():
            y=y+1
        else:
            h.append(i)
    
    return round(int(t[h[0]:h[1]]) + (int(t[h[1]+1:h[2]])/60) + int(t[h[2]+1:])/3600 , 3)
######### GRAPH ET TELECHARGEMENT #################################
def GRAPHD(options):
    try:
        if len(options)==1:
            #Distence
            Graph([ Gra_J(options[0]).DJ_D() ]).graph()[0]
            Graph([ Gra_J(options[0]).DS_D() ]).graph()[0]
            Graph([ Gra_J(options[0]).DM_D() ]).graph()[0]
            
        else:
            f_0 = []
            f_1 = []
            f_2 = []
            for i in range(len(options)):
                #Distance
                f_0.append(Gra_J(options[i]).DJ_D())
                f_1.append(Gra_J(options[i]).DS_D())
                f_2.append(Gra_J(options[i]).DM_D())
            Graph(f_0).graph()[0]
            Graph(f_1).graph()[0]
            Graph(f_2).graph()[0]
        
    except:
        pass
    
def F11(options):
        j = []
        s = []
        m = []
        if len(options)==1:
            j.append(File(Graph([ Gra_J(options[0]).DJ_D() ]).graph()[1]).file())
            s.append(File(Graph([ Gra_J(options[0]).DS_D() ]).graph()[1]).file())
            m.append(File(Graph([ Gra_J(options[0]).DM_D() ]).graph()[1]).file())
            
        else:
            f_0 = []
            f_1 = []
            f_2 = []
            for i in range(len(options)):
                #Distance
                f_0.append(Gra_J(options[i]).DJ_D())
                f_1.append(Gra_J(options[i]).DS_D())
                f_2.append(Gra_J(options[i]).DM_D())
            j.append(File(Graph(f_0).graph()[1]).file())
            s.append(File(Graph(f_1).graph()[1]).file())
            m.append(File(Graph(f_2).graph()[1]).file())
        
        
        return j,s,m

def GRAPHTM(options):
    try:
        if len(options)==1:
            #Temps M
            GraphTime([GTM_J(options[0]).TMJ_D()]).graph()[0]
            GraphTime([GTM_J(options[0]).TMS_D()]).graph()[0]
            GraphTime([GTM_J(options[0]).TMM_D()]).graph()[0]
            
        else:
            g_0 = []
            g_1 = []
            g_2 = []
            for i in range(len(options)):
                #Temps M
                g_0.append(GTM_J(options[i]).TMJ_D())
                g_1.append(GTM_J(options[i]).TMS_D())
                g_2.append(GTM_J(options[i]).TMM_D())
            
            GraphTime(g_0).graph()[0]
            GraphTime(g_1).graph()[0]
            GraphTime(g_2).graph()[0]
    except:
        pass

def F22(options):
        j = []
        s = []
        m = []
        if len(options)==1:
            j.append(File(GraphTime([GTM_J(options[0]).TMJ_D()]).graph()[1]).file())
            s.append(File(GraphTime([GTM_J(options[0]).TMS_D()]).graph()[1]).file())
            m.append(File(GraphTime([GTM_J(options[0]).TMM_D()]).graph()[1]).file())
        else:
            g_0 = []
            g_1 = []
            g_2 = []
            for i in range(len(options)):
                #Temps M
                g_0.append(GTM_J(options[i]).TMJ_D())
                g_1.append(GTM_J(options[i]).TMS_D())
                g_2.append(GTM_J(options[i]).TMM_D())
            j.append(File(GraphTime(g_0).graph()[1]).file())
            s.append(File(GraphTime(g_1).graph()[1]).file())
            m.append(File(GraphTime(g_2).graph()[1]).file())
        return j,s,m

def GRAPHTIM(options):
    try:
        if len(options)==1:
            #Temps IM
            GraphTime([GTIM_J(options[0]).TMJ_D()]).graph()[0]
            GraphTime([GTIM_J(options[0]).TMS_D()]).graph()[0]
            GraphTime([GTIM_J(options[0]).TMM_D()]).graph()[0]
            
        else:
            gi_0 = []
            gi_1 = []
            gi_2 = []
            for i in range(len(options)):
                #Temps IM
                gi_0.append(GTIM_J(options[i]).TMJ_D())
                gi_1.append(GTIM_J(options[i]).TMS_D())
                gi_2.append(GTIM_J(options[i]).TMM_D())
            
            GraphTime(gi_0).graph()[0]
            GraphTime(gi_1).graph()[0]
            GraphTime(gi_2).graph()[0]
    except:
        pass

def F33(options):
        j = []
        s = []
        m = []
        if len(options)==1:
            j.append(File(GraphTime([GTIM_J(options[0]).TMJ_D()]).graph()[1]).file())
            s.append(File(GraphTime([GTIM_J(options[0]).TMS_D()]).graph()[1]).file())
            m.append(File(GraphTime([GTIM_J(options[0]).TMM_D()]).graph()[1]).file())
        else:
            g_0 = []
            g_1 = []
            g_2 = []
            for i in range(len(options)):
                #Temps M
                g_0.append(GTIM_J(options[i]).TMJ_D())
                g_1.append(GTIM_J(options[i]).TMS_D())
                g_2.append(GTIM_J(options[i]).TMM_D())
            j.append(File(GraphTime(g_0).graph()[1]).file())
            s.append(File(GraphTime(g_1).graph()[1]).file())
            m.append(File(GraphTime(g_2).graph()[1]).file())
        return j,s,m




st.set_page_config(page_title="TKHGPS.io__V_:_1.5",page_icon="📐",layout="wide")

if 'key' not in st.session_state:
    st.session_state.key = 'value'

################# CACHER des elements ##################
#.css-10xlvwk, .css-fblp2m  == sidebar
#.css-18ni7ap == bare de haut
#.css-1q1n0ol == barre d'en bas
#.css-1v3fvcr == fond d'ecran
st.markdown("""
        <style>  
        ..css-fblp2m {display: none}
        ..css-10xlvwk {display: none}
        .css-18ni7ap {display: none}
        .css-1q1n0ol {display: none}
        ..css-1n76uvr {display: none}
        .css-qri22k {display: none}
        </style>
        """, unsafe_allow_html=True) 
Image('i9.png','.css-1v3fvcr').background()
Image('i5.jpg','.css-10xlvwk').background()
#######################################################


############################ LOGIN ##############################################

st.sidebar.title("SE CONNECTER")

username_1 = st.sidebar.text_input("Entrez votre nom d'utilisateur  ")

try:
    if (len(username_1)>1) & (Super_1.idp(username_1)>0)  :
        
        st.markdown("""
                <style>  
                .css-1cpxqw2 {display: none}
                </style>
                """, unsafe_allow_html=True)
        
        if Database('example.db').user_exist_with(username_1):
            st.sidebar.write("Mr "+ username_1 + " est identifier")
            password = st.sidebar.text_input("Entrez votre mot de pass  ", type="password")
            st.session_state.key = password
            boutton_2 = st.sidebar.button("Se connecter ")
            h=0
            if (boutton_2) :
                if (Super_1.login(username_1,password) ==1):
                    Super_1.update(username_1,0)
                else:
                    st.sidebar.write("Mot de pass incorrect")
    
                    
except:
    if len(username_1)>1:
        st.sidebar.header("Profitez du compte démo")
        st.sidebar.header("nom = demo")
        st.sidebar.header("mot de pass = demo")
        st.sidebar.header("Vous ne disposez pas de compte, et avez la possibilté d'en ouvrir un")
        st.sidebar.header("Crée un mot de pass")
        password = st.sidebar.text_input(" ", type="password")
        st.sidebar.header("Numéro correct ***")
        Numéro = st.sidebar.text_input("  ")
        
        st.sidebar.header("E-Mail correcte ***")
        mail = st.sidebar.text_input("   ")
        
        boutton_3 = st.sidebar.button("S'enregistrez ")
        if (len(password)!=0) & boutton_3:
            Database('example.db').create(username_1, password,1,Numéro,mail)
            st.sidebar.success("Compte creé avec succes")
        
        


try:
    if ((Super_1.idp(username_1))==0) & (Super_1.login(username_1,st.session_state.key) ==1):
                    h=1            
                    st.markdown("""
                            <style>  
                            .css-1cpxqw2 {display: flex}
                            </style>
                            """, unsafe_allow_html=True)
                    st.markdown("""
                            <style>  
                            .css-10xlvwk {display: none}
                            </style>
                            """, unsafe_allow_html=True)
                    Image('i3_1.jpg','.css-1v3fvcr').background()
                    ######################## ESPACE DE TRAVAIL ##################################
                    st.title("TKHGPS vous souhaite la bienvenue  "+username_1)
                    user= username_1
                    Super.user(user) # CREATION DE LA LISTE DES VOITURES
                    tab1, tab2, tab3 , tab4 , tab5 , tab6 = st.tabs(["Présentation 🎁" , " Bureau 💻 ⚙️" , "Distances 🚘 📊" , "Temps ⌚ 📊" , "Téléchargement 📤" , "Déconnexion 🚪" ])
                    with tab1:
                        
                        if username_1 == 'tsafack_kevin_root':
                            st.header("TABLEAU DE BORD")
                            table = Super.printt()
                            st.subheader("Nombre d'utilisateurs : " + str(len(table)))
                            st.write(table)
                            
                            T = Super.infos()
                            for i in range(len(T)):
                                st.write(T[i][0])
                                st.write(T[i][1])
                            coll , colll = st.columns(2)
                            with coll:
                                st.subheader("Suprimer un utilisateur")
                                nom = st.selectbox("Choisir l'utilisateur", Super.infos_1())
                                sup = st.button("Suprimer")
                                if sup:
                                    Super.delet(nom)
                                    st.success("Le compte a été suprimé avec suscces")
                            
                        else:
                            st.header("Presentation 🎁")
                            st.subheader("TKHGPS est une plateforme dédiée au traitement des données GPS.")
                            st.subheader("Il s'agit ici des informations brutes prélevées directement sur le traceur GPS via une plateforme de géolocalisation. ")
                            st.subheader("Ces informations sont ensuite traitées de manière automatique et rationnelle, ayant pour objectif d'avoir. ")
                            st.subheader("Une visibilité détaillée sur la mobilité de votre traceur GPS. ")
                            st.subheader("Aujourd'hui, TKHGPS vous offre les services suivants pour un essai de 6 mois : ")
                            st.subheader("1- Sauvegarde permanente de vos données sur les 6 mois")
                            st.subheader("2- Ajout de voiture illimité")
                            st.subheader("3- Mise à jour de vos voitures ")
                            st.subheader("4- Le service personnalisé inclut. ")
                            st.subheader("5- Visuel sur les distances parcourues ")
                            st.subheader("6- Visuel sur le temps mobile ")
                            st.subheader("7- Visuel sur le temps immobile ")
                            st.subheader("8- Téléchargez les donnes traitées au format excel")
                            st.subheader("9- Assistance 24/24 du lundi au vendredi")
                            st.subheader("Au bout des 6 mois une mise à jour de TKHGPS sera disponible avec des 🎁")
                            st.header("Mode d'utilisation ")
                            st.subheader("Nous contacter pour une formation gratuite au : ")
                            st.subheader("📧 : tsafack40@gmail.com")
                            st.subheader("📞 : +237 695 092 273")
                        
                    with tab2:
                        st.header("Bureau 💻 ⚙️")
                        st.subheader("Apres chaque modifation taper sur la touche 'r' ")
                        st.warning("Si la page s'actualise, entrez vos informations")
                        # Créer une voiture
                        col_1,col_2=st.columns(2)
                        with col_1:
                            st.subheader("➕ Ajoutez une voiture")
                            with st.expander("Ajoutez une voiture"):
                                try:
                                    username = st.text_input("nom du véhicule")
                                    submitted = st.button("Enregistrer")
                                    if submitted & (len(username)!=0):
                                        st.subheader("patientez ...")
                                        n = Super.exist(username,user)
                                        N = Super.Exist(username)
                                        if (n==0)&(N==0):
                                            Super.Insert(username)
                                            Super.liste(username,user)
                                            st.success("Voiture enregistré avec success")
                                        else:
                                            st.warning("Cette voiture existe déjà dans notre base de données")
                                            st.warning("Nous vous suggérons de modifier le nom de votre voiture")
                                except:
                                    pass
                        
                        with col_2:
                            st.subheader("➖ Retirez une voiture")
                            with st.expander(" Retirez une voiture"):
                                st.write("En cours de developpent !!!")
                        
                        ### MANAGER LE VEHICULE 
                        
                        col_1_1,col_2_2=st.columns(2)
                        with col_1_1:
                            st.subheader("📥 Inserez les données d'une voiture")
                            with st.expander("Inserez les données d'une voiture"):
                                try:
                                    #a=Super.elemts(user)
                                    #options = st.multiselect('Choix multiple',a)
                                    if username_1 == 'tsafack_kevin_root':
                                        option = st.multiselect("Selectionez une voiture        ",Super.Allelemts())
                                    else :
                                        option = st.multiselect("Selectionez une voiture        ",Super.elemts(user))
                                    r=Uplaodss(" ").uploid()
                                    name = r[1][0][:-4]
                                    st.write(option[0])
                                    if option[0] == name:
                                        submitted = st.button("Enregistrer ")
                                        if submitted:
                                            option = option[0]
                                            st.subheader("patientez ...")
                                            var_1 = SeparationEnJour(DataSet(r[0][0]).DataFrame()).Separe()
                                            #r_1.append([ r[1][i]  , var_1[0]  , var_1[1]]) # [nom de la voiture , dataset,jour] 
                                            Super.sq(option,var_1[0],var_1[1])
                                            Super.update([option],1,1,1,24)
                                            st.success("Les données de votre voiture ont été sauvegardé avec success")
                                    else :
                                        st.write("le fichier ne corespond pas au véhicule")
                                    
                                except:
                                        st.warning("Actualiser l'application si une erreur se produit après le chargement de votre fichier!!!")
                        # UPDATE
                        with col_2_2:
                            st.subheader("♻️ Mettre à jours les données d'une voiture")
                            with st.expander("Mettre à jours les données d'une voiture"):
                                if username_1 == 'tsafack_kevin_root':
                                    option = st.multiselect("Selectionez une voiture       ",Super.Allelemts())
                                else :
                                    option = st.multiselect("Selectionez une voiture       ",Super.elemts(user))
                                r=Uplaodss("  ").uploid()
                                try:
                                    name = r[1][0][:-4]
                                    st.write(option[0])
                                    if option[0] == name:
                                        submitted = st.button("Enregistrer  ")
                                        if submitted:
                                            option = option[0]
                                            st.subheader("patientez ...")
                                            car = Super.sql_to_df(option) #tableau [name , DataFrmae , Days Week] we read this on data base
                                            var_1 = SeparationEnJour(DataSet(r[0][0]).DataFrame()).Separe() #tableau [DataFrmae , Days Week]
                                            new_car = Super.concat(car[1],var_1[0],car[2],var_1[1])
                                            new_car_day = SeparationEnJour(new_car).Separe()[1]
                                            Super.sq_1(option,new_car,new_car_day)
                                            Super.update([option])
                                            st.success("Les données de votre voiture ont été mise à jour avec success")
                                    else :
                                        st.warning("le fichier ne corespond pas au véhicule")
                                    
                                except:
                                    pass
                        
                        n_j = 1
                        n_s = 1
                        n_m = 1
                        st.subheader("⚙️ Préférences")
                        with st.expander("Préférences"):
                            col1_1 , col1_2 = st.columns(2)
                            with col1_1:
                                 title = st.text_input('Heure de Début : hh:mm:ss',"00:00:00")
                                 debut = title
                                 st.write(debut)
                            with col1_2:
                                title_1 = st.text_input('Heure de Fin : hh:mm:ss',"23:59:59")
                                fin = title_1
                                st.write(fin)
                            
                            st.write("Traitement groupé")
                            col2_1 , col2_2 , col2_3 = st.columns(3)
                            with col2_1:
                                 j = st.text_input('Nombre de jour',1)
                                 try:    
                                     n_j = int(j)
                                     st.write(j)
                                 except:
                                    st.write("")
                            with col2_2:
                                s = st.text_input('Nombre de semaine',1)
                                try:    
                                    n_s = int(s)
                                    st.write(s)
                                except:
                                   st.write("")
                            with col2_3:
                                m = st.text_input('Nombre de mois',1)
                                try:    
                                    n_m = int(m)
                                    st.write(m)
                                except:
                                   st.write("")
                            
                            if username_1 == 'tsafack_kevin_root':
                                option = st.multiselect("Selectionez une voiture         ",Super.Allelemts())
                            else :
                                option = st.multiselect("Selectionez une voiture         ",Super.elemts(user))
                            submitted = st.button("Enregistrer   ")
                            try:
                                if submitted:
                                    x = c_h(fin)-c_h(debut)
                                    if len(option)==1:
                                        st.subheader("patientez ...")
                                        option=option[0]
                                        car = Super.sql_to_df(option) #tableau [name , DataFrmae , Days Week] we read this on data base
                                        var_1 = SeparationEnJour(car[1] , debut ,fin ).Separe() #tableau [DataFrmae , Days Week]
                                        #avant de faire la modification , on suprime dataframe_1 et Jours_1
                                        Super.sq_1(option,var_1[0],var_1[1]) # on modifie la copie du véhicule en question on va crer un sq_1
                                        Super.update([option],n_j,n_s,n_m,x)
                                        st.success("Modification enregistré avec success")
                                    else:
                                        for option in option:
                                            st.subheader("patientez ...")
                                            car = Super.sql_to_df(option) #tableau [name , DataFrmae , Days Week] we read this on data base
                                            var_1 = SeparationEnJour(car[1] , debut ,fin ).Separe() #tableau [DataFrmae , Days Week]
                                            #avant de faire la modification , on suprime dataframe_1 et Jours_1
                                            Super.sq_1(option,var_1[0],var_1[1]) # on modifie la copie du véhicule en question on va crer un sq_1
                                            Super.update([option],n_j,n_s,n_m,x)
                                            st.success("Modification enregistré avec success")
                            except:
                                st.warning("error!!! Actualiser l'application")
                        
                    with tab3:
                        st.header("Distances 🚘 📊")
                        if username_1 == 'tsafack_kevin_root':
                            options = st.multiselect("Selectionez une voiture    ",Super.Allelemts())
                        else :
                            options = st.multiselect("Selectionez une voiture    ",Super.elemts(user))
                        try:
                            if len(options)!=0:
                                st.subheader(" Jours , Semaines , Mois")
                                GRAPHD(options)
                            else:
                                st.warning('Selectionez au moins une voiture')
                        except:
                            st.warning('Selectionez au moins une voiture')
                    
                    with tab4:
                        st.header("Temps ⌚ 📊")
                        if username_1 == 'tsafack_kevin_root':
                            options = st.multiselect("Selectionez une voiture     ",Super.Allelemts())
                        else :
                            options = st.multiselect("Selectionez une voiture     ",Super.elemts(user))
                        try:
                            if len(options)!=0:
                                st.subheader("Temps Mobile : Jours , Semaines , Mois")
                                GRAPHTM(options)
                                st.subheader("Temps Immobile : Jours , Semaines , Mois")
                                GRAPHTIM(options)
                            else:
                                st.warning('Selectionez au moins une voiture')
                        except:
                            st.warning('Selectionez au moins une voiture')
                    
                    with tab5:
                        st.header("Téléchargement 📥")
                        if username_1 == 'tsafack_kevin_root':
                            options = st.multiselect("Selectionez une voiture      ",Super.Allelemts())
                        else :
                            options = st.multiselect("Selectionez une voiture      ",Super.elemts(user))
                        if len(options)!=0:
                            'Distance Jours'
                            st.write(F11(options)[0][0])
                            'Distance Semaines'
                            st.write(F11(options)[1][0])
                            'Distance Mois'
                            st.write(F11(options)[2][0])
                            'Temps Mobile Jours'
                            st.write(F22(options)[0][0])
                            'Temps Mobile Semaines'
                            st.write(F22(options)[1][0])
                            'Temps Mobile Mois'
                            st.write(F22(options)[2][0])
                            'Temps Immobile Jours'
                            st.write(F33(options)[0][0])
                            'Temps Immobile Semaines'
                            st.write(F33(options)[1][0])
                            'Temps Immobile Mois'
                            st.write(F33(options)[2][0])
                            
                            col1_111,col1_122 = st.columns(2)
                            with col1_111:
                                try:
                                     with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                                         # Write each dataframe to a different worksheet.
                                         F11(options)[0][0].to_excel(writer, sheet_name='Distance Jours')
                                         F11(options)[1][0].to_excel(writer, sheet_name='Distance Semaines')
                                         F11(options)[2][0].to_excel(writer, sheet_name='Distance Mois')
                                         F22(options)[0][0].to_excel(writer, sheet_name='Temps Mobile Jours')
                                         F22(options)[1][0].to_excel(writer, sheet_name='Temps Mobile Semaines')
                                         F22(options)[2][0].to_excel(writer, sheet_name='Temps Mobile Mois')
                                         F33(options)[0][0].to_excel(writer, sheet_name='Temps Immobile Jours')
                                         F33(options)[1][0].to_excel(writer, sheet_name='Temps Immobile Semaines')
                                         F33(options)[2][0].to_excel(writer, sheet_name='Temps Immobile Mois')
                                         # Close the Pandas Excel writer and output the Excel file to the buffer
                                         writer.save()
                                         st.markdown("Téléchargher toutes les données : distances, temps mobiles , temps immobiles au format excel")
                                         st.download_button(
                                             label="Télécharger",
                                             data=buffer,
                                             file_name= str(options)+"Données GPS.xlsx",
                                             #mime="application/vnd.ms-excel"
                                         )
                                except:
                                    st.warning('Selectionez une voiture')
                            with col1_122:
                                st.write("")
                        else:
                            st.warning('Selectionez au moins une voiture')
                    
                    with tab6:
                        st.header("Déconnexion 🚪")
                        st.subheader("📧 : tsafack40@gmail.com")
                        st.subheader("📞 : +237 695 092 273")
                        boutton_2h1 = st.button("Se déconnecter 🚪")
                        if (boutton_2h1) :
                            Super_1.update(username_1,1)
                            username=" "
                            
                    
        
except:
    pass            

try:
    if ((Super_1.idp(username_1))==0) :
        st.sidebar.title("Cette session est en cours Entrez le mot de pass pour la répurez")
        password = st.sidebar.text_input(" ", type="password")
        st.session_state.key = password
        boutton_1 = st.sidebar.button("Recupérez ")
        if (boutton_1) :
            pass
        elif (Super_1.login(username_1,password) !=1):
            st.sidebar.write("Mot de pass incorrect")
except:
    pass




    



       
