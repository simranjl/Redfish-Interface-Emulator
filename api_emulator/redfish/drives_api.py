# Drives API File

"""
Only GET is supported for now
"""

from flask_restful import Resource
import sys, traceback
import logging

from .templates.drives import format_drives_template

members = {}
INTERNAL_ERROR = 500


class DrivesAPI(Resource):
    def __init__(self, **kwargs):
        pass
    

    def get(self, system_ident, storage_ident, drive_ident):
        try:
            resp = 404
            if system_ident not in members:
                return "system not found", resp
            if storage_ident not in members[system_ident]:
                return "storage not found", resp
            if drive_ident not in members[system_ident][storage_ident]:
                return "drive not found", resp 
            resp = members[system_ident][storage_ident][drive_ident]
        except Exception as e:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp 
    


def CreateDrives(**kwargs):
    suffix_id = kwargs['suffix_id']
    storage_id = kwargs['storage_id']
    drive_id = kwargs['drive_id']
    if suffix_id not in members:
        members[suffix_id] = {}
    if storage_id not in members[suffix_id]:
        members[suffix_id][storage_id] = {}
    members[suffix_id][storage_id][drive_id] = format_drives_template(**kwargs)