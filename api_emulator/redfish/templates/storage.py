from copy import deepcopy

STORAGE_TEMPLATE = {
    "@odata.context": "{rb}$metadata#Storage.Storage",
    "@odata.type": "#Storage.v1_1_0.Storage",
    "@odata.id": "{rb}{suffix}/{suffix_id}/Storage/{storage_id}",
    "Id": "{storage_id}",
    "Name": "Local Storage Controller",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }, 
    "Drives": None
}


def format_storage_template(**kwargs):
    defaults = {
        'rb': '/redfish/v1/',
        'suffix': 'Systems',
        'drives': []
    }
    defaults.update(kwargs)

    c = deepcopy(STORAGE_TEMPLATE)
    c['@odata.context'] = c['@odata.context'].format(**defaults)
    c['@odata.type'] = c['@data.type'].format(**defaults)
    c['@odata.id'] = c['@odata.id'].format(**defaults)
    c['Id'] = c['Id'].format(**defaults)
    c['Drives'] = c['Drives'].format(**defaults)

    return c