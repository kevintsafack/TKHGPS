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
########## page configuration #############
st.set_page_config(
     page_title="TKHGPS.io",page_icon="👋",
     layout="wide",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)

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
###########
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f :
        return json.load(f)

###########
#################### Nom des animation ###################################
itineraire = load_lottiefile("itineraite.json")
stat = load_lottiefile("stat.json")
question = load_lottiefile("question.json")
traking = load_lottiefile("traking.json")
analys = load_lottiefile("analys.json")
car = load_lottiefile("car.json")
garage = load_lottiefile("garage.json")
analys =load_lottiefile("analys.json")
gps =load_lottiefile("gps.json")
#########################################################################


tab1, tab2, tab3 , tab4 = st.tabs(["Présentation 🎁", " Insérez un 📁", "Distances 🚘 📊" , "Temps ⌚ 📊"])
###################### tab1 = Présentation des différentes animations  #################################
with tab1:
    
    p=200
    n=400
    with st.container():
        col1, col2 , col3  = st.columns(3)
        with col1:
                
                st_lottie( gps,speed=1,reverse=False,loop=True,quality="low",height=p,width=n, key=None,)
                st.title("GPS")
            
        with col2:
                
                st_lottie(question,speed=1,reverse=False,loop=True,quality="low",height=p,width=n,key=None,)
                st.title("QUESTION")
        with col3:
                
                st_lottie(car,speed=1,reverse=False,loop=True,quality="low",height=p,width=n,key=None,)
                st.title("MOBILITE")
    with st.container():
        col4 , col5 , col6 = st.columns(3)
        with col4:
                
                st_lottie(itineraire,speed=1,reverse=False,loop=True,quality="low",height=p,width=n, key=None,)
                st.title("Itineraire")
            
        with col5:
                
                st_lottie(stat,speed=1,reverse=False,loop=True,quality="low",height=p,width=n,key=None,)
                st.title("Statistique")
        with col6:
                
                st_lottie(analys,speed=1,reverse=False,loop=True,quality="low",height=p,width=n,key=None,)
                st.title("ANALYSES")
################################################################♦########################################☺#####
#################################  traiement simple   ######################################
j=0


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
            st.write("Temps M")
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
            st.write("Temps IM")
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


user='liste'
with tab2:
    st.title(user)
    a=Super.elemts(user)
    options = st.multiselect('Choix multiple',Super.elemts(user))
    #DOWNLOAD
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
    
    try:
        st.title("D")
        GRAPHD(options)
        st.title("TM")
        GRAPHTM(options)
        st.title("TIM")
        GRAPHTIM(options)
    except:
        st.warning('1-Selectionez une voiture')
    
    
    
    
    
    ###### Colonne pour le choix des heures ######
    
    n_j = 1
    n_s = 1
    n_m = 1
    with st.expander("Heure journalière"):
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
        
        option = st.multiselect("Selectionez une voiture ",Super.elemts(user))
        submitted = st.button("Enregistrer   ")
        try:
            if submitted:
                x = c_h(fin)-c_h(debut)
                if len(option)==1:
                    option=option[0]
                    car = Super.sql_to_df(option) #tableau [name , DataFrmae , Days Week] we read this on data base
                    var_1 = SeparationEnJour(car[1] , debut ,fin ).Separe() #tableau [DataFrmae , Days Week]
                    #avant de faire la modification , on suprime dataframe_1 et Jours_1
                    Super.sq_1(option,var_1[0],var_1[1]) # on modifie la copie du véhicule en question on va crer un sq_1
                    Super.update([option],n_j,n_s,n_m,x)
                    st.success("Modification enregistré avec success")
                else:
                    for option in option:
                        car = Super.sql_to_df(option) #tableau [name , DataFrmae , Days Week] we read this on data base
                        var_1 = SeparationEnJour(car[1] , debut ,fin ).Separe() #tableau [DataFrmae , Days Week]
                        #avant de faire la modification , on suprime dataframe_1 et Jours_1
                        Super.sq_1(option,var_1[0],var_1[1]) # on modifie la copie du véhicule en question on va crer un sq_1
                        Super.update([option],n_j,n_s,n_m,x)
                        st.success("Modification enregistré avec success")
        except:
            st.warning("error!!! Actualiser l'application")
    
    ## AJOUT DE VOITURES
    col_1,col_2=st.columns(2)
    with col_1:
        with st.expander("Ajoutez une voiture"):
            try:
                username = st.text_input("nom du véhicule")
                submitted = st.button("Enregistrer")
                if submitted & (len(username)!=0):
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
        with st.expander(" Retirer une voiture"):
            st.write("En cours de developpent !!!")
    
    ### MANAGER LE VEHICULE
    col_1_1,col_2_2=st.columns(2)
    with col_1_1:
        with st.expander("Inserez les données d'une voiture"):
            try:
                option = st.selectbox("Selectionez une voiture",Super.elemts(user))
                r=Uplaodss(" ").uploid()
                name = r[1][0][:-4]
                st.write(r[1][0][:-4])
                if option == name:
                    submitted = st.button("Enregistrer ")
                    if submitted:
                        var_1 = SeparationEnJour(DataSet(r[0][0]).DataFrame() ,debut ,fin ).Separe()
                        #r_1.append([ r[1][i]  , var_1[0]  , var_1[1]]) # [nom de la voiture , dataset,jour] 
                        Super.sq(option,var_1[0],var_1[1])
                        Super.update([option],1,1,1,24)
                        st.success("Les données de votre voiture ont été sauvegardé avec success")
                else :
                    st.write("le fichier ne corespond pas au véhicule")
                
            except:
                    st.warning("error!!! Actualiser l'application")
    # UPDATE
    with col_2_2:
        with st.expander("Mettre à jours les données d'une voiture"):
            option = st.selectbox("Selectionez une voiture   ",Super.elemts(user))
            r=Uplaodss("  ").uploid()
            try:
                name = r[1][0][:-4]
                st.write(r[1][0][:-4])
                if option == name:
                    submitted = st.button("Enregistrer  ")
                    if submitted:
                        car = Super.sql_to_df(option) #tableau [name , DataFrmae , Days Week] we read this on data base
                        var_1 = SeparationEnJour(DataSet(r[0][0]).DataFrame() ,debut ,fin ).Separe() #tableau [DataFrmae , Days Week]
                        new_car = Super.concat(car[1],var_1[0],car[2],var_1[1])
                        new_car_day = SeparationEnJour(new_car ,debut ,fin ).Separe()[1]
                        Super.sq(option,new_car,new_car_day)
                        Super.update([option])
                        st.success("Les données de votre voiture ont été sauvegardé avec success")
                else :
                    st.warning("le fichier ne corespond pas au véhicule")
                
            except:
                pass
    
    
    try:
       ############## JOURS #######################
       if 'distance_Jour' not in st.session_state:
           st.session_state.distance_Jour = []
           
       if 'temp_jour_mobile' not in st.session_state:
           st.session_state.temps_jour_mobile = []
           
       if 'temp_jour_immobile' not in st.session_state:
          st.session_state.temps_jour_immobile = []
       
       if 'excel_jr_d' not in st.session_state:
           st.session_state.excel_jr_d = []
       
       
       if 'excel_jr_tm' not in st.session_state:
           st.session_state.excel_jr_tm = []
       
       
       if 'excel_jr_tim' not in st.session_state:
           st.session_state.excel_jr_tim = []
           
       
       #----------------------------------------------#
        
       ###############################################    
       if 'nom' not in st.session_state:
           st.session_state.nom = []
       
       x = c_h(fin)-c_h(debut) # Calcul du temps d'une Jou
       st.write("Vous considérez qu'une journé fait : ",x , "Heures")
       r_1 = [] # Tableau qui contient les datasets filtré sur l'heure journalié
       for i in range(len(r[0])):
           var_1 = SeparationEnJour(DataSet(r[0][i]).DataFrame() ,debut ,fin ).Separe()
           r_1.append([ r[1][i]  , var_1[0]  , var_1[1]]) # [nom de la voiture , dataset,jour]
       st.session_state.data = r_1 # enrégistre le tableau dans la session courante
       datas = st.session_state.data # Variable sur le Tableau des dataset : datas
       
       jour = sq(datas[0][0],datas[0][1],datas[0][2])
       nom = "Afrique du Sud CE 290 LP 1.csv"
       datas_1 = [[ nom , m_j(nom) , jour]]
       #######JOURS############
       distance_jour = [] # nom_voiture,dataframe,jours de mobilité
       temps_jour_mobile = []
       temps_jour_immobile = []
       
       #######SEMAINES############
       distance_sem = [] 
       temps_sem_mobile = []
       temps_sem_immobile = []
       #######MOIS############
       distance_m = [] 
       temps_m_mobile = []
       temps_m_immobile = [] 
        
       
       for i in range(len(datas_1)):
           #######JOURS############
           distance_jour.append(Dist(datas[i],n_j,0).dist()) #datas[i]==[nom de la voiture, dataframe de la voiture,jours de la voiture]
           temps_jour_mobile.append(Tem(datas[i],n_j,0,x).temps()[0])
           temps_jour_immobile.append(Tem(datas[i],n_j,0,x).temps()[1])
           ######SEMAINES############
           distance_sem.append(Dist(datas[i],n_s,1).dist())
           temps_sem_mobile.append(Tem(datas[i],n_s,1,x).temps()[0])
           temps_sem_immobile.append(Tem(datas[i],n_s,1,x).temps()[1])
           ######MOIS############
           distance_m.append(Dist(datas[i],n_m,2).dist())
           temps_m_mobile.append(Tem(datas[i],n_m,2,x).temps()[0])
           temps_m_immobile.append(Tem(datas[i],n_m,2,x).temps()[1])
           
       
       ######MISE SOUS SESSION PERMANENTE#######
       #######JOURS############
       st.session_state.distance_Jour = [distance_jour,distance_sem,distance_m]
       st.session_state.temps_jour_mobile = [temps_jour_mobile,temps_sem_mobile,temps_m_mobile]
       st.session_state.temps_jour_immobile = [temps_jour_immobile,temps_sem_immobile,temps_m_immobile]
       
       #######SEMAINES############
       
       nom_car = st.session_state.distance_Jour[0]
       #st.write(nom_car[i][0])
       name_car = []
       for i in range(len(nom_car)):
           name_car.append([i,nom_car[i][0]])
       option = st.multiselect('Choisir une voiture',name_car,name_car)
       st.session_state.nom = option
       
       def F1(nom_car):
           options = st.session_state.nom
           Données = []
           G = []
           if len(options)==1:
               st.write(options[0][0],nom_car[options[0][0]])
               G = Graph([nom_car[options[0][0]]]).graph()[0]
               Données.append(Graph([nom_car[options[0][0]]]).graph()[1]) 
           else:
               
               options_1 = []
               for i in range(len(options)):
                   options_1.append(nom_car[options[i][0]])
               G = Graph(options_1).graph()[0]
               Données.append(Graph(options_1).graph()[1])
           
           return G , File(Données[0]).file()
       
       #######MOIS############
       st.success("Bien chargé 😃")
    except : 
        st.title("Respecteer le format horaire ")
#############################################################################
with tab3:
    
    try:
        datas[0][1]
        st.title(f"on considère qu'une journé à : {x} heures")
        st.title("JOURS")
        
        T_1 = F1(st.session_state.distance_Jour[0])
        T_1[0]
        st.write(T_1[1])
        st.title("SEMAINES")
        T_2 = F1(st.session_state.distance_Jour[1])
        T_2[0]
        st.write(T_2[1])
        st.title("MOIS")
        T_3 = F1(st.session_state.distance_Jour[2])
        T_3[0]
        st.write(T_3[1])
        st.session_state.excel_jr_d = [T_1[1],T_2[1],T_3[1]]
        
        
            
        
        
    except:
        st.write("")

with tab4:
    try:
        st.title("Temps mobile")
        def F2(nom_car):
                name_car = []
                for i in range(len(nom_car)):
                    name_car.append([i,nom_car[i][0]])
                options = st.session_state.nom
                Données = []
                G = []
                if len(options)==1:
                    G = GraphTime([nom_car[options[0][0]]]).graph()[0]
                    Données.append(GraphTime([nom_car[options[0][0]]]).graph()[1]) 
                else:
                    
                    options_1 = []
                    for i in range(len(options)):
                        options_1.append(nom_car[options[i][0]])
                    G = GraphTime(options_1).graph()[0]
                    Données.append(GraphTime(options_1).graph()[1])
                return G,File(Données[0]).file()
        st.title("Jours")
        T_1 = F2(st.session_state.temps_jour_mobile[0])
        T_1[0]
        st.write(T_1[1])
        st.title("SEMAINES")
        T_2 = F2(st.session_state.temps_jour_mobile[1])
        T_2[0]
        st.write(T_2[1])
        st.title("MOIS")
        T_3 = F2(st.session_state.temps_jour_mobile[2])
        T_3[0]
        st.write(T_3[1])
        st.session_state.excel_jr_tm = [T_1[1],T_2[1],T_3[1]]
        st.title("Temps immobile")
            
        nom_cars = st.session_state.temps_jour_immobile
        def F3(nom_cars):
            name_cars = []
            for i in range(len(nom_cars)):
                name_cars.append([i,nom_cars[i][0]])
            optionss = st.session_state.nom
            Données = []
            G = []
            if len(optionss)==1:
                G = GraphTime([nom_cars[optionss[0][0]]]).graph()[0]
                Données.append(GraphTime([nom_cars[optionss[0][0]]]).graph()[1]) 
            else:
                
                options_1 = []
                for i in range(len(optionss)):
                    options_1.append(nom_cars[optionss[i][0]])
                G = GraphTime(options_1).graph()[0]
                Données.append(GraphTime(options_1).graph()[1])
            return G,File(Données[0]).file()
        st.title("Jours")
        T_11 = F3(st.session_state.temps_jour_immobile[0])
        T_11[0]
        st.write(T_11[1])
        st.title("SEMAINES")
        T_21 = F3(st.session_state.temps_jour_immobile[1])
        T_21[0]
        st.write(T_21[1])
        st.title("MOIS")
        T_31 = F3(st.session_state.temps_jour_immobile[2])
        T_31[0]
        st.write(T_31[1])
        st.session_state.excel_jr_tim = [T_11[1],T_21[1],T_31[1]]
        col1_111,col1_122 = st.columns(2)
        with col1_111:
             with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                 # Write each dataframe to a different worksheet.
                 st.session_state.excel_jr_d[0].to_excel(writer, sheet_name='Distance Jours')
                 st.session_state.excel_jr_d[1].to_excel(writer, sheet_name='Distance Semaines')
                 st.session_state.excel_jr_d[2].to_excel(writer, sheet_name='Distance Mois')
                 st.session_state.excel_jr_tm[0].to_excel(writer, sheet_name='Temps Mobile Jours')
                 st.session_state.excel_jr_tm[1].to_excel(writer, sheet_name='Temps Mobile Semaines')
                 st.session_state.excel_jr_tm[2].to_excel(writer, sheet_name='Temps Mobile Mois')
                 st.session_state.excel_jr_tim[0].to_excel(writer, sheet_name='Temps Immobile Jours')
                 st.session_state.excel_jr_tim[1].to_excel(writer, sheet_name='Temps Immobile Semaines')
                 st.session_state.excel_jr_tim[2].to_excel(writer, sheet_name='Temps Immobile Mois')
                 # Close the Pandas Excel writer and output the Excel file to the buffer
                 writer.save()
                 st.header("Téléchargher toutes les données : distances, temps mobiles , temps immobiles au format excel")
                 st.download_button(
                     label="Télécharger",
                     data=buffer,
                     file_name="Données GPS.xlsx",
                     mime="application/vnd.ms-excel"
                 )
        with col1_122:
            st.write("")
        
    except:
        pass