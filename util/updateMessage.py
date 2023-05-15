from util import statics
import requests
import logging
logger = logging.getLogger(__name__)

def update(id):
    updateurl = statics.baseUrl + """
        ?method=set_entry&input_type=JSON&response_type=JSON&rest_data=
        {
            "session":\"""" + statics.session + """\",
            "module_name":\"""" + statics.moduleName + """\",
            "name_value_list":{"id":\"""" + id + """\","is_sent": 1},
            "track_view":1
        }
    
    
    """
    
    payload = {}
    headers = {}
    
    try:
        response = requests.request("GET", updateurl, headers=headers, data=payload)
        
    except requests.HTTPError as http_err:
        logging.error(f'errore HTTP nell\'aggiornamento: {http_err}')
        print(f'errore HTTP nell\'aggiornamento: {http_err}')
        return -1
    
    except Exception as err:
        logging.error(f'errore generico nell\'aggiornamento: {err}')
        print(f'errore generico nell\'aggiornamento: {err}')
        return -1
    
    jsonResponse = response.json()
    print(jsonResponse)
    