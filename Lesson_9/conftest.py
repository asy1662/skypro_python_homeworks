import pytest
url =    'https://x-clients-be.onrender.com' 

def pytest_addoption(parser):
    """Метод PyTest для добавления пользовательских параметров."""
    parser.addoption(
        "--stage", 
        action="store", 
        default='test', 
        type=str,
        required=False,
        help="Установить этап: '--stage=test' -> /configs/appsettings.test.json"
    )

@pytest.fixture(scope="session")
def stage(request):
    """Обработчик параметра --stage."""
    return request.config.getoption("--stage")