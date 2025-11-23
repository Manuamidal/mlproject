import pandas as pd
import os
import sys
from src.exception import CustomException
import numpy as np
from sklearn.metrics import r2_score
import dill
import pickle
from sklearn.model_selection import GridSearchCV
def save_object(file_path, obj):
   
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, Y_train, X_test, Y_test, models,params):
    try:
       report = {}
       for i in range(len(list(models))):
           model=list(models.values())[i]
           param=params[list(models.keys())[i]]
      
           gs=GridSearchCV(model,param,cv=3,)
           gs.fit(X_train,Y_train)
           model.set_params(**gs.best_params_)

           model.fit(X_train, Y_train)
           Y_train_pred = model.predict(X_train)
           Y_test_pred = model.predict(X_test)
           train_model_score = r2_score(Y_train, Y_train_pred)
           report[list(models.keys())[i]] = train_model_score
       return report

    except Exception as e:
        raise CustomException(e, sys)    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)