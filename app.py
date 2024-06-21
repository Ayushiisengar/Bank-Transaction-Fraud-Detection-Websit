from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize prediction history list
prediction_history = []

# Load the model and necessary data
dataset = pd.read_csv('creditcard.csv')
valid = dataset[dataset.Class == 0]
fraud = dataset[dataset.Class == 1]
sample_valid = valid.sample(n=len(fraud))
balanced_dataset = pd.concat([sample_valid, fraud], axis=0)

X = balanced_dataset.drop('Class', axis=1)
y = balanced_dataset['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2, test_size=0.2, stratify=y)

# Initialize models
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

# Fit models
for model in models.values():
    model.fit(X_train, y_train)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('model_selection'))
        else:
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html', message='')

@app.route('/model_selection', methods=['GET', 'POST'])
def model_selection():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))

    if request.method == 'POST':
        selected_model = request.form['model']
        session['selected_model'] = selected_model
        return redirect(url_for('options'))
    return render_template('model_selection.html', models=models.keys())

@app.route('/options', methods=['GET', 'POST'])
def options():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if request.form['submit'] == 'Predict':
            return redirect(url_for('predict'))
        elif request.form['submit'] == 'History':
            return redirect(url_for('history'))
    return render_template('options.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))

    if request.method == 'POST':
        features = [float(request.form[f'feature{i}']) for i in range(1, 7)]
        selected_model = session.get('selected_model')
        model = models[selected_model]
        prediction = model.predict([features])[0]
        result = 'Valid Transaction' if prediction == 0 else 'Fraudulent Transaction'
        prediction_history.append((features, result, selected_model))
        return render_template('result.html', result=result)
    return render_template('predict.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('selected_model', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
