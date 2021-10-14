import json
import base64
from config import API_REQUEST_HEADERS, GET_REQUEST_HEADERS
import requests
from config import BASE_URL
from helpers import make_apireq_data
from cloudscraper import CloudScraper


URL_TARGET = 'https://www.driveon.es/buscador'
API_GET_COCHE = "https://administracion.driveon.es/driveonadmin/callDROApi"


def retrieve_all_available_vehicles():
    sess = CloudScraper(browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    })

    list_json = sess.post(
        API_GET_COCHE,
        headers={**API_REQUEST_HEADERS,
                 # "access-control-request-headers": "authorization",
                 "Authorization": "Bearer ",
                 "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                 # "access-control-request-method": "POST"
                 },
        data={
            "data": "eyJlbnRpZGFkIjoiMSIsImZyb20iOiJkcnZvbiIsImNvbXBhcmUiOiJzZWFyY2giLCJjb25jIjoiIiwidGV4dFNlYXJjaCI6IiIsInR5cGVvZkNhciI6W10sImFuaW9NYXQiOiIiLCJjb21idXN0aWJsZSI6IiIsImNhbWJpbyI6IiIsIm1vZGVsbyI6IiIsImJyYW5kc1NlbGVjdCI6W10sInByZWNpb0Rlc2RlIjowLCJwcmVjaW9IYXN0YSI6ODAwMDAsImtpbG9tZXRyb3NEZXNkZSI6MCwia2lsb21ldHJvc0hhc3RhIjoxMDAwMDAwMCwiZHNtYXJjYSI6IiIsImRzbW9kZWxvIjoiIiwiYWNjaW9uIjoibG9hZERhdGEiLCJleGVjdXRlQXBpIjoiQnVzY2Fkb3JBUEkifQ=="
        },
        # data=req_data,
        allow_redirects=False
    )

    js = json.loads(
        list_json.text).get('data', '{}')
    extracted_data = base64.b64decode(js)

    converted = json.loads(extracted_data.decode('latin-1'))

    return converted.get('listDatos', [])


def car_exists(oid): 
    pass

def retrieve_single_vehicle_data(vehicle_oid):
    sess = CloudScraper(browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    })
    # {"entidad":"1","oidVehiculo":"7836","precioVehiculo":0,"dineroEntrada":0,"numCuotas":0,"landing":"","nombre":"","apellidos":"","telefono":"","email":"","hora":"","dia":"","aceptaComunicaciones":"No","nombreFinan":"","apellidosFinan":"","movilFinan":"","emailFinan":"","aceptaComunicacionesFinan":"No","nombreVideo":"","apellidosVideo":"","movilVideo":"","emailVideo":"","observacionesVideo":"","aceptaComunicacionesVideo":"No","urlOrgin":"www.driveon.es/coches-ocasion/bmw/serie-7/730d-xdrive-195-kw-265-cv-15323km-9368LFX-7836","detailveh":"true","from":"drvon","compare":"search","accion":"cargaVehiculo","executeApi":"BuscadorAPI"}
    req_data = make_apireq_data(None)
    r1 = sess.get(URL_TARGET, headers=GET_REQUEST_HEADERS)
    list_json = sess.post(
        API_GET_COCHE,
        headers={**API_REQUEST_HEADERS,
                 # "access-control-request-headers": "authorization",
                 "Authorization": "Bearer ",
                 "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                 # "access-control-request-method": "POST"
                 },
        data={
            "data": base64.b64encode(json.dumps({"entidad": "1", "oidVehiculo": vehicle_oid, "precioVehiculo": 0, "dineroEntrada": 0, "numCuotas": 0, "landing": "", "nombre": "", "apellidos": "", "telefono": "", "email": "", "hora": "", "dia": "", "aceptaComunicaciones": "No", "nombreFinan": "", "apellidosFinan": "", "movilFinan": "", "emailFinan": "",
                                                 "aceptaComunicacionesFinan": "No", "nombreVideo": "", "apellidosVideo": "", "movilVideo": "", "emailVideo": "", "observacionesVideo": "", "aceptaComunicacionesVideo": "No", "urlOrgin": "", "detailveh": "true", "from": "drvon", "compare": "search", "accion": "cargaVehiculo", "executeApi": "BuscadorAPI"}).encode('utf-8')).decode('utf-8')
        },
        # data=req_data,
        allow_redirects=False
    )

    js = json.loads(
        list_json.text).get('data', '{}')
    extracted_data = base64.b64decode(js)

    converted = json.loads(extracted_data.decode('latin-1'))
    
    return converted
