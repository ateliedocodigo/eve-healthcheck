import pytest


class TestExample(object):

    def test_example(self):
        assert True, "This should not fail"

    @pytest.mark.xfail
    def test_failing(self):
        assert False, "This will always fail"
