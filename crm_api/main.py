#!/usr/bin/env python3

import os
import pandas as pd
import urllib.request
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
from app import app
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

ALLOWED_EXTENSIONS = set(['xlsx'])
username = app.config['SENDER_EMAIL']  # Email Address from the email you want to send an email
password = app.config['SENDER_EMAIL_PASSWORD']  # Password
server = smtplib.SMTP('')

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function that send email.
def send_mail(username, password, from_addr, to_addrs, msg):
	server = smtplib.SMTP('smtp.gmail.com', '587')
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(username, password)
	result = server.sendmail(from_addr, to_addrs, msg.as_string())
	print("result", result)
	server.quit()

@app.route('/readxlsx', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file.filename == '':
			flash('No file selected')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			#reading uploads excel file
			read_excel = pd.read_excel(file)
			#extracting all emails from excel file
			email_list = read_excel['Emails'].values						
			email_template = open("./templates/email_template.html")
			# Create the body of the message (a HTML version for formatting).
			html = email_template.read()

			for to_addr in email_list:
				msg = MIMEMultipart()
				msg['Subject'] = "AKDS Business Proposal - Outsourcing Services"
				msg['From'] = username
				msg['To'] = to_addr

				# Attach HTML to the email
				body = MIMEText(html, 'html')
				msg.attach(body)

				# Attach Bussiness Proposal to the email
				cover_letter = MIMEApplication(open("AKDS Business Proposal.pdf", "rb").read())
				cover_letter.add_header('Content-Disposition', 'attachment', filename="AKDS.pdf")
				msg.attach(cover_letter)

				try:
					send_mail(username, password, username, to_addr, msg)
					flash("Email successfully sent to", to_addr)
				except Exception:
					print('Exception')
					flash("Email not sent to", to_addr)

		return render_template('success.html', value=email_list)

if __name__ == "__main__":
	app.run(debug=True)
