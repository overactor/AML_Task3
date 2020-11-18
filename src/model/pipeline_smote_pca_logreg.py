from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA

from sklearn.model_selection import StratifiedKFold, GridSearchCV
from imblearn.pipeline import Pipeline

def give_model():
    steps = [("smote", SMOTE()), ("pca", PCA()), ("logreg", LogisticRegression())]
    n_splits = 5
    param_grid = {'smote__n_neighbours)' : [3, 5, 7, 9],
                  'smote__random_state' :[0]
                  'pca__n_components': [10, 20, 30, 40, 50],
                  'logreg__penalty': ['elasticnet'],
                  'logreg__C': [1.0, 10.0, 100.0],
                  'logreg__solver': ['saga'],
                  'logreg__class_weight': ['balanced'],
                  'logreg__l1_ratio': [0.0, 1.0],
                  'logreg__random_state' : [0]
    }

    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=0)
    model = GridSearchCV(Pipeline(steps=steps), param_grid=param_grid, cv=cv, scoring='balanced_accuracy', return_train_score=True, n_jobs=-1, verbose=1)
    
    return model