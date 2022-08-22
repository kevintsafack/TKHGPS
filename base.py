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
# Copy de la base données des jours et dataframe
class Super:
    def __init__(self):
        pass
    
    def copy(nom):
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS dataframe_1 AS SELECT * FROM dataframe"
        cur.execute(query)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = f"CREATE TABLE IF NOT EXISTS Jours_1 AS SELECT * FROM Jours"
        cur.execute(query_1)
        con.commit()
        cur.close()
    
    def drop(nom):
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = "DROP TABLE IF EXISTS dataframe_1"
        cur.execute(query)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS Jours_1"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS DJ_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS DJ_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS DS_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS DS_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS DM_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS DM_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        ########################################
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMJ_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMJ_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMJ_T"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMS_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMS_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMS_T"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMM_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMM_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TMM_T"
        cur.execute(query_1)
        con.commit()
        cur.close()
        ########################################
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMJ_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMJ_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMJ_T"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMS_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMS_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMS_T"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMM_D"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMM_J"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query_1 = "DROP TABLE IF EXISTS TIMM_T"
        cur.execute(query_1)
        con.commit()
        cur.close()
        
    #Dataframe to sqlite3
    def sq(nom,data,jours):
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS dataframe (lat number,lng number,altitude number,angle number,speed number, dt datetime)"
        cur.execute(query)
        data.to_sql('dataframe', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #######################################################
        df = pd.DataFrame({'jours' : jours})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS Jours (jours TEXT)"
        cur.execute(query)
        df.to_sql('Jours', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT jours from Jours"
        n=cur.execute(query)
        t=n.fetchall()
        t[0][0]
        z=[]
        for i in range(len(t)):
            z.append(t[i][0])
        con.close()
        Super.copy(nom)
        
        return z
    
    def sq_1(nom,data,jours):
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS dataframe_1 (lat number,lng number,altitude number,angle number,speed number, dt datetime)"
        cur.execute(query)
        data.to_sql('dataframe_1', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #######################################################
        df = pd.DataFrame({'jours' : jours})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS Jours_1 (jours TEXT)"
        cur.execute(query)
        df.to_sql('Jours_1', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT jours from Jours_1"
        n=cur.execute(query)
        t=n.fetchall()
        t[0][0]
        z=[]
        for i in range(len(t)):
            z.append(t[i][0])
        con.close()
        Super.copy(nom)
        
        return z
       
    #mise à jours de la base de données sqlite3
    #conversion de la base de données endatabase puis formatage connue
    def m_j(nom):
        file = nom+'.db'
        con = sqlite3.connect(file)
        df = pd.read_sql_query("SELECT * from dataframe", con)
        con.close()
        df.dt = pd.to_datetime(df.dt)
        dte = df.dt
        df = df.rename(columns={'dt':'dte', 'lat':'lat', 'lng':'lng', 'altitude':'altitude',
                                    'angle':'angle', 'speed':"speed"})
        df = pd.concat([df,dte],axis=1)
        df=df.set_index('dte')
        return df
    
    def m_j_1(nom):
        file = nom+'.db'
        con = sqlite3.connect(file)
        df = pd.read_sql_query("SELECT * from dataframe_1", con)
        con.close()
        df.dt = pd.to_datetime(df.dt)
        dte = df.dt
        df = df.rename(columns={'dt':'dte', 'lat':'lat', 'lng':'lng', 'altitude':'altitude',
                                    'angle':'angle', 'speed':"speed"})
        df = pd.concat([df,dte],axis=1)
        df=df.set_index('dte')
        return df
    
    def printt():
        con = sqlite3.connect('example.db')
        df = pd.read_sql_query("SELECT * from person", con)
        con.close()
        return df
    
    def concat(S1,S2,Q1,Q2):
        d=str(S2.index[0])[:10]
        d_1=str(S2.index[-1])[:10]
        if len(S1.loc[d:d_1]) == 0:
            return pd.concat([S1,S2])
        else :
            Q2_1 = []
            for i in Q2:
                if Q1.count(i)==0:
                    Q2_1.append(i)
            print("Nous avons suprimez les jours qui se repaitaient")
            return pd.concat([S1,S2.loc[Q2_1[0]:Q2_1[-1]]])
    
    def liste(nom,user):
        file = user+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS Listes (listes TEXT)"
        cur.execute(query)
        con.commit()
        cur.close()
        ####################insert##############
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"INSERT INTO Listes (listes) VALUES (?)"
        cur.execute(query,(nom,))
        con.commit()
        cur.close()
    
    def user(user):
        file = user+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS Listes (listes TEXT)"
        cur.execute(query)
        con.commit()
        cur.close()
    
    
    def exist(nom,user):
        file = user+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM Listes WHERE listes = ?"
        c = cur.execute(query,(nom,)).fetchall()
        con.commit()
        cur.close()
        return len(c)
    
    def Exist(nom):
        con = sqlite3.connect('LISTES.db')
        cur = con.cursor()
        query = f"SELECT * FROM Listes WHERE listes = ?"
        c = cur.execute(query,(nom,)).fetchall()
        con.commit()
        cur.close()
        return len(c)
    def Insert(nom):
        con = sqlite3.connect('LISTES.db')
        cur = con.cursor()
        query = f"INSERT INTO Listes (listes) VALUES (?)"
        cur.execute(query,(nom,))
        con.commit()
        cur.close()
    
    def elemts(user):
        file = user+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM Listes"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        z=[]
        for i in range(len(c)):
            z.append(c[i][0])
        return z
    #donne le nom de toutes les voitures
    def Allelemts():
        con = sqlite3.connect('LISTES.db')
        cur = con.cursor()
        query = f"SELECT * FROM Listes"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        z=[]
        for i in range(len(c)):
            z.append(c[i][0])
        return z
    #nom de tous les users
    def infos_1():
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        query = f"SELECT * FROM person"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        z=[]
        for i in range(len(c)):
            z.append(c[i][0])
        return z
    
    def infos():
        r=Super.infos_1()
        T = []
        for i in r:
            file = i+'.db'
            con = sqlite3.connect(file)
            try:
                df = pd.read_sql_query("SELECT * from Listes", con)
                con.close()
                T.append([i,df])
            except:
                st.subheader("L'utilisateur "+i+" n'a pas encore de véhicules")
        return T
    def delet(nom):
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        query = f"DELETE FROM person WHERE nom=?"
        cur.execute(query,(nom,))
        con.commit()
        cur.close()
    
    #base de donné vers le format : nom,dataframe,jours
    def sql_to_df(nom):
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT jours from Jours"
        n=cur.execute(query)
        t=n.fetchall()
        t[0][0]
        z=[]
        for i in range(len(t)):
            z.append(t[i][0])
        con.close()
        return nom,Super.m_j(nom),z
    
    def sql_to_df_1(nom):
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT jours from Jours_1"
        n=cur.execute(query)
        t=n.fetchall()
        t[0][0]
        z=[]
        for i in range(len(t)):
            z.append(t[i][0])
        con.close()
        return nom,Super.m_j_1(nom),z
    
    def update(a,n_j=1,n_s=1,n_m=1,x=24):
        for i in range(len(a)):
            #Distance
            d=Dist(Super.sql_to_df_1(a[i]),n_j,0).dist() # 1 == nombre de jour
            d_1 = Dist(Super.sql_to_df_1(a[i]),n_s,1).dist()
            d_2 = Dist(Super.sql_to_df_1(a[i]),n_m,2).dist()
            D = [d[1],d[2],d_1[1],d_1[2],d_2[1],d_2[2]]
            #Temps M
            t = Tem(Super.sql_to_df_1(a[i]),n_j,0,x).temps()[0] # 1 == nombre de semaine , 24 == heure de la journée
            t_1 = Tem(Super.sql_to_df_1(a[i]),n_s,1,x).temps()[0]
            t_2 = Tem(Super.sql_to_df_1(a[i]),n_m,2,x).temps()[0]
            TM = [ t[1],t[2],t[3] , t_1[1],t_1[2],t_1[3] , t_2[1],t_2[2],t_2[3] ]
            #Temps IM
            ti = Tem(Super.sql_to_df_1(a[i]),n_j,0,x).temps()[1] # 1 == nombre de semaine , 24 == heure de la journée
            ti_1 = Tem(Super.sql_to_df_1(a[i]),n_s,1,x).temps()[1]
            ti_2 = Tem(Super.sql_to_df_1(a[i]),n_m,2,x).temps()[1]
            TIM = [ ti[1],ti[2],ti[3] , ti_1[1],ti_1[2],ti_1[3] , ti_2[1],ti_2[2],ti_2[3] ]
            nom=a[i]
            Temps_M(nom, TM).indistr()
            Temps_IM(nom, TIM).indistr()
            DistanceJour(nom,D).indistr()

