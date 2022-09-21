from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


API_ENDPOINT = 'telephony'
OBJECT_TYPE = 'telephony'


class TelephonyAPI(object):
    def __init__(self, session, object_factory):
        """Initialize a new PeopleAPI object with the provided RestSession.
        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Webex Teams service.
        Raises:
            TypeError: If the parameter types are incorrect.
        """
        check_type(session, RestSession)

        super(TelephonyAPI, self).__init__()

        self._session = session
        self._object_factory = object_factory


    @generator_container
    def list_aa(self, name=None, locationId=None, orgId=None, start=None, phoneNumber=None, max=None, **request_parameters):
        """List AAs in your organization.
        Args:
            name(basestring): The name of the AA
            locationId(basestring): list all in this location
            orgId(basestring): The organization ID.
            start: Start at the zero-based offset in the list of matching objects.
            phoneNumber: Only return auto attendants with the matching phone number.
            max(int): Limit the maximum number of items returned from the Webex
                Teams service per request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the people returned by the Webex Teams query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.
        """
        check_type(name, basestring, optional=True)
        check_type(phoneNumber, basestring, optional=True)
        check_type(locationId, basestring, optional=True)
        check_type(orgId, basestring, optional=True)
        check_type(max, int, optional=True)
        check_type(start, int, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            name=name,
            locationId=locationId,
            start=start,
            orgId=orgId,
            phoneNumber=phoneNumber,
            max=max,
        )
        # API request - get items, define items key as autoAttendants, since Cisco decided to change that on us
        items = self._session.get_items(API_ENDPOINT  + "/config/autoAttendants", params=params, items_param="autoAttendants")

        # Yield person objects created from the returned items JSON objects
        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)


    def get_aa(self, locationId=None, autoAttendantId=None, orgId=None,  **request_parameters):
        """
        """
        check_type(locationId, basestring)
        check_type(autoAttendantId, basestring)
        check_type(orgId, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
        )

        # API request
        json_data = self._session.get(API_ENDPOINT + "/config/locations/" + locationId +
                                        "/autoAttendants/" + autoAttendantId,
                                        params=params)

        # Return a person object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)


    def create(self, emails, displayName=None, firstName=None, lastName=None,
               avatar=None, orgId=None, roles=None, licenses=None, locationId=None,
               callingData=False,
               **request_parameters):

        check_type(emails, list)
        check_type(displayName, basestring, optional=True)
        check_type(firstName, basestring, optional=True)
        check_type(lastName, basestring, optional=True)
        check_type(avatar, basestring, optional=True)
        check_type(orgId, basestring, optional=True)
        check_type(locationId, basestring, optional=True)
        check_type(roles, list, optional=True)
        check_type(licenses, list, optional=True)
        check_type(callingData, bool, optional=True)

        post_data = dict_from_items_with_values(
            request_parameters,
            emails=emails,
            displayName=displayName,
            firstName=firstName,
            lastName=lastName,
            avatar=avatar,
            orgId=orgId,
            locationId=locationId,
            roles=roles,
            licenses=licenses,
        )

        params = dict(callingData=callingData)

        # API request
        json_data = self._session.post(API_ENDPOINT, params=params, json=post_data)

        # Return a person object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)


    def delete(self, personId):
        check_type(personId, basestring)

        # API request
        self._session.delete(API_ENDPOINT + '/' + personId)


    @generator_container
    def list_hunt(self, name=None, locationId=None, orgId=None, start=None, phoneNumber=None, max=None, **request_parameters):
        """List AAs in your organization.
        Args:
            name(basestring): The name of the AA
            locationId(basestring): list all in this location
            orgId(basestring): The organization ID.
            start: Start at the zero-based offset in the list of matching objects.
            phoneNumber: Only return auto attendants with the matching phone number.
            max(int): Limit the maximum number of items returned from the Webex
                Teams service per request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the people returned by the Webex Teams query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.
        """
        check_type(name, basestring, optional=True)
        check_type(phoneNumber, basestring, optional=True)
        check_type(locationId, basestring, optional=True)
        check_type(orgId, basestring, optional=True)
        check_type(max, int, optional=True)
        check_type(start, int, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            name=name,
            locationId=locationId,
            start=start,
            orgId=orgId,
            phoneNumber=phoneNumber,
            max=max,
        )
        # API request - get items, define items key as autoAttendants, since Cisco decided to change that on us
        items = self._session.get_items(API_ENDPOINT  + "/config/huntGroups", params=params, items_param="huntGroups")

        # Yield person objects created from the returned items JSON objects
        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)


    def get_hunt(self, locationId=None, huntGroupId=None, orgId=None,  **request_parameters):
        """
        """
        check_type(locationId, basestring)
        check_type(huntGroupId, basestring)
        check_type(orgId, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
        )

        # API request
        json_data = self._session.get(API_ENDPOINT + "/config/locations/" + locationId +
                                        "/huntGroups/" + huntGroupId,
                                        params=params)

        # Return a person object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    #@generator_container
    def get_numbers(self, locationId=None, orgId=None,  **request_parameters):
        """
        """
        #check_type(locationId, basestring)
        #check_type(phoneNumber, basestring)
        #check_type(orgId, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
        )

        # API request
        items = self._session.get_items(API_ENDPOINT + "/config/numbers", params=params, items_param="phoneNumbers")
        #items = self._session.get(API_ENDPOINT + "/config/numbers",
        #                                params=params)


        # Yield person objects created from the returned items JSON objects
        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)