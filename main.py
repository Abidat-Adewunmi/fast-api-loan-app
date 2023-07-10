from fastapi import FastAPI
import uvicorn
import pickle


app = FastAPI(debug=True)

@app.get('/')
def loan():
    return {'text':'Loan Prediction Solution'}


@app.get('/predict')
def predict(Age:str, LoanAmount:str, ApplicantIncome:str, Credit_History:str, Gender:str, Married:str, Property_Area:str):

    model = pickle.load(open('loan_app_prediction_model.pkl','rb'))
    makeprediction = model.predict([[Age, LoanAmount, ApplicantIncome, Credit_History, Gender, Married, Property_Area]])
    output = round (makeprediction[0],2)

    return {"You Can Approve Loan for {}".format(output)}

if __name__ == '__main__':
    uvicorn.run(app)