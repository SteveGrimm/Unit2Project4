# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from constants import ESTIMATOR, PREDS_DEST, PATH

def load_data(path):
    return pd.read_csv(path)

def salar_sales_binarizer(data):
    data['salary'] = np.where(data['salary'].isin(['low','medium']), 1, 0)
    data['sales'] = np.where(data['sales'].isin(['RandD','management']), 0, 1)

def data_splitter(data):
    features = data.drop(['id','churn'],axis=1)
    target = data['churn']
    return features, target

def predict_on_data(ESTIMATOR, X, y):
    predictions = ESTIMATOR.fit(X, y).predict(X)
    return predictions

def write_predictions_csv(y_pred):
    pd.DataFrame(y_pred).to_csv(PREDS_DEST)

def main():
    X_train, y_train = data_splitter(salar_sales_binarizer(load_data(PATH)))
    write_predictions_csv(predict_on_data(ESTIMATOR, X_train, y_train))

if __name__ == "__main__":
    main()

