import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('C:/Users/PC/Desktop/Programlama/ClassifficationProject/Datasets/flower_dataset.csv')
print(df.head())
print(df.shape)

categorical_columns = ['size', 'fragrance']
existing_categorical_columns = [col for col in categorical_columns if col in df.columns]

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), existing_categorical_columns)
    ],
    remainder='passthrough'
)

# encode the target variable
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

# split the data into features (X) and target (y)
X = df.drop('species', axis=1)
y = df['species']

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# define the models
models = {
    'Random Forest': RandomForestClassifier(n_estimators=50, random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=200, random_state=42),
    'Support Vector Machine': SVC(random_state=42),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=20)
}

# evaluate each model
for model_name, model in models.items():
    # Build a pipeline with preprocessing and model
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('scaler', StandardScaler()),
        ('classifier', model)
    ])
    
    # Train the model
    model_pipeline.fit(X_train, y_train)
    y_pred = model_pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'\nModel: {model_name}')
    print(f'Accuracy: {accuracy * 100:.2f}%')
    
    # convert the label encoded classes back to original species names
    target_names = label_encoder.inverse_transform(range(len(label_encoder.classes_)))
    print('Classification Report:')
    print(classification_report(y_test, y_pred, target_names=target_names))
