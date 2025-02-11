# -*- coding: utf-8 -*-
"""Webex Teams Devices API wrapper.
"""


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


API_ENDPOINT = 'devices'
OBJECT_TYPE = 'device'


class DevicesAPI(object):
    """Webex Teams People API.

    Wraps the Webex Teams Devices API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory):
        """Initialize a new PeopleAPI object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Webex Teams service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DevicesAPI, self).__init__()

        self._session = session
        self._object_factory = object_factory

    @generator_container
    def list(self, personId=None, placeId=None, orgId=None, displayName=None, product=None, capability=None,
             max=None, **request_parameters):
        """List devices in your organization.

        For most users, either the `email` or `displayName` parameter is
        required. Admin users can omit these fields and list all users in their
        organization.

        Args:
            email(basestring): The e-mail address of the person to be found.
            displayName(basestring): The complete or beginning portion of
                the displayName to be searched.
            id(basestring): List people by ID. Accepts up to 85 person IDs
                separated by commas.
            orgId(basestring): The organization ID.
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

        '''check_type(id, basestring, optional=True)
        check_type(email, basestring, optional=True)
        check_type(displayName, basestring, optional=True)
        check_type(orgId, basestring, optional=True)
        check_type(max, int, optional=True)'''

        params = dict_from_items_with_values(
            request_parameters,
            personId=personId,
            placeId=placeId,
            displayName=displayName,
            orgId=orgId,
            product=product,
            capability=capability,
            max=max,
        )


        # API request - get items
        items = self._session.get_items(API_ENDPOINT, params=params)

        # Yield person objects created from the returned items JSON objects
        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)

    '''def create(self, emails, displayName=None, firstName=None, lastName=None,
               avatar=None, orgId=None, roles=None, licenses=None, locationId=None,
               callingData=False,
               **request_parameters):
        """Create a new user account for a given organization

        Only an admin can create a new user account.

        Args:
            emails(`list`): Email address(es) of the person (list of strings).
            displayName(basestring): Full name of the person.
            firstName(basestring): First name of the person.
            lastName(basestring): Last name of the person.
            avatar(basestring): URL to the person's avatar in PNG format.
            orgId(basestring): ID of the organization to which this
                person belongs.
            roles(`list`): Roles of the person (list of strings containing
                the role IDs to be assigned to the person).
            licenses(`list`): Licenses allocated to the person (list of
                strings - containing the license IDs to be allocated to the
                person).
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Person: A Person object with the details of the created person.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
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

    def get(self, personId, callingData=False):
        """Get a person's details, by ID.

        Args:
            personId(basestring): The ID of the person to be retrieved.

        Returns:
            Person: A Person object with the details of the requested person.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(personId, basestring)

        # API request
        json_data = self._session.get(API_ENDPOINT + '/' + personId + '?callingData=' + str(callingData))

        # Return a person object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    def get_voicemail(self, personId):
        """Get a person's voicemail details, by ID.

        Args:
            personId(basestring): The ID of the person to be retrieved.

        Returns:
            Person: A Person object with the details of the requested person.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(personId, basestring)

        # API request
        #url = f"https://webexapis.com/v1/people/{person_id}/features/voicemail?orgId={org_id}"
        json_data = self._session.get(API_ENDPOINT + '/' + personId + '/features/voicemail')

        # Return a person object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    def get_forwarding(self, personId):
        """Get a person's voicemail details, by ID.

        Args:
            personId(basestring): The ID of the person to be retrieved.

        Returns:
            Person: A Person object with the details of the requested person.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(personId, basestring)

        # API request
        json_data = self._session.get(API_ENDPOINT + '/' + personId + '/features/callForwarding')

        # Return a person object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    def update(self, personId, emails=None, displayName=None, firstName=None,
               lastName=None, avatar=None, orgId=None, roles=None, callingData=False,
               licenses=None, locationId=None, **request_parameters):
        """Update details for a person, by ID.

        Only an admin can update a person's details.

        Email addresses for a person cannot be changed via the Webex Teams API.

        Include all details for the person. This action expects all user
        details to be present in the request. A common approach is to first GET
        the person's details, make changes, then PUT both the changed and
        unchanged values.

        Args:
            personId(basestring): The person ID.
            emails(`list`): Email address(es) of the person (list of strings).
            displayName(basestring): Full name of the person.
            firstName(basestring): First name of the person.
            lastName(basestring): Last name of the person.
            avatar(basestring): URL to the person's avatar in PNG format.
            orgId(basestring): ID of the organization to which this
                person belongs.
            roles(`list`): Roles of the person (list of strings containing
                the role IDs to be assigned to the person).
            licenses(`list`): Licenses allocated to the person (list of
                strings - containing the license IDs to be allocated to the
                person).
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Person: A Person object with the updated details.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(emails, list, optional=True)
        check_type(displayName, basestring, optional=True)
        check_type(firstName, basestring, optional=True)
        check_type(lastName, basestring, optional=True)
        check_type(avatar, basestring, optional=True)
        check_type(orgId, basestring, optional=True)
        check_type(locationId, basestring, optional=True)
        check_type(roles, list, optional=True)
        check_type(licenses, list, optional=True)
        check_type(callingData, bool, optional=True)

        put_data = dict_from_items_with_values(
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
        #print('XXX', locationId, callingData)
        params = dict(callingData=callingData)


        # API request
        json_data = self._session.put(API_ENDPOINT + '/' + personId,
                                      params=params, json=put_data)

        # Return a person object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)



    def delete(self, personId):
        """Remove a person from the system.

        Only an admin can remove a person.

        Args:
            personId(basestring): The ID of the person to be deleted.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(personId, basestring)

        # API request
        self._session.delete(API_ENDPOINT + '/' + personId)

    def me(self):
        """Get the details of the person accessing the API.

        Raises:
            ApiError: If the Webex Teams cloud returns an error.

        """
        # API request
        json_data = self._session.get(API_ENDPOINT + '/me')

        # Return a person object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)'''
