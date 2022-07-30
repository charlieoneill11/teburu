# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_ML.ipynb.

# %% auto 0
__all__ = ['RegressionResults', 'ClassificationResults']

# %% ../01_ML.ipynb 3
from .core import *
from nbdev.showdoc import *
from fastcore.all import *
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
# classification models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
# regression models
import xgboost as xgb
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# %% ../01_ML.ipynb 5
class RegressionResults:
    "Regression results from model set"
    
    def __init__(self, 
                 X, # Predictor variables
                 y): # Target variables
        self.X, self.y = X, y
        self.lr = linear_model.LinearRegression()
        self.dt = DecisionTreeRegressor()
        self.rf = RandomForestRegressor()
        self.xgboost = xgb.XGBRegressor()
        self.models_list = [self.lr, self.dt, self.rf, self.xgboost]
        
    def report(self):
        "Generate RMSEs for each model"
        rmses = []
        for model in self.models_list:
            reg = Regressor(self.X, self.y, model)
            rmses.append(reg.score())
        return rmses
    
    def df_report(self):
        "Print out a dataframe of results"
        rmses = self.report()
        models = ["linear_regression", "decision_tree", "random_forest", "xgboost"]
        df_dict = {'models': models, 'RMSE': rmses}
        return pd.DataFrame(df_dict)

# %% ../01_ML.ipynb 11
class ClassificationResults:
    "Classification results from model set"
    
    def __init__(self, X, y):
        self.X, self.y = X, y
        self.lr = linear_model.LogisticRegression()
        self.dt = DecisionTreeClassifier()
        self.rf = RandomForestClassifier()
        self.xgboost = xgb.XGBClassifier()
        self.models_list = [self.lr, self.dt, self.rf, self.xgboost]
        
    def report(self):
        "Generate performance metric for each model"
        accuracies, aucs = [], []
        for model in self.models_list:
            reg = Classifier(self.X, self.y, model)
            accuracy, auc = reg.score()
            accuracies.append(accuracy)
            aucs.append(auc)
        return accuracies, aucs
    
    def df_report(self):
        "Print out a dataframe of results"
        accuracies, aucs = self.report()
        models = ["linear_regression", "decision_tree", "random_forest", "xgboost"]
        df_dict = {'models': models, 'Accuracy': accuracies, 'AUC': aucs}
        return pd.DataFrame(df_dict)