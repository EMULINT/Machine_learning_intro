from flask import Flask,jsonify,request
from sklearn.externals import joblib
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():

    if(request.method == 'POST'):
        data = request.get_json()
        house_price = float(data["area"])
        lin_reg = joblib.load("./linear_reg.pkl")
        return jsonify(lin_reg.predict([[house_price]]).tolist())
    else:
        return  jsonify({"about":"Error"})

if __name__ == '__main__':
    app.run(debug=True)
