# GENERAL ERRORS
NOT_FOUND = "Not Found: {}"
INTERNAL_ERROR = "Internal server error"
INVALID_PARAMS = "Invalid parameters provided: {}"
AUTHENTICATION_ERROR = "Cannot authenticate. Api token missing or invalid"
INVALID_JAF_DATA_TYPE = "Data can be list or object only"

# LIBRARY ERRORS
LIBRARY_INVALID_NAME = "Library name must be an alpha numeric string with [-_.]"
LIBRARY_ALREADY_EXISTS = "A library with this name already exists"

# LIBRARY VERSION ERRORS
LIBRARY_VERSION_NO_TRYOUT = "The specified library does not have an endpoint"
LIBRARY_VERSION_BAD_FORMAT = "Uploaded file must be tar.gz"
LIBRARY_VERSION_TAR_ALREADY_EXIST = "Cannot upload a tar file twice to the same version"
LIBRARY_VERSION_INFERENCE_DOESNT_EXIST = "This blueprint doesn't use an inference library"

# BLUEPRINT ERRORS
BLUEPRINT_INVALID_NAME = "Blueprint name must be an alpha numeric string with [-_.]"
BLUEPRINT_ALREADY_EXISTS = "A blueprint with this name already exists"
BLUEPRINT_NOT_INFERENCE = "Blueprint is not an inference"
BLUEPRINT_BUILD_DOESNT_EXISTS = "The blueprint does not have an active build"
BLUEPRINT_BUILD_ALREADY_EXISTS = "The blueprint already has an active build (use force to override)"

# TAG ERRORS:
NAMES_NOT_PROVIDED = "Please provide tag names using the 'name' or the 'names' attribute"

# COMMON
VERSION_NOT_FOUND = "The requested version was not found"
VERSION_TOO_LOW = "Higher version already exists"
RESOURCE_NOT_FOUND = "The requested {resource} was not found"

# HTTP ERRORS
PARSING_ERROR = "Could not parse response"
PROXY_HTTP_ERROR = "A server error has occurred."
PROXY_UNAUTH_ERROR = "Unauthorized to perform this action."
PROXY_EMPTY_RESPONSE = "Cannot convert empty response to json"
PROXY_NOT_FOUND_ERROR = "The requested resource could not be found."

# FILE ERRORS
NOT_PARSABLE_YAML = "The yaml provided is couldn't be parsed"
INVALID_SCHEMA_TYPE = "Invalid schema type provided"
INVALID_SCHEMA_ARGUMENT = "Invalid schema: {}"

# PAGINATION
INVALID_FILTER = "Invalid filter provided"
CONDITION_NOT_FOUND = "Invalid filter. Conditions not found in filter"
INVALID_CONDITION = "Invalid filter. Condition must have key, operator and value attributes"
