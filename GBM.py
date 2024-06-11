import lightgbm as lgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
#minimizar una función de pérdida específica 
#lightgbm: Gradienete rapido--arboles de decisiones que utiliza para clasificar
#agrupa valores de características continuos en bina o contenedores separados
# Generar un conjunto de datos sintético
X, y = make_classification(n_samples=10000, n_features=20, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear el dataset de LightGBM
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test)

# Configuración del modelo
params = {
    'objective': 'binary',#clasificacion binaria
    'metric': 'binary_logloss',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'n_jobs': -1  # Usar múltiples núcleos para la paralelización
}

# Entrenamiento del modelo
bst = lgb.train(params, train_data, valid_sets=[test_data], num_boost_round=100)
#la métrica de evaluación que se utilizará durante el entrenamiento y la validación del #modelo. binary_logloss--> es la función de pérdida log-loss 
#'gbdt' significa Gradient Boosting Decision Tree (Árbol de Decisión de Gradiente #Boosting), que es el algoritmo principal de LightGBM para construir el modelo GBM.
#learning_rate puede ayudar a prevenir el sobreajuste
#seleccionarán aleatoriamente para construir cada árbol de decisión.feacture_fraction
