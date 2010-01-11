import logs
import messaging

f=open('e:\\QSMS.txt','r')
message = f.readline().decode('utf-8')

lastmiss=logs.calls(mode='missed')[0]
lastin=logs.calls(mode='in')[0]

if lastmiss["time"]>lastin["time"]:
	messaging.sms_send(lastmiss["number"], message)
else:
	messaging.sms_send(lastin["number"], message)

