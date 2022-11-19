import requests
from flask import Flask, render_template, request

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "h2vJ937H5pAJq9TjZs1TKvsBeVKaTkrFIYx4QQpAOoQ-"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)  # interface between my server and my application wsgi


@app.route('/')  # binds to an url
def helloworld():
    return render_template("index.html")


@app.route('/login', methods=['POST'])  # binds to an url
def login():
    print("Welcome to login")
    aa = request.form["year"]
    q = request.form["DO"]
    r = request.form["PH"]
    s = request.form["Conductivity"]
    pp = request.form["BOD"]
    qq = request.form["NI"]
    ss = request.form["Tot_col"]

    # t=request.form
    t = [[int(aa), float(q), float(r), float(s), float(pp), float(qq), float(ss)]]
    # output= model.predict(t)
    # print(output)

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [['f0','f1','f2','f3','f4','f5','f6']],
                                       "values":t }]}

    response_scoring = requests.post(
        'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/68c0c00b-cf33-4ac9-a40f-e4835b4935e4/predictions?version=2022-11-18',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    #print(response_scoring.json())
    pred=response_scoring.json()
    output = pred['predictions'][0]['values'][0][0]
    print(output)
    if (output >= 95 and output <= 100):
        return render_template("index.html", y="Excellent. The WQI predicted value is " + str(output))  # we can only concatenate string to str
    elif (output >= 89 and output <= 94):
        return render_template("index.html", y="Very Good. The WQI predicted value is " + str(output))  # we can only concatenate string to str
    elif (output >= 80 and output <= 88):
        return render_template("index.html", y="Good. The WQI predicted value is " + str(output))  # we can only concatenate string to str
    elif (output >= 65 and output <= 79):
        return render_template("index.html", y="Fair. The WQI predicted value is " + str(output))  # we can only concatenate string to str
    elif (output >= 45 and output <= 64):
        return render_template("index.html", y="Marginal. The WQI predicted value  is " + str(output))  # we can only concatenate string to str
    else:
        return render_template("index.html", y="Poor. The WQI predicted value is " + str(output))  # we can only concatenate string to str


@app.route('/admin')  # binds to an url
def admin():
    return "Hey Admin How are you?"


if __name__ == '__main__':
    app.run(debug=False)

