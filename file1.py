from flask import Flask, render_template,request
import pickle
file1=Flask(__name__, template_folder="template")
model=pickle.load(open("model/height.pkl","rb"))
@file1.route("/")
def home():
    return render_template("index.html")

@file1.route("/predict",methods=["post"])
def pred():
    data=float(request.form.get("height"))
    feature=[[data]]
    prediction=model.predict(feature)
    return render_template("index.html",predicted_data=f"weight is {prediction}")

if __name__=="__main__":
    file1.run(debug=True)