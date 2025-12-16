import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


X, y = make_classification(
    n_samples=1000,
    n_features=3,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    random_state=42
)


model = RandomForestClassifier()
model.fit(X, y)


with open("credit_fraud.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully to 'credit_fraud.pkl'.")
