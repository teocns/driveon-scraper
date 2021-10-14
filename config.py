BASE_URL = "https://www.driveon.es/buscador"

DB_NAME = "coches"
DB_TABLENAME = "available_coches"
DB_PASSWORD = ''
DB_USER = "postgres"
DB_HOST = ""


GET_REQUEST_HEADERS = {
    # 'Accept': '*/*',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'max-age=0',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
API_REQUEST_HEADERS = {
    # 'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Host': 'administracion.driveon.es',
    'Referer': "https://www.driveon.es/",
    'Origin': "https://www.driveon.es",
    # 'authorization': 'Bearer',
    # 'Connection': 'keep-alive',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',

}

JSON_ATTRIBUTES_TO_SAVE = [
    "listaMantenimiento",
    "listaEquipamiento",
    "listaImagenes",
]

ATTRIBUTES_TO_SAVE = [
    "idcombustible",
    "proximamente",
    "financiacion",
    "esconcesionario",
    "caballos",
    "distintivo",
    "chasis",
    "dsmodelo",
    "plazas",
    "precioNuevo",
    "estadoVehiculo",
    "pesoVacio",
    "dscategoria",
    "fechaMatriculacion",
    "idcarroceria",
    "precioAnt",
    "matricula",
    "deposit",
    "fechaPublicacion",
    "activo",
    "aceleracion",
    "idmarca",
    "kilometros",
    "libraryId",
    "pesoMaximo",
    "precioOrig",
    "idconcesionario",
    "dstraccion",
    "dsmarca",
    "largo",
    "fechaReserva",
    "dstransmision",
    "descuento",
    "consumoUrbano",
    "dscanalventa",
    "dsconcesionario",
    "dscombustible",
    "descripcion",
    "anioMatriculacion",
    "consumoMixto",
    "dscarroceria",
    "imgVeh",
    "garantia",
    "idtraccion",
    "cilindrada",
    "precioreserva",
    "transmision",
    "destacado",
    "emisiones",
    "idcategoria",
    "deposito",
    "consumoCarretera",
    "listaAviso",
    "precioacondicionar",
    "marchas",
    "precioDescuentoAntformat",
    "color",
    "oid",
    "alto",
    "capMaletero",
    "puertas",
    "precio",
    "dateCreated",
    "idmodelo",
    "ancho",
    "tapiceria",
    "idcanalventa",
    "caballosFiscales",
    "entidad",
    "isconcesionario"
]
