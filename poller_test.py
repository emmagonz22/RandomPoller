import pytest
from poller import Participant
from mock_open import mock_open

def test_participant():
    participant = Participant("Isabelle",5,3,1,1)
    assert str(participant) == "Isabelle,5,3,1,1"
@pytest.mark.parametrize(
    ["value","expected"],
    [
    ]
)
def poller_test(value, expected ):

    pass


    