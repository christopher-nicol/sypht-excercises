import re
from flask import Flask, redirect, url_for, render_template, request, session
import requests
from base64 import b64encode
from sypht.client import SyphtClient
from json2html import *
from credentials import *

sc = SyphtClient(CLIENT_ID, CLIENT_SECRET)

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]

    with open(uploaded_file.filename, 'rb') as f:
        fid = sc.upload(f, products=["invoices:2"])

    results = sc.fetch_results(fid)

    issuerName = results['issuer.name']
    issuerABN = results['issuer.ABN']
    invoiceDueDate = results['invoice.dueDate']
    recipientName = results['recipient.name']
    recipientServiceAddress = results['recipient.serviceAddress']

    session['results_converted'] = json2html.convert(json=results)

    return render_template('summary.html', issuerName=issuerName, issuerABN=issuerABN, invoiceDueDate=invoiceDueDate, recipientName=recipientName, recipientServiceAddress=recipientServiceAddress)

@app.route('/results')
def results():
    return render_template('results.html', results_converted=session["results_converted"])


if __name__ == '__main__':
    app.run(debug=True)