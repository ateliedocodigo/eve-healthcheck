import pytest
from nose.tools import raises


class TestExample(object):

    def test_example(self):
        assert True, "This should not fail"

    @pytest.mark.xfail
    @raises(AssertionError)
    def test_failing(self):
        assert False, "This will always fail"
