import lightgbm as lgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generar un conjunto de datos sintético
X, y = make_classification(n_samples=10000, n_features=20, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear el dataset de LightGBM
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test)

# Configuración del modelo
params = {
    'objective': 'binary',
    'metric': 'binary_logloss',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'n_jobs': -1  # Usar múltiples núcleos para la paralelización
}

# Entrenamiento del modelo
bst = lgb.train(params, train_data, valid_sets=[test_data], num_boost_round=100)
