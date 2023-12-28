from flask import Flask, redirect, render_template, request, jsonify, url_for
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import database
import encryDecrypt

app = Flask(__name__)

# Load the models using pickle
with open('./model/model.pickle', 'rb') as file:
    modelGetName = pickle.load(file)
    modelGetPrerequisites = pickle.load(file)
    modelGetSkill = pickle.load(file)
    modelGetConse = pickle.load(file)
    modelGetMitigation = pickle.load(file)
    modelGetHL = pickle.load(file)
    tfidf_vectorizer = pickle.load(file)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/registeruser', methods=['POST'])
def registeruser():
    if request.method == 'POST':
        name=request.form['fullname']
        email=request.form['email']
        password=request.form['password']

        eemail=encryDecrypt.encrypt_des('arav',email)
        epassword=encryDecrypt.encrypt_des('arav',password)

        tf=database.registerUserIntoDb(name,eemail,epassword)
        if(tf):
            response_data = {'message': 'Registration successful\nNow you can Login'}
            return jsonify(response_data)
        else:
            print("Unable to insert")


@app.route('/validatelogin', methods=['POST'])
def validatelogin():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        
        eemail=encryDecrypt.encrypt_des('arav',email)
        epassword=encryDecrypt.encrypt_des('arav',password)
       
        checklogin = database.login_user(eemail, epassword)

        if checklogin:
            # Successful login, redirect to homepage without including the user's name in the URL
            return jsonify({'success': True, 'redirect_url': url_for('homepage',x=checklogin)})
        else:
            # Invalid login
            response_data = {'success': False, 'message': 'Invalid email or password. Please try again.'}
            return jsonify(response_data)

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        threat_text = request.form['threatTextarea']
       
        new_text_data = [threat_text]
        new_text_tfidf = tfidf_vectorizer.transform(new_text_data)

        Name_probabilities = modelGetName.predict_proba(new_text_tfidf)
        Pre_probabilities = modelGetPrerequisites.predict_proba(new_text_tfidf)
        Skill_probabilities = modelGetSkill.predict_proba(new_text_tfidf)
        Conse_probabilities = modelGetConse.predict_proba(new_text_tfidf)
        Miti_probabilities = modelGetMitigation.predict_proba(new_text_tfidf)
        HL_probabilities = modelGetHL.predict_proba(new_text_tfidf)

        top3_indicesName = np.argsort(Name_probabilities, axis=1)[:, -3:][:, ::-1]
        top3_labelsName = modelGetName.classes_[top3_indicesName]

        top3_indicesPre = np.argsort(Pre_probabilities, axis=1)[:, -3:][:, ::-1]
        top3_labelsPre = modelGetPrerequisites.classes_[top3_indicesPre]

        top3_indicesSkill = np.argsort(Skill_probabilities, axis=1)[:, -3:][:, ::-1]
        top3_labelsSkill = modelGetSkill.classes_[top3_indicesSkill]

        top3_indicesConse = np.argsort(Conse_probabilities, axis=1)[:, -3:][:, ::-1]
        top3_labelsConse = modelGetConse.classes_[top3_indicesConse]

        top3_indicesMiti = np.argsort(Miti_probabilities, axis=1)[:, -3:][:, ::-1]
        top3_labelsMiti = modelGetMitigation.classes_[top3_indicesMiti]

        top3_indicesHL = np.argsort(HL_probabilities, axis=1)[:, -3:][:, ::-1]
        top3_labelsHL = modelGetHL.classes_[top3_indicesHL]

        mitigation=[]
        new_text_tfidf = tfidf_vectorizer.transform([top3_labelsMiti[0][0]])
        Mitigati = modelGetName.predict(new_text_tfidf)
        mitigation.append(Mitigati[0])

        new_text_tfidf = tfidf_vectorizer.transform([top3_labelsMiti[0][1]])
        Mitigati = modelGetName.predict(new_text_tfidf)
        mitigation.append(Mitigati[0])

        new_text_tfidf = tfidf_vectorizer.transform([top3_labelsMiti[0][2]])
        Mitigati = modelGetName.predict(new_text_tfidf)
        mitigation.append(Mitigati[0])


        loa=[top3_labelsHL[0][0],top3_labelsHL[0][1],top3_labelsHL[0][2]]
        value_mapping = {1: 'Low', 2: 'Medium', 3: 'High'}
        new_list = [value_mapping[value] for value in loa]

        return render_template('predict.html',
                               showDesc=threat_text, 
                               detailName=top3_labelsName,
                               detailPre=top3_labelsPre,
                               detailSkill=top3_labelsSkill,
                               detailConse=top3_labelsConse,
                               miti=mitigation,
                               Loa=new_list)

if __name__ == '__main__':
    app.run(debug=True)
