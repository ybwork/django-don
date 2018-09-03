import datetime

from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session

def work_soap():
    session = Session()
    session.auth = HTTPBasicAuth('webclient', '123')

    client = Client(
        'http://80.254.115.133:8070/oookp_Donskoy/ws/inpk.1cws?wsdl',
        transport=Transport(session=session)
    )
    params = {
        'StartPeriod': '1535760000',
        'EndPeriod': '1538351999',
        'IdAccount': '101'
    }
    return client.service.GetClientBalance(datetime.datetime.now(), datetime.datetime.now(), '101')

