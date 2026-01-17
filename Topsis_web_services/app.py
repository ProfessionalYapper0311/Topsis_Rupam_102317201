import os
import smtplib
import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


SENDER_EMAIL = "rbiswas_be23@thapar.edu"   
SENDER_PASSWORD = "lvmk vjve wehx vwvm" 


def calculate_topsis(file_path, weights, impacts):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
    except:
        return None, "Error reading file."

    if df.shape[1] < 3:
        return None, "File must have at least 3 columns."

    try:
        weights = [float(w) for w in weights.split(',')]
        impacts = impacts.split(',')
    except:
        return None, "Weights/Impacts format error."

    data = df.iloc[:, 1:].values

    if not np.issubdtype(data.dtype, np.number):
         return None, "Columns from 2nd onwards must be numeric."

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        return None, "Count of weights/impacts mismatch with columns."
    
    if not all(i in ['+', '-'] for i in impacts):
        return None, "Impacts must be + or -."


    col_sums = np.sqrt((data**2).sum(axis=0))
    col_sums[col_sums == 0] = 1
    norm_data = data / col_sums

    weighted_data = norm_data * weights
    

    ideal_best = []
    ideal_worst = []
    for i in range(len(weights)):
        if impacts[i] == '+':
            ideal_best.append(weighted_data[:, i].max())
            ideal_worst.append(weighted_data[:, i].min())
        else:
            ideal_best.append(weighted_data[:, i].min())
            ideal_worst.append(weighted_data[:, i].max())

    S_plus = np.sqrt(((weighted_data - ideal_best)**2).sum(axis=1))
    S_minus = np.sqrt(((weighted_data - ideal_worst)**2).sum(axis=1))

    total = S_plus + S_minus
    score = np.divide(S_minus, total, out=np.zeros_like(S_minus), where=total!=0)
    
    df['Topsis Score'] = score
    df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)
    
    output_path = os.path.join(UPLOAD_FOLDER, 'result.csv')
    df.to_csv(output_path, index=False)
    return output_path, "Success"

def send_email(receiver_email, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = "Your Topsis Result"
    msg.attach(MIMEText("Hello,\n\nPlease find the attached Topsis result file.\n\nBest Regards,\nTopsis Service", 'plain'))


    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename=result.csv")
    msg.attach(part)


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email Error: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        file = request.files['inputFile']
        weights = request.form['weights']
        impacts = request.form['impacts']
        email = request.form['email']

        if not file:
            return render_template('index.html', message="No file uploaded", status="error")


        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        result_path, status_msg = calculate_topsis(filepath, weights, impacts)
        
        if result_path is None:
            return render_template('index.html', message=status_msg, status="error")

        if send_email(email, result_path):
            return render_template('index.html', message=f"Success! Result sent to {email}", status="success")
        else:
            return render_template('index.html', message="Result generated but Email failed. Check server logs.", status="error")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)