
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
senders = "daisywndungu@gmail.com"		#Senders Email Address
receivers = "daisywndungu@gmail.com"		#Receiver email Address
msg = MIMEMultipart()
msg['From'] = senders
msg['To'] = receivers
msg['Subject'] = "Ticket Booking"
 
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

try: 
	server = smtplib.SMTP('smtp.gmail.com', 587)	#Call Gmail SMTP server
	server.starttls()
	server.login(senders, "daliken1995")		#Senders authentication
	text = msg.as_string()
	server.sendmail(senders, receivers, text)
	#if se
	print ".................Email sent.............................."
	server.quit()
except:
	print "Error: unable to send email"


