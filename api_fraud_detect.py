from flask import Flask,jsonify,request
from sklearn.externals import joblib
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    if(request.method == 'POST'):
        data = request.get_json()
        values = [data[x] for x in data]
        log_reg = joblib.load("./log_Regression.pkl")
        return jsonify(log_reg.predict([values]).tolist())
    else:
        return  jsonify({"about":"Error"})

if __name__ == '__main__':
    app.run(debug=True)
