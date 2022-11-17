from flask import Flask, render_template, request

app = Flask(__name__)

# interface between my server and my application wsgi
import pickle
model = pickle.load(open('WaterQuality_RFModel.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    print("KIDDO>>")
    return render_template("index.html")

@app.route('/login', methods=['POST','GET'])#binds to an url
def login():
    print("Welcome to login")
    aa= request.form["year"]
    q= request.form["DO"]
    r= request.form["PH"]
    s= request.form["Conductivity"]
    pp = request.form["BOD"]
    qq = request.form["NI"]
    ss = request.form["Tot_col"]

    #t=request.form
    t=[[int(aa),float(q),float(r),float(s),float(pp),float(qq),float(ss)]]
    output= model.predict(t)
    print(output)
    output=output[[0]]
    if (output>=95 and output<=100):
        return render_template("index.html", y="Excellent. The WQI predicted value is " + str(output))  # we can only concatenate string to str
    elif (output>=89 and output<=94):
        return render_template("index.html", y="Very Good. The WQI predicted value is " + str(output))  # we can only concatenate string to str
    elif(output>=80 and output<=88):
        return render_template("index.html", y="Good. The WQI predicted value is " + str(output))  # we can only concatenate string to str
    elif (output >=65 and output <=79):
        return render_template("index.html", y="Fair. The WQI predicted value is " + str(output))  # we can only concatenate string to str
    elif (output >=45 and output <=64):
        return render_template("index.html", y="Marginal. The WQI predicted value  is " + str(output))  # we can only concatenate string to str
    else:
        return render_template("index.html", y="Poor. The WQI predicted value is " + str(output))  # we can only concatenate string to str


@app.route('/admin')#binds to an url
def admin():
    return "Hey Admin How are you?"

if __name__ == '__main__' :
    app.run(debug=True)
    
