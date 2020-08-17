from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
import numpy as np

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class MySimplmputer(TransformerMixin):
    def __init__(self):
        self.si = SimpleImputer(
            missing_values=np.nan,  # os valores faltantes são do tipo ``np.nan`` (padrão Pandas)
            strategy='constant',  # a estratégia escolhida é a alteração do valor faltante por uma constante
            fill_value=0,  # a constante que será usada para preenchimento dos valores faltantes é um int64=0.
            verbose=0,
            copy=True
        )
        pass
    
    def fit(self, X, y=None):
        return self.si.fit(X = X)

    def transform(self, X, y=None):
        data = X.copy()
        return self.si.transform(
            X= data
        )
        
    

class MyOverSampler(TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        max_size = X['PERFIL'].value_counts().max()
        self.max_size = max_size
        return self

    def transform(self, X, y=None):
        data = X.copy()
        lst = [data]
        for class_index, group in data.groupby('PERFIL'):
            lst.append(group.sample(self.max_size-len(group), replace=True))
        frame_new = pd.concat(lst)
        return frame_new
    

