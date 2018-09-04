import datetime

from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session

session = Session()
client = Client

login = 'webclient'
password = '123'

url = 'http://80.254.115.133:8070/oookp_Donskoy/ws/inpk.1cws?wsdl'

start_period = datetime.datetime.now()
end_perion = datetime.datetime.now()
id_account = '101'


def get_connection_with_1c_server():
    session.auth = HTTPBasicAuth(login, password)

    return client(url, transport=Transport(session=session))


def fetch_client_balance_from_1c():
    connection = get_connection_with_1c_server()

    return connection.service.GetClientBalance(start_period, end_perion, id_account)

