#!/usr/bin/env python
__author__ = 'Klius'
import mail
import credentials
import getopt
import sys
import argparse


def sendMail(to, subject, body, fromAd):
	credence = credentials.Credentials()
	if not fromAd:
		mailer = mail.Mail(credence.fromAd, to, subject)
	else:
		mailer = mail.Mail(fromAd, to, subject)
	mailer.composeHTMLBody(body)
	mailer.sendMessage(credence.server, credence.username, credence.getpassword())

def sendTextMail(to, subject, body, fromAd):
	credence = credentials.Credentials()
	if not fromAd:
		mailer = mail.Mail(credence.fromAd, to, subject)
	else:
		mailer = mail.Mail(fromAd, to, subject)
	mailer.composePlainBody(body)
	mailer.sendMessage(credence.server, credence.username, credence.getpassword())

def readHTML(path):
	body = open(path)  # '/Users/Klius/Desktop/msg.html')
	msg = body.read()
	body.close()
	return msg


def usage():
	print("PENE")


def main(argv):
	parser = argparse.ArgumentParser(description='Send Mails, plain text or HTML.')
	parser.add_argument("to",help="Destination email address.")
	parser.add_argument("--From",help="Alias for the sender.")
	parser.add_argument("subject", help="Subject of the email.")
	parser.add_argument("--bodyhtml", help="Path of the HTML to use as template for the body of the email.")
	parser.add_argument("--textmessage", help="Text to use as body of the email.")
	args = parser.parse_args()
	
	if bool( args.bodyhtml ):
		htmlmsg = readHTML( args.bodyhtml )
		sendMail( args.to, args.subject, htmlmsg, args.From)
		print True
	elif bool( args.textmessage ):
		sendTextMail(args.to, args.subject, args.textmessage, args.From)
		print True
	else:
		print( "You haven't especified a path to an html nor a plain text body." )
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])
