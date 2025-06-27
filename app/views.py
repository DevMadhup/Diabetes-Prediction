from django.shortcuts import render
from .forms import DiabetesForm
import numpy as np
import joblib
from django.http import HttpResponse
import csv

model = joblib.load('diabetes_model.pkl')

def index(request):
    result = None
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = np.array([[data['Pregnancies'], data['Glucose'], data['BloodPressure'], data['BMI'], data['Age']]])
            prediction = model.predict(input_data)[0]
            result = 'Diabetic' if prediction else 'Not Diabetic'
            request.session['input'] = data
            request.session['result'] = result
    else:
        form = DiabetesForm()
    return render(request, 'app/index.html', {'form': form, 'result': result})

def download_report(request):
    input_data = request.session.get('input')
    result = request.session.get('result')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    writer = csv.writer(response)
    writer.writerow(['Pregnancies', 'Glucose', 'BloodPressure', 'BMI', 'Age', 'Result'])
    writer.writerow([
        input_data['Pregnancies'], input_data['Glucose'], input_data['BloodPressure'],
        input_data['BMI'], input_data['Age'], result
    ])
    return response