from builtins import *

from past.builtins import basestring

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


OBJECT_TYPE = ''


class csdmAPI(object):
    def __init__(self, session, object_factory):
        check_type(session, RestSession)
        super(csdmAPI, self).__init__()
        self._session = session
        self._object_factory = object_factory


    def get(self, orgId=None, feature=None, device_id=None):
        # API request
        json_data = self._session.get(f"/csdm/api/v1/organization/{orgId}/{feature}/{device_id}")

        return self._object_factory(OBJECT_TYPE, json_data)

    #@generator_container
    def list(self, orgId=None, feature=None):
        check_type(orgId, basestring, optional=True)
        payload = {"query": None,
                    "aggregates": ["connectionStatus",
                                   "category",
                                   "callingType"
                                   ],
                    "size": 100,
                    "from": 0,
                    "sortField": "category",
                    "sortOrder": "asc",
                    "initial": True,
                    "translatedQueryString": ""
                    }

        #items = self._session.get_items(f"/csdm/api/v1/organization/{orgId}/{feature}", items="hits")#, params=None, items=None)
        items = self._session.post_test(f"/csdm/api/v1/organization/{orgId}/{feature}", json=payload)
                                        #items="hits")  # , params=None, items=None)

        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)
            #yield item

    @generator_container
    def list_feature_list(self, orgId=None, feature=None, type=None, **request_parameters):
        check_type(orgId, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
            type=type
        )
        items = self._session.get_items_list(f"/organization/{orgId}/{feature}", params=params)

        # Yield person objects created from the returned items JSON objects
        for item in items:
            # yield self._object_factory(OBJECT_TYPE, item)
            yield item




    def create_feature(self, orgId=None, feature=None, payload=None):
        json_data = self._session.post(f"/organization/{orgId}/{feature}", json=payload, erc = 201)

        # Return a person object created from the returned JSON object
        #return self._object_factory("OBJECT_TYPE", json_data)
        return json_data  #todo changed as tests were failing


    def update_feature(self, orgId=None, feature=None, payload=None, id=None):
        json_data = self._session.put(f"/organization/{orgId}/{feature}/{id}", json=payload, erc = 200)

        # Return a person object created from the returned JSON object
        # return self._object_factory("OBJECT_TYPE", json_data)

        return json_data  # todo changed as tests were failing


    def delete_feature(self, orgId=None, feature=None, id=None):
        return self._session.delete(f"/organization/{orgId}/{feature}/{id}")

