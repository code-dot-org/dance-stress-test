import pytest


def pytest_addoption(parser):
    parser.addoption('--framework', action='store', default='selenium', \
      help='automation framework: selenium (default) or appium')
    parser.addoption('--ml-hoc-url', action='store', default='https://test-studio.code.org/', \
      help='base url for ML HoC activity')


@pytest.fixture(scope='class')
def framework(request):
    request.cls.framework = request.config.getoption('--framework')
    return request.config.getoption('--framework')


@pytest.fixture(scope='class')
def ml_hoc_url(request):
    url = request.config.getoption('--ml-hoc-url')
    if not url.endswith('/'):
        url += '/'

    request.cls.ml_hoc_url = url
    return url
