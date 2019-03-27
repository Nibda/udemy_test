from pytest import mark


@mark.body
class BodyTests:

    @mark.door
    def test_body_funtions_as_expected():
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
