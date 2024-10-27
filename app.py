from flask import Flask, request, render_template
from services import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/income_tax')
def Tax():
    return render_template('income_tax.html')

@app.route('/calculateIncome', methods=['POST'])
def calculate_incomeTax():
    # Get form data from the user
    income = float(request.form['income'])
    deductions = request.form.get('deductions', 0)

    # Calculate the tax
    tax = calculate_tax(income, deductions)

    # Display the tax result to the user
    return render_template('result.html', income=income, deductions=deductions, tax=tax)

@app.route('/TypesOfTaxes')
def  TypesOfTaxes():
    return render_template('TypesOfTaxes.html')

@app.route('/gst')
def  gst():
    return render_template('gst.html')
@app.route('/calculateGST', methods = ['POST'])
def GST():
    price = float(request.form.get('amount'))
    percentage = float(request.form.get('percentage'))
    tax = calculate_GST(price,percentage)
    return render_template('result_universal.html',tax = tax)
    
@app.route('/corporate_tax')
def corporate():
    return render_template('corporate_tax.html')



if __name__ == '__main__':
    app.run(debug=True)
