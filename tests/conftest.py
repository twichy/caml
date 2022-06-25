import os
import sys
import string
import pytest
import random

# Add the parent folder to python path to run tests and coverage from shell
sys.path.append(os.path.join(os.getcwd(), os.pardir))


def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@pytest.fixture(scope="function")
def random_name():
    return random_string


def get_domain():
    # Add env var CLUSTER_DOMAIN
    return os.environ.get("CLUSTER_DOMAIN") or "http://localhost:3000"


@pytest.fixture(scope="package")
def domain():
    return get_domain()
