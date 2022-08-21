import sqlite3
import subprocess
import streamlit as st
import base64
from streamlit_option_menu import option_menu
class Database:
    def __init__(self,database_name:str):
        self.con = sqlite3.connect(database_name)
        self.con.row_factory = sqlite3.Row
    def create(self,nom:str,pas:str,idp:int,rand:int,mail:str):
        cursor =  self.con.cursor()
        query = f"INSERT INTO person (nom,pas,idp,rand,mail) VALUES (?,?,?,?,?);"
        cursor.execute(query,(nom,pas,idp,rand,mail,))
        cursor.close()
        self.con.commit()
    def laod(self,idlaod:int,idp:int):
        cursor =  self.con.cursor()
        query = f"UPDATE laod SET idlaod =? , idp =?,idl=0 ;"
        cursor.execute(query,(idlaod,idp))
        cursor.close()
        self.con.commit()
    
    #Vérifier qu'un utilisateur existe
    def user_exist_with(self,nom : str)->bool:
        cursor = self.con.cursor()
        query = f"SELECT * FROM person WHERE nom = ?;"
        result=cursor.execute(query,(nom,)).fetchall()
        cursor.close()
        return len(result) == 1
    
    #Récupérer le mot de pass d'un utilisateur qui existe
    def pas_for(self,nom:str)->str:
        cursor = self.con.cursor()
        query = f"SELECT pas FROM person WHERE nom = ?;"
        cursor.execute(query,(nom,))
        result = cursor.fetchall()
        cursor.close()
        return dict(result[0])["pas"]
    
    #Changer un mot de passe
    def change_pas(self,nom:str,new_pas:str):
        cursor = self.con.cursor()
        query = f"UPDATE person SET  pas = ?, nom=?;"
        cursor.execute(query,(new_pas,nom,))
        cursor.close()
        self.con.commit()

class Image:
    def __init__(self,image,css):
        self.image = image
        self.css = css
        pass
    def background(self):
        image = self.image
        with open(image, "rb") as image:
            encoded_string = base64.b64encode(image.read())
        t=self.css 
        st.markdown(
    f"""
    <style>
    {t}  {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """, unsafe_allow_html=True)


            
class Super_1:
    def __inin__(self):
        pass
    def login(username,password):
            if password == Database('example.db').pas_for(username):
                return 1
            else:
                pass
    def update(nom,idp):
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        query=f"UPDATE person SET idp=? WHERE nom =?  ;"
        cur.execute(query,(idp,nom))
        cur.close()
        con.commit()
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        query=f"SELECT idp FROM person WHERE nom =?  ;"
        t=cur.execute(query,(nom,)).fetchall()
        con.close()
        return t[0][0]
    def idp(nom):
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        query=f"SELECT idp FROM person WHERE nom =?  ;"
        t=cur.execute(query,(nom,)).fetchall()
        con.close()
        try:
            return t[0][0]
        except:
            pass