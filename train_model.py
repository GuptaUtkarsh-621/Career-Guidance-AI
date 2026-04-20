import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Dummy Data for MCA project (Expand this CSV for better results)
data = {
    'academic': [90, 80, 70, 60, 85, 75],
    'coding': [95, 60, 40, 80, 90, 30],
    'comm': [70, 90, 80, 50, 60, 95],
    'logic': [90, 70, 60, 85, 80, 65],
    'role': ['Data Scientist', 'Manager', 'HR', 'SDE', 'AI Engineer', 'Marketing']
}
df = pd.DataFrame(data)

X = df.drop('role', axis=1)
y = df['role']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

joblib.dump(model, 'models/random_forest_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
print("Model and Scaler saved!")