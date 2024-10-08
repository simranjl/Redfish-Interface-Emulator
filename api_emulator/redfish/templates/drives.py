# Drives Template File

from copy import deepcopy
import strgen

DRIVES_TEMPLATE = {
    "@odata.id": "{rb}{suffix}/Storage/{storage_id}/Drives/{drive_id}",
    "@odata.type": "#Drives.v1_1_0.Drives",
    "@odata.context": "{rb}$metadata#Drives.Drives",
    "Id": "{drive_id}",
    "Name": "{drive_name}",
    "Model": None,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "SerialNumber": None,
    "CapacityBytes": None
}


def format_drives_template(**kwargs):
    defaults = {
        'rb': '/redfish/v1/',
        'suffix': 'Systems',
        'drive_model': strgen.StringGenerator('[A-Z]{1}[0-3]{3}').render(),
        'serial_number': strgen.StringGenerator('[0-9]{10}').render(),
        'capacity_bytes': 384950234
    }
    defaults.update(kwargs)

    c = deepcopy(DRIVES_TEMPLATE)
    c['@odata.id'] = c['@odata.id'].format(**defaults)
    c['@odata.context'] = c['@odata.context'].format(**defaults)
    c['Id'] = c['Id'].format(**defaults)
    c['Name'] = c['Name'].format(**defaults)
    c['Model'] = defaults['Model']
    c['SerialNumber'] = defaults['serial_number']
    # c['CapacityBytes'] = c['CapacityBytes'].format(**defaults)
    c['CapacityBytes'] = defaults['capacity_bytes']

    return c