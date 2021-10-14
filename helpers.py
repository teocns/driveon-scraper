import base64
import json


def make_apireq_data(d: dict) -> dict:
    a = {
        "data": base64.b64encode(
            json.dumps(
                {"entidad": "1", "from": "drvon", "compare": "search", "conc": "", "textSearch": "", "typeofCar": [{"value": "berlina", "text": "Berlina"}, {"value": "compacto", "text": "Compacto"}], "anioMat": "", "combustible": "", "cambio": "", "modelo": "", "brandsSelect": [
                ], "precioDesde": 0, "precioHasta": 80000, "kilometrosDesde": 0, "kilometrosHasta": 10000000, "dsmarca": "", "dsmodelo": "", "accion": "search", "executeApi": "BuscadorAPI"}
            ).encode("utf-8")
        ),
    }

    return a


def get_sql(sql_filename):
    with open("sql/%s.sql" % sql_filename, "r") as f:
        return f.read()
