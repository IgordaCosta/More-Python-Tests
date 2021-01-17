import dns.resolver

import socket
import smtplib


def CheckifEmailExists(mxRecord, addressToVerify,myEmail):
    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail(myEmail)
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        print('Success')
    else:
        print('Bad')




def CheckIfThisEmailExist(emailDNS,addressToVerify,myEmail):
    # records = dns.resolver.query(emailDNS, 'MX')
    records = dns.resolver.resolve(emailDNS, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    # print(records)
    # print('records above')

    # print(mxRecord)

    # print('mxRecord above')

    CheckifEmailExists(mxRecord=mxRecord, addressToVerify=addressToVerify,myEmail=myEmail)



addressToVerify= 'renovacao@aconteceimobiliaria.com.br'

myEmail='mye456@gmail.com'

emailDNS='aconteceimobiliaria.com.br'


CheckIfThisEmailExist(emailDNS,addressToVerify,myEmail)



