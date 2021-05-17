from keras.models import load_model
from flask import Flask, render_template, request
app=Flask("Diapred")
model=load_model("dia_model.h5")
@app.route("/home")
def home():
    return render_template("first_model_page.html")

@app.route("/data", methods=["GET"])
def data():
      n1=(request.args.get("x1"))
      n2=(request.args.get("x2"))
      n3=(request.args.get("x3")) 
      n4=(request.args.get("x4"))
      n5=(request.args.get("x5")) 
      n6=(request.args.get("x6"))
      n7=(request.args.get("x7"))
      n8=(request.args.get("x8"))

      
      out=model.predict([[int(n1),int(n2),int(n3),int(n4),int(n5),float(n6),float(n7),int(n8)]])
      if (str(round(out[0][0])))=='0':
          value="The Person is Diabetic Person, Stay Healthy and take advise from doctors"
      else:
          value="The person is not Diabetic, Do Exercises Regularly and stay Healthy"    
      return render_template("prediction_page.html", value=value)      
      


app.run(debug=True)
