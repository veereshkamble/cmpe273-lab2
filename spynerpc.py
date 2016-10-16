import logging
logging.basicConfig(level=logging.DEBUG)
from spyne import Application, srpc, ServiceBase, Integer, Unicode, decorator,Float
from spyne.decorator import srpc
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication
import api

class CrimeReportAPIService(ServiceBase):
    @srpc(Float, Float, Float,_returns=Unicode)
    def checkcrime(lat, lon, radius):
      return api.call(lat, lon, radius)


application = Application([CrimeReportAPIService],
    tns='veereshkamble.spyne.crime.api',
    in_protocol=HttpRpc(validator='soft'),
    out_protocol=JsonDocument()
)
if __name__ == '__main__':

    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
