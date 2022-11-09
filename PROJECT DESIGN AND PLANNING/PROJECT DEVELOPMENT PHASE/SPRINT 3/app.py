from flask import Flask, render_template, request

app = Flask(__name__)

# interface between my server and my application wsgi
import pickle
model = pickle.load(open('WQ_DC_Model.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    print("KIDDO>>")
    return render_template("index.html")

@app.route('/login', methods=['POST','GET'])#binds to an url
def login():
    print("Welcome to lodin")
    p=request.form["Temp"]
    q= request.form["DO"]
    r= request.form["PH"]
    s= request.form["Conductivity"]
    pp = request.form["BOD"]
    qq = request.form["NI"]
    rr = request.form["Fec_col"]
    ss = request.form["Tot_col"]
    #t=request.form
    t=[[float(p),float(q),float(r),float(s),float(pp),float(qq),float(rr),float(ss)]]
    output= model.predict(t)
    print(output)
    myoutput = ""
    if (output[0] < 25 ):
        myoutput = "EXCELLENT and FIT for usage "
    elif (output[0] >25 and output[0] <50):
        myoutput = "GOOD and FIT for usage"
    elif(output[0] >50 and output[0] <75):
        myoutput = "POOR and UNFIT for usage"
    else:
        myoutput = "VERY POOR and UNFIT for usage"
    print(myoutput)

    return render_template("index.html",y = "The WQI predicted is " + str(output[0]) + ". /n The water is " + str(myoutput))   #we can only concatenate string to str

@app.route('/admin')#binds to an url
def admin():
    return "Hey Admin How are you?"

if __name__ == '__main__' :
    app.run(debug=True)
    
