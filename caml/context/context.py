import os
import requests

from caml.errors import CamlArgumentsError
from caml.errors.error_messages import CamlArgumentsError


class SCOPE:
    """
    The scope is used to keep the correct URL or the API resource
    """

    # Resources are the cloud resources connected to caml
    RESOURCE = {
        "key": "resource",
        "dependencies": ["user"]
    }

    @classmethod
    def scopes(cls):
        """
        Calculates all of the scopes from the class attributes
        @return: [List] list of scopes
        """
        scopes = []
        for attr in dir(cls):
            if not callable(getattr(cls, attr)) and not attr.startswith("__"):
                scopes.append(getattr(cls, attr)["key"])
        return scopes


class Context:
    def __init__(self, context=None, caml_url=None, user=None, password=None):
        # Set the credentials variables:
        self.user = None
        self.token = None
        self.caml_url = None

        # Reset the scope:
        for scope in SCOPE.scopes():
            setattr(self, scope, None)

        # If a context is passed, perform a deep copy and return
        if context:
            self._copy_context(context=context)
            return

        # Cannot pass username/password without a domain+username+password or domain + user + token
        if (user or password or domain) and not all([domain, user, password]):
            raise CamlArgumentsError(error_messages.CONTEXT_BAD_ARGUMENTS)

        # If a domain is passed, init a blank Cnvrg client
        if domain:
            self.domain = domain
            self._authenticate(domain, user, password, token, is_capi)
        else:
            self._load_credentials()

    def get_scope(self, scope):
        """
        Checks if the current context contains the relevant scope
        @param scope: a SCOPE object constant
        @raise CnvrgError: if the context does not contain the required scope dependencies
        @return: scope dictionary
        """

        dependencies_dict = self._check_dependencies(scope)
        cur_scope = getattr(self, scope["key"], None)
        if cur_scope is None:
            error_msg = error_messages.CONTEXT_SCOPE_BAD_SCOPE.format(scope["key"])
            raise CnvrgError(error_msg)

        return {scope["key"]: cur_scope, **dependencies_dict}

    def set_scope(self, scope, slug):
        """
        Checks if the current context contains the relevant scope and sets new scope
        @param scope: a SCOPE object constant
        @param slug: scope object slug
        @raise CnvrgError: if the context does not contain the required scope dependencies
        @return: slug/None
        """
        if scope == SCOPE.ORGANIZATION:
            self.ensure_organization_exist(slug)

        self._check_dependencies(scope)
        setattr(self, scope["key"], slug)

    def save(self):
        """
        Creates a .cnvrg/config file to reuse authentication.
        Config save will only work in organization context, otherwise an error will be raised
        @raise CnvrgError: Tried to save without having at least organization context
        @return: Boolean depending if context save was successful
        """
        config = Config()
        # Will throw a CnvrgError if organization context is not present
        config_data = self._generate_context_dict()
        config.update(**config_data)

    def _copy_context(self, context):
        """
        Performs a deep copy of the supplied context into the current one
        @param context: [context] The source context
        @return: None
        """
        self.token = context.token
        self.domain = context.domain
        self.user = context.user

        for scope in SCOPE.scopes():
            target_attr = getattr(context, scope, None)
            setattr(self, scope, target_attr)

    def _check_dependencies(self, scope):
        """
        This function checks that the requested scope has all of its dependencies initialized
        @param scope: The scope const we want to check
        @return: dict of scopes and their slugs
        """
        # Build scope object
        scope_dict = {}
        for dependency in scope["dependencies"]:
            dependency_slug = getattr(self, dependency, None)
            if dependency_slug is None:
                error_msg = error_messages.CONTEXT_SCOPE_BAD_DEPENDENCIES.format(scope["key"], dependency)
                raise CnvrgError(error_msg)
            else:
                scope_dict[dependency] = dependency_slug

        return scope_dict

    def _load_credentials(self):
        """
        Attempts to login using either environment variables or the global Cnvrg config file
        @raise: CnvrgError if cannot login using either method
        @return: None
        """
        logged_in = self._load_from_env() or self._load_from_config()
        if not logged_in:
            raise CnvrgError(error_messages.CONTEXT_BAD_ENV_VARIABLES)

    def _load_from_config(self):
        """
        Attempts to find credentials in local/global config file
        @return: Boolean
        """
        config = Config()
        if not config:
            return False

        token, domain, user = config.get_credential_variables()

        # Context variables
        organization = config.organization

        if not all([token, domain, user, organization]):
            return False

        self.token = token
        self.is_capi = config.is_capi
        self.domain = domain
        self.user = user

        return True
