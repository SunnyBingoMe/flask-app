from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import pickle
with open('forecast_model.pckl', 'rb') as fin:
    m2 = pickle.load(fin)

app = Flask(__name__)
CORS(app)
#@app.route("/katana-ml/api/v1.0/forecast/ironsteel", methods=['POST'])
@app.route("/ai-ops-ns/flask-app", methods=['POST'])
def predict():
    horizon = int(request.json['horizon'])
    
    future2 = m2.make_future_dataframe(periods=horizon)
    forecast2 = m2.predict(future2)
    
    data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:]
    
    ret = data.to_json(orient='records', date_format='iso')
    
    return ret

@app.route("/ai-ops-ns/flask-app", methods=['GET'])
def predict2():
    horizon = 5 # int(request.json['horizon'])
    
    future2 = m2.make_future_dataframe(periods=horizon)
    forecast2 = m2.predict(future2)
    
    data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:]
    
    ret = data.to_json(orient='records', date_format='iso')
    
    return ret

# running REST interface, port=... for direct test
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)

