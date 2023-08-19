from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def send_email():
    if request.method == "POST":
        recipient = request.form.get("recipient")
        subject = "Email Notification"
        message = request.form.get("message")

        sender_email = "ishwarya34bala@gmail.com" 
        sender_password = "pvfwddazmmbhfghq"     

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())
            server.quit()
            return "Email sent successfully!"
        except Exception as e:
            return f"An error occurred: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
