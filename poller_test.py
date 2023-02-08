import pytest
from poller import Participant

@pytest.mark.parametrize(
    ["participants", "expected"],
    [
    (Participant("Isabelle",5,3,1,1), "Isabelle,5,3,1,1" ),
    (Participant("Manny G",6,4,1,1), "Manny G,6,4,1,1"),
    (Participant("Louis T",5,4,1,0), "Louis T,5,4,1,0"),
    (Participant("Glory Hernandez",7,3,3,1), "Glory Hernandez,5,3,1,1"),
    (Participant("Paulo J",3,2,0,1), "Paulo J,3,2,0,1"),
    (Participant("Julio Volteo",1,0,0,0), "Julio Volteo,1,0,0,0")
    ]
)
def test_participant(participants, expected):
    assert str(participants) == expected


@pytest.mark.parametrize(
    ["polled ","expected"]

)
def test_poller(poller, expected):
    assert 
