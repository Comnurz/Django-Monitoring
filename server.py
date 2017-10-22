from bottle import run, template, get, post, request
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def oid(oids):
    data=[]
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData('public'),
        cmdgen.UdpTransportTarget(('localhost', 161)),
        *oids,
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
    return data

# server url (example: host:post/data)
@get('/ramdata')
def ram():
    oids=['1.3.6.1.4.1.2021.4.5','1.3.6.1.4.1.2021.4.6']
#               total Ram          ,    total ram used
    data=oid(oids)
    return {'response': data}


@get('/cpudata')
def cpu():
    oids=['1.3.6.1.4.1.2021.10.1.3.1','1.3.6.1.4.1.2021.10.1.3.2']
#           1 minute load               5 minute load
    data=oid(oids)
    return {'response': data}

@get('/diskdata')
def disk():
    oids=['1.3.6.1.4.1.2021.9.1.8.1','1.3.6.1.4.1.2021.9.1.7.1']
#           used                        avaible
    data=oid(oids)
    return {'response': data}

# make api call
run(host='localhost', port=8080)
