import pandas as pd
import sqlite3
class DistanceJour:
    def __init__(self,nom,D):
        self.D=D
        self.nom=nom
        pass
    def indistr(self):
        #################################
        nom=self.nom
        D=self.D
        file = nom+'.db'
        
        #######################################################
        df_0 = pd.DataFrame({'DJ_d' : D[0]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS DJ_D (DJ_d REAL)"
        cur.execute(query)
        df_0.to_sql('DJ_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #################################
        df_1 = pd.DataFrame({'DJ_j' : D[1]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS DJ_J (DJ_j TEXT)"
        cur.execute(query)
        df_1.to_sql('DJ_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_2 = pd.DataFrame({'DS_d' : D[2]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS DS_D (DS_d REAL)"
        cur.execute(query)
        df_2.to_sql('DS_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_3 = pd.DataFrame({'DS_j' : D[3]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS DS_J (DS_j TEXT)"
        cur.execute(query)
        df_3.to_sql('DS_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_4 = pd.DataFrame({'DM_d' : D[4]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS DM_D (DM_d REAL)"
        cur.execute(query)
        df_4.to_sql('DM_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_5 = pd.DataFrame({'DM_j' : D[5]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS DM_J (DM_j TEXT)"
        cur.execute(query)
        df_5.to_sql('DM_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()

class Gra_J:
    def __init__(self,nom):
        self.nom=nom
    def DJ_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM DJ_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM DJ_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
        return nom,z,z_1
    def DS_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM DS_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM DS_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
        return nom,z,z_1
    def DM_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM DM_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM DM_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
        return nom,z,z_1

class Temps_M:
    def __init__(self,nom,D):
        self.D=D
        self.nom=nom
        pass
    def indistr(self):
        #################################
        nom=self.nom
        D=self.D
        file = nom+'.db'
        
        #############################################################################
        df_0 = pd.DataFrame({'TMJ_d' : D[0]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMJ_D (TMJ_d REAL)"
        cur.execute(query)
        df_0.to_sql('TMJ_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #################################
        df_1 = pd.DataFrame({'TMJ_j' : D[1]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMJ_J (TMJ_j TEXT)"
        cur.execute(query)
        df_1.to_sql('TMJ_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_2 = pd.DataFrame({'TMJ_t' : D[2]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMJ_T (TMJ_t TEXT)"
        cur.execute(query)
        df_2.to_sql('TMJ_T', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        ############################################################################
        df_0 = pd.DataFrame({'TMS_d' : D[3]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMS_D (TMS_d REAL)"
        cur.execute(query)
        df_0.to_sql('TMS_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #################################
        df_1 = pd.DataFrame({'TMS_j' : D[4]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMS_J (TMS_j TEXT)"
        cur.execute(query)
        df_1.to_sql('TMS_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_2 = pd.DataFrame({'TMS_t' : D[5]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMS_T (TMS_t TEXT)"
        cur.execute(query)
        df_2.to_sql('TMS_T', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        ############################################################################
        df_0 = pd.DataFrame({'TMM_d' : D[6]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMM_D (TMM_d REAL)"
        cur.execute(query)
        df_0.to_sql('TMM_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #################################
        df_1 = pd.DataFrame({'TMM_j' : D[7]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMM_J (TMM_j TEXT)"
        cur.execute(query)
        df_1.to_sql('TMM_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_2 = pd.DataFrame({'TMM_t' : D[8]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TMM_T (TMM_t TEXT)"
        cur.execute(query)
        df_2.to_sql('TMM_T', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()

class Temps_IM:
    def __init__(self,nom,D):
        self.D=D
        self.nom=nom
        pass
    def indistr(self):
        #################################
        nom=self.nom
        D=self.D
        file = nom+'.db'
        
        #############################################################################
        df_0 = pd.DataFrame({'TIMJ_d' : D[0]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMJ_D (TIMJ_d REAL)"
        cur.execute(query)
        df_0.to_sql('TIMJ_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #################################
        df_1 = pd.DataFrame({'TIMJ_j' : D[1]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMJ_J (TIMJ_j TEXT)"
        cur.execute(query)
        df_1.to_sql('TIMJ_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_2 = pd.DataFrame({'TIMJ_t' : D[2]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMJ_T (TIMJ_t TEXT)"
        cur.execute(query)
        df_2.to_sql('TIMJ_T', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        ############################################################################
        df_0 = pd.DataFrame({'TIMS_d' : D[3]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMS_D (TIMS_d REAL)"
        cur.execute(query)
        df_0.to_sql('TIMS_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #################################
        df_1 = pd.DataFrame({'TIMS_j' : D[4]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMS_J (TIMS_j TEXT)"
        cur.execute(query)
        df_1.to_sql('TIMS_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_2 = pd.DataFrame({'TIMS_t' : D[5]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMS_T (TIMS_t TEXT)"
        cur.execute(query)
        df_2.to_sql('TIMS_T', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        ############################################################################
        df_0 = pd.DataFrame({'TIMM_d' : D[6]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMM_D (TIMM_d REAL)"
        cur.execute(query)
        df_0.to_sql('TIMM_D', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        #################################
        df_1 = pd.DataFrame({'TIMM_j' : D[7]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMM_J (TIMM_j TEXT)"
        cur.execute(query)
        df_1.to_sql('TIMM_J', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
        
        #################################
        df_2 = pd.DataFrame({'TIMM_t' : D[8]})
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"CREATE TABLE IF NOT EXISTS TIMM_T (TIMM_t TEXT)"
        cur.execute(query)
        df_2.to_sql('TIMM_T', con, if_exists = 'replace', index = False)
        con.commit()
        cur.close()
    
        
class GTM_J:
    def __init__(self,nom):
        self.nom=nom
    def TMJ_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMJ_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMJ_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMJ_T"
        c_2 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        z_2 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
            z_2.append(c_2[i][0])
        return nom,z , z_1, z_2
    def TMS_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMS_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMS_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMS_T"
        c_2 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        z_2 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
            z_2.append(c_2[i][0])
        return nom,z , z_1, z_2
    def TMM_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMM_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMM_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TMM_T"
        c_2 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        z_2 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
            z_2.append(c_2[i][0])
        return nom,z , z_1, z_2
    
class GTIM_J:
    def __init__(self,nom):
        self.nom=nom
    def TMJ_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMJ_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMJ_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMJ_T"
        c_2 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        z_2 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
            z_2.append(c_2[i][0])
        return nom,z , z_1, z_2
    def TMS_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMS_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMS_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMS_T"
        c_2 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        z_2 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
            z_2.append(c_2[i][0])
        return nom,z , z_1, z_2
    def TMM_D(self):
        nom=self.nom
        file = nom+'.db'
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMM_D"
        c = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMM_J"
        c_1 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        con = sqlite3.connect(file)
        cur = con.cursor()
        query = f"SELECT * FROM TIMM_T"
        c_2 = cur.execute(query).fetchall()
        con.commit()
        cur.close()
        
        z=[]
        z_1 = []
        z_2 = []
        for i in range(len(c)):
            z.append(c[i][0])
            z_1.append(c_1[i][0])
            z_2.append(c_2[i][0])
        return nom,z , z_1, z_2
