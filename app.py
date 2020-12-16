from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("diabet_rf.pkl", "rb"))



@app.route("/")
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
def predict():
    error = None
    if request.method == "POST":
        
        # Age 
        age = request.form['Age']
        Age = int(age)
        
           
        #Gender (Male or Female)
        gender=request.form['Gender']
        if(gender == 'Male'):
            Gender = 1
            
        else:
            Gender = 0
            
           
        # Polyuria
        polyuria =request.form['Polyuria']
        if(polyuria =='Yes'):
            Polyuria = 1
            
        else:
            Polyuria = 0
            
    
        # Polydipsia
        polydipsia =request.form['Polydipsia']
        if(polydipsia =='Yes'):
            Polydipsia = 1
    
        else:
            Polydipsia = 0
             
          
        # Weight loss
        weight_loss =request.form['Sudden_Weight_Loss']
        if(weight_loss =='Yes'):
            Sudden_Weight_Loss = 1
       
        else:
            Sudden_Weight_Loss= 0
             
             
        # Weakness
        weakness =request.form['Weakness']
        if(weakness =='Yes'):
            Weakness = 1
    
        else:
            Weakness = 0
             
        # Polyphagia
        polyphagia =request.form['Polyphagia']
        if(polyphagia =='Yes'):
            Polyphagia = 1
  
        else:
            Polyphagia = 0
             
        # Genital Thrush
        g_thrush =request.form['Genital_Thrush']
        if(g_thrush =='Yes'):
            Genital_Thrush = 1

        else:
            Genital_Thrush = 0
           
             
         # Visual blurring
        v_blurring =request.form['Visual_Blurring']
        if(v_blurring =='Yes'):
            Visual_Blurring = 1
     
        else:
            Visual_Blurring = 0
             
             
          # Itching
        itching =request.form['Itching']
        if(itching =='Yes'):
            Itching = 1
      
        else:
            Itching = 0
           
             
             
        # Irritability
        irritable =request.form['Irritability']
        if(irritable =='Yes'):
            Irritability = 1
  
        else:
            Irritability = 0
           
         
         # Delayed_Healing
        d_healing =request.form['Delayed_Healing']
        if(d_healing =='Yes'):
            Delayed_Healing = 1

        else:
            Delayed_Healing = 0
             
             
        # partial paresis
        paresis =request.form['Partial_Paresis']
        if(paresis =='Yes'):
            Partial_Paresis = 1
            
        else:
            Partial_Paresis = 0
             
         # Muscle Stiffness
        stiffness =request.form['Muscle_Stiffness']
        if(stiffness =='Yes'):
            Muscle_Stiffness = 1
   
        else:
            Muscle_Stiffness = 0
       
             
         # Alopecia
        alopecia =request.form['Alopecia']
        if(alopecia =='Yes'):
            Alopecia = 1
   
        else:
            Alopecia = 0
            
     
         # Obesity
        obesity =request.form['Obesity']
        if(obesity =='Yes'):
            Obesity = 1
  
        else:
            Obesity = 0
            
             
             
             
        prediction=model.predict([[
            Age,
            Gender,
            Polyuria,
            Polydipsia,
            Sudden_Weight_Loss,
            Weakness,
            Polyphagia,
            Genital_Thrush,
            Visual_Blurring,
            Itching,
            Irritability,
            Delayed_Healing,
            Partial_Paresis,
            Muscle_Stiffness,
            Alopecia,
            Obesity
            
        
        ]])


        output= prediction[0]
        

        if output < .39:
            return render_template('home.html', prediction_text="You are unlikely to be Diabetic with {:.0%} probability detected".format(output))

        elif output > .39 and output < .50:
            return render_template('home.html', prediction_text="You may be at risk, {:.0%} probability detected".format(output))

        else:
            return render_template('home.html', prediction_text="Very likely to be Diabetic, {:.0%} probability detected".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
