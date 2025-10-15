# models.py
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn import metrics

# Train models
dtree = DecisionTreeClassifier()
rf = RandomForestClassifier()
knn = KNeighborsClassifier()
xgb = XGBClassifier()

dtree.fit(X_train, y_train)
rf.fit(X_train, y_train)
knn.fit(X_train, y_train)
xgb.fit(X_train, y_train)

# Evaluate models
print(metrics.accuracy_score(y_test, dtree.predict(X_test)))
print(metrics.accuracy_score(y_test, rf.predict(X_test)))
print(metrics.accuracy_score(y_test, knn.predict(X_test)))
print(metrics.accuracy_score(y_test, xgb.predict(X_test)))

# Identify the best-performing model
best_model = xgb
# models.py (continued)
# Evaluate the best-performing model (XGBoost)
print(metrics.confusion_matrix(y_test, xgb.predict(X_test)))
print(metrics.precision_score(y_test, xgb.predict(X_test)))
print(metrics.recall_score(y_test, xgb.predict(X_test)))
