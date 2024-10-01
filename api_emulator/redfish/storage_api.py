# Redfish Storage and Storage Collection Resources API

from flask_restful import Resource
import sys, traceback
import logging
import g
from .templates.storage import format_storage_template

members = {}
INTERNAL_ERROR = 500

class Storage(Resource):
    """
    API for Storage Resource
    """

    def __init__(self, **kwargs):
        pass
    

    def get(self, system_ident, storage_ident):
        logging.info("Storage API made a GET request")
        try:
            resp = 404
            if system_ident not in members:
                return "requested storage not found", resp
            if storage_ident not in members[system_ident]:
                return "requested drive not found", resp
            resp = members[system_ident][storage_ident], 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp            


class StorageCollection(Resource):
    def __init__(self, rb, suffix):
        """
        Storage Collection Constructor
        """
        self.config = {u'@odata.context': '{rb}$metadata#StorageCollection.StorageCollection'.format(rb=rb),
                       u'@odata.id': '{rb}{suffix}'.format(rb=rb, suffix=suffix),
                       u'@odata.type': u'#StorageCollection.v1_1_0.StorageCollection'}
        
    
    def get(self, ident):
    """
    Creates the template for a Storage Collection and returns it
    """
        try:
            logging.info("Calling Storage Collection GET API")
            if ident not in members:
                return "storage not found", 404
            controllers = []
            for c in members.get(ident, {}).values():
                controllers.append({'@odata.id': c['@odata.id']})
            self.config['@odata.id'] = '{prefexi}/{ident}/Storage'.format(prefix=self.config['@odata.id'], ident=ident)
            self.config['Members'] = controllers
            self.config['Members@odata.count'] = len(controllers)
            resp = self.config, 200
        except Exception as e:
            logging.error(e)
            resp = 'Internal error', INTERNAL_ERROR
        return resp



def CreateStorage(**kwargs):
    suffix_id = kwargs['suffix_id']
    storage_id = kwargs['storage_id']
    if suffix_id not in members:
        members[suffix_id] = {}
    members[suffix_id][storage_id] = format_storage_template(**kwargs)
    g.api.add_resource(Drives, '/redfish/v1/Systems/<string:system_ident>/Storage/<string:storage_ident>/Drives/<string:drive_ident>')
                
