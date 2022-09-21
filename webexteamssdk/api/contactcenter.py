from builtins import *

from past.builtins import basestring

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


OBJECT_TYPE = ''


class ContactCenterAPI(object):
    def __init__(self, session, object_factory):
        check_type(session, RestSession)
        super(ContactCenterAPI, self).__init__()
        self._session = session
        self._object_factory = object_factory


    @generator_container
    def list_feature(self, orgId=None, feature=None, type=None, **request_parameters):
        check_type(orgId, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
            type=type
        )
        items = self._session.get_items(f"/organization/{orgId}/{feature}", params=params, items_param="data")

        # Yield person objects created from the returned items JSON objects
        for item in items:
            # yield self._object_factory(OBJECT_TYPE, item)
            yield item

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


    @generator_container
    def list_queues(self, orgId=None, feature=None, type=None, **request_parameters):
        check_type(orgId, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
            type=type
        )
        items = self._session.get_items(f"/organization/{orgId}/{feature}", params=params, items_param="resources")

        # Yield person objects created from the returned items JSON objects
        for item in items:
            # yield self._object_factory(OBJECT_TYPE, item)
            yield item

    def get_feature(self, orgId=None, feature=None, id=None):
        return self._session.get(f"/organization/{orgId}/{feature}/{id}")


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

