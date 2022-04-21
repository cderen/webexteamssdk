from builtins import *

from past.builtins import basestring

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


OBJECT_TYPE = 'telephony'


class SkillsAPI(object):
    def __init__(self, session, object_factory):
        check_type(session, RestSession)
        super(SkillsAPI, self).__init__()
        self._session = session
        self._object_factory = object_factory

    @generator_container
    def list_skills(self, orgId=None, **request_parameters):
        check_type(orgId, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
        )
        items = self._session.get_items(f"/organization/{orgId}/v2/skill", params=params, items="data")

        # Yield person objects created from the returned items JSON objects
        for item in items:
            #yield self._object_factory(OBJECT_TYPE, item)
            yield item


    def create_skill(self, orgId=None, payload=None):
        # API request
        json_data = self._session.post(f"/organization/{orgId}/skill", json=payload, erc = 201)

        # Return a person object created from the returned JSON object
        return self._object_factory("OBJECT_TYPE", json_data)


    def delete_skill(self, orgId=None, id=None):
        # API request
        self._session.delete(f"/organization/{orgId}/skill/{id}")

