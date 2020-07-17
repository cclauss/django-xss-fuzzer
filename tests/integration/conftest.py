import pytest


@pytest.fixture(scope='session')
def session_capabilities(session_capabilities):
    session_capabilities['loggingPrefs'] = {'browser': 'ALL'}
    session_capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}

    return session_capabilities
