import pytest


@pytest.mark.usefixtures("setup_common")
class TestClass:
    def test_ui(self, setup_ui):
        assert 3 == 3

    def test_ui_1(self, setup_ui):
        assert 3 == 3