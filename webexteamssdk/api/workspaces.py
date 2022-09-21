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


API_ENDPOINT = 'workspaces'
OBJECT_TYPE = 'workspace'


class WorkspacesAPI(object):
    """Webex Teams workspaces API.

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

        super(WorkspacesAPI, self).__init__()

        self._session = session
        self._object_factory = object_factory

    @generator_container
    def list(self, orgId=None, workspaceLocationId=None, floorId=None, displayName=None, capacity=None,
             type=None, start=None, calling=None, calendar=None, max=None, **request_parameters):
        """List devices in your organization.

        For most users, either the `email` or `displayName` parameter is
        required. Admin users can omit these fields and list all users in their
        organization.

        Args:
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
            orgId=orgId,
            workspaceLocationId=workspaceLocationId,
            floorId=floorId,
            displayName=displayName,
            capacity=capacity,
            type=type,
            start=start,
            calling=calling,
            calendar=calendar,
            max=max,
        )


        # API request - get items
        items = self._session.get_items(API_ENDPOINT, params=params)

        # Yield person objects created from the returned items JSON objects
        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)

    def create(self, orgId=None, workspaceLocationId=None, floorId=None, displayName=None, capacity=None,
             type=None, start=None, calling=None, calendar=None, max=None, **request_parameters):
        """Create a new user account for a given organization

        Only an admin can create a new user account.

        Args:
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Person: A Person object with the details of the created person.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        '''check_type(emails, list)
        check_type(displayName, basestring, optional=True)
        check_type(firstName, basestring, optional=True)
        check_type(lastName, basestring, optional=True)
        check_type(avatar, basestring, optional=True)
        check_type(orgId, basestring, optional=True)
        check_type(locationId, basestring, optional=True)
        check_type(roles, list, optional=True)
        check_type(licenses, list, optional=True)'''

        post_data = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
            workspaceLocationId=workspaceLocationId,
            floorId=floorId,
            displayName=displayName,
            capacity=capacity,
            type=type,
            start=start,
            calling=calling,
            calendar=calendar,
            max=max
        )


        # API request
        json_data = self._session.post(API_ENDPOINT, json=post_data, erc=201)

        # Return a person object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)

    def get(self, workspace_id):
        """Get a person's details, by ID.

        Args:
            personId(basestring): The ID of the person to be retrieved.

        Returns:
            Person: A Person object with the details of the requested person.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(workspace_id, basestring)

        # API request
        json_data = self._session.get(API_ENDPOINT + '/' + workspace_id)

        # Return a person object created from the response JSON data
        #return self._object_factory(OBJECT_TYPE, json_data)
        return json_data


    def update(self, workspaceId=None, orgId=None, workspaceLocationId=None, floorId=None, displayName=None, capacity=None,
             type=None, start=None, calling=None, calendar=None, max=None, **request_parameters):
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
        # check_type(emails, list, optional=True)
        # check_type(displayName, basestring, optional=True)
        # check_type(firstName, basestring, optional=True)
        # check_type(lastName, basestring, optional=True)
        # check_type(avatar, basestring, optional=True)
        # check_type(orgId, basestring, optional=True)
        # check_type(locationId, basestring, optional=True)
        # check_type(roles, list, optional=True)
        # check_type(licenses, list, optional=True)
        # check_type(callingData, bool, optional=True)

        put_data = dict_from_items_with_values(
            request_parameters,
            orgId=orgId,
            workspaceLocationId=workspaceLocationId,
            floorId=floorId,
            displayName=displayName,
            capacity=capacity,
            type=type,
            start=start,
            calling=calling,
            calendar=calendar,
            max=max
        )

        # API request
        json_data = self._session.put(API_ENDPOINT + '/' + workspaceId, json=put_data)

        # Return a person object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)



    def delete(self, workspaceId):
        """Remove a person from the system.

        Only an admin can remove a person.

        Args:
            personId(basestring): The ID of the person to be deleted.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(workspaceId, basestring)

        # API request
        self._session.delete(API_ENDPOINT + '/' + workspaceId)
