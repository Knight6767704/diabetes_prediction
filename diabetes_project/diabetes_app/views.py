from django.shortcuts import render
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,"index.html")
def predict(request):
    return render(request,"predict.html")
def result(request):
    data=pd.read_csv('diabetes.csv')
    X=data[['Glucose','BloodPressure','Insulin','BMI','Age']]
    y=data.Outcome
    model=LogisticRegression()
    model.fit(X,y)
    val1=float(request.GET['Glucose'])
    val2=float(request.GET['BloodPressure'])
    val3=float(request.GET['Insulin'])
    val4=float(request.GET['BMI'])
    val5=float(request.GET['Age'])


    pred=model.predict([[val1,val2,val3,val4,val5]])
    result=""
    if pred==[0]:
        result="<h1>You are not diabetic.</h1>"
    else:
        result="<h1>You are diabetic</h1>"
    return HttpResponse(result)