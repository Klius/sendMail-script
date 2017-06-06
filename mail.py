__author__ = 'Klius'
import smtplib
import codecs
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail(object):

    def __init__(self, fromAddress, toAddress, subject):
        self.fromAd = fromAddress
        self.toAd = toAddress
        self.msg = MIMEMultipart()
        self.msg['Subject'] = subject
        self.msg['From'] = fromAddress
        self.msg['To'] = toAddress
        self.msg["Date"] = formatdate(localtime=True)

    def composePlainBody(self, body):
        self.msg.attach(MIMEText(body, 'plain', 'utf-8'))

    def composeHTMLBody(self, body):
        self.msg.attach(MIMEText(body, 'html', 'utf-8'))

    def attachFile(self, filepath):
        fil = codecs.open(filepath, 'rb', 'utf-8')
        part = MIMEText('text', 'plain', 'utf-8')
        part.set_payload(fil.read())
        part.add_header('Content-Disposition', 'attachment; filename="' + basename(filepath) + '"')
        fil.close()
        self.msg.attach(part)

    def sendMessage(self, serverAddress, username = None, password = None, tls = False):
        server = smtplib.SMTP(serverAddress)
        server.ehlo()
        if tls:
            server.starttls()
        if username is not None and password is not None:
            server.login(username, password)
        server.sendmail(self.fromAd, self.toAd, self.msg.as_string())
        server.quit()
