
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import pickle
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
def preprocessing(df):
    df.drop(["name","nrOfPictures"],axis="columns",inplace=True)  
    df["seller"].replace(["privat","gewerblich"],[1,0],inplace=True)
    df["offerType"].replace(["Angebot","Gesuch"],[1,0],inplace=True)
    df["vehicleType"] =LabelEncoder().fit_transform(df["vehicleType"].astype(str))
    df["fuelType"] =LabelEncoder().fit_transform(df["fuelType"].astype(str))
    df["gearbox"] =LabelEncoder().fit_transform(df["gearbox"].astype(str))
    df["notRepairedDamage"] =LabelEncoder().fit_transform(df["notRepairedDamage"].astype(str))
    df["brand"] =LabelEncoder().fit_transform(df["brand"].astype(str))
    df["model"] =LabelEncoder().fit_transform(df["model"].astype(str))
    df["abtest"] =LabelEncoder().fit_transform(df["abtest"].astype(str))
    return df


# In[2]:


def training(df):
    df = preprocessing(df)
    #train with all data
    y = df["price"]
    X = df.drop(["price"], axis='columns')
    sc= StandardScaler()
    X=sc.transform(X)
    filename = 'standardscale1.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(X, file)

    dummyRow = pd.DataFrame(np.zeros(len(X.columns)).reshape(1, len(X.columns)), columns=X.columns)    
    dummyRow.to_csv("dummyRow.csv", index=False)
    model = RandomForestRegressor(n_estimators=89, min_samples_split=3, min_samples_leaf=4, max_features="sqrt", max_depth=35, bootstrap=False)
    model.fit(X, y)
    pkl_filename = "finalized_model2.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)


# In[3]:


def pred(ob):
    print(1)
    d1 = ob.to_dict()
    df = pd.DataFrame(d1, index=[0])
    print("**"*50)
    print(df.head())
    df = preprocessing(df)    
    print("--"*50)
    print(df.head())
    dummyrow_filename = "./dummyRow.csv"
    dummyrow_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), dummyrow_filename)    
    print(2)
    df2 = pd.read_csv(dummyrow_filename)    
    for c1 in df.columns:
        df2[c1] = df[c1]        
    print("=="*50)
    print(df2.head())        
    pkl_filename = "./finalized_model2.pkl"
    pkl_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), pkl_filename)
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)
    pred = model.predict(df2)
    return pred


# In[4]:

if __name__ == "__main__":
    df = pd.read_csv("autos.csv")
    training(df)


# In[5]:


#     sc = StandardScaler()
#     sc.fit(X)
#     pkl_filename2 = "pickle_scaler.pkl"
#     with open(pkl_filename2, 'wb') as file:
#         pickle.dump(sc, file)


#     pkl_filename2 = "./pickle_scaler.pkl"
#     pkl_filename2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), pkl_filename2)
#     with open(pkl_filename2, 'rb') as file:
#         sc = pickle.load(file)

