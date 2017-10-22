from bottle import run, template, get, post, request
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()
# server url (example: host:post/data)
@get('/data')
def oidtoSend():
    data=[]
    # grab data from form

    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData('public'),
        cmdgen.UdpTransportTarget(('localhost', 161)),
        '1.3.6.1.4.1.2021.4.5', #Total Ram
        # '1.3.6.1.2.1.1.1',         #System Description
        '1.3.6.1.4.1.2021.4.6',      #total RAM used
      #  '1.3.6.1.4.1.2021.9.1.8.1',  #Path where the disk is mounted
    )
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                )
            )
        else:
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    list1=[name.prettyPrint(),val.prettyPrint()]
                    data.append(list1)
    return {'response': data}
    print (data)
    

# make api call
run(host='localhost', port=8080)
