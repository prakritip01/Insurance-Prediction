from flask import Flask, render_template, request
import pickle


app= Flask(__name__)
model = pickle.load(open('insurance.pickle', 'rb'))

@app.route('/',methods=['GET'])

def Home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            gender = request.form['gender']
            if (gender == 'Male'):
                gender = 1
            else:
                gender = 0
            smoker= request.form['smoker']
            if (smoker == 'yes'):
                smoker = 1
            else:
                smoker = 0
            region = request.form['region']
            if (region == 'southwest'):
                region = southwest
            elif (region == 'southeast'):
                region = southeast
            elif (region == 'notheast'):
                region = northheast
            else:
                region = northwest

            filename = "insurance.pickle"

            prediction = model.predict([[age,bmi, children, gender, smoker, region]])
            output = round(prediction[0],2)

            return render_template('index.html', prediction_text= 'The total Premium will be Rs.{}'.format(output))
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)