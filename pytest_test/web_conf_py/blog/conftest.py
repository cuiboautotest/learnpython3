import pytest
@pytest.fixture(scope="session")
def open_blog():
    print("打开blog页面_function")
