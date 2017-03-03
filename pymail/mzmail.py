#!/usr/bin/python
import sys
import smtplib
import argparse
import logging
import base64


parser = argparse.ArgumentParser(description='Send mail from admin@mznco.net')
parser.add_argument('TO', help='Email will be sent to this address')
parser.add_argument('SUBJECT', help='Specify a subject line')
parser.add_argument('BODY', help='Specify the Body of the email', nargs='*')
args = parser.parse_args()

logging.basicConfig(filename='/var/log/mzmail.log', level=logging.DEBUG) # /var/log/

logging.info(str(sys.argv))

email_from = 'admin@mznco.net'

email_to = [args.TO]
subject = args.SUBJECT
body = " ".join(args.BODY)

smtp_server = 'mail.mznco.net'
smtp_login = 'admin@mznco.net'
smtp_pass = 'PASSWORD'

msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (email_from, ", ".join(email_to), subject) )
msg += "%s\r\n" % body

try:
		server = smtplib.SMTP(smtp_server, 587)
		server.set_debuglevel(1)
		server.ehlo()
		server.starttls()
		server.login(smtp_login, smtp_pass)
		resp = server.sendmail(email_from, email_to, msg)

		logging.info("%s\n" % resp)
		server.quit()
		
except Exception as e:
		logging.error("Exception: %s" % e)
