import pytest
from poller import Participant, Poller
from mock_open import mock_open



@pytest.mark.parametrize(
    ["participants", "expected"],
    [
    (Participant("Isabelle",5,3,1,1), "Isabelle,5,3,1,1" ),
    (Participant("Manny G",6,4,1,1), "Manny G,6,4,1,1"),
    (Participant("Louis T",5,4,1,0), "Louis T,5,4,1,0"),
    (Participant("Glory Hernandez",5,3,1,1), "Glory Hernandez,5,3,1,1"),
    (Participant("Paulo J",3,2,0,1), "Paulo J,3,2,0,1"),
    (Participant("Julio Volteo",1,0,0,0), "Julio Volteo,1,0,0,0")
    ]
)
def test_participant(participants, expected):
    assert str(participants) == expected

## Verify the participants list is correct
def test_enter_poller():
    with Poller("./data/participants.csv", mock_open(["Juan Perez,1,0,1,0", "Maria Rosa,5,3,0,2", "Danny Mek,2,0,2,0"])) as poller:
        participants_list = [str(participant) for participant in  poller.participants]
        assert participants_list ==  [str(Participant("Juan Perez",1,0,1,0)),str(Participant("Maria Rosa",5,3,0,2)),str(Participant("Danny Mek",2,0,2,0))]

#def test_exit_poller():

def test_poller_iter_next():

    with Poller("./data/participants.csv", mock_open(["Juan Perez,1,0,1,0", "Maria Rosa,5,3,0,2", "Danny Mek,2,0,2,0"])) as poller:
        minimum_polled = poller.participants[0].poll_counter
        for participant in poller.participants:
            if participant.poll_counter < minimum_polled:
                minimum_polled = participant.poll_counter 
        assert next(poller).poll_counter == minimum_polled

def test_poller_correct():
    with Poller("./data/participants.csv", mock_open(["Juan Perez,1,0,1,0", "Maria Rosa,5,3,0,2", "Danny Mek,2,0,2,0"])) as poller:
        next(poller)
        poller.correct()
        participants_list = [str(participant) for participant in  poller.participants]  
        assert participants_list == [str(Participant("Juan Perez",2,1,1,0)),str(Participant("Maria Rosa",5,3,0,2)),str(Participant("Danny Mek",2,0,2,0))]
def test_poller_attempt():
    with Poller("./data/participants.csv", mock_open(["Juan Perez,1,0,1,0", "Maria Rosa,5,3,0,2", "Danny Mek,2,0,2,0"])) as poller:
        next(poller)
        poller.attempted()
        participants_list = [str(participant) for participant in  poller.participants]  
        assert participants_list == [str(Participant("Juan Perez",2,0,2,0)),str(Participant("Maria Rosa",5,3,0,2)),str(Participant("Danny Mek",2,0,2,0))]

def test_poller_missing():
    with Poller("./data/participants.csv", mock_open(["Juan Perez,1,0,1,0", "Maria Rosa,5,3,0,2", "Danny Mek,2,0,2,0"])) as poller:
        next(poller)
        poller.missing()
        participants_list = [str(participant) for participant in  poller.participants]  
        assert participants_list == [str(Participant("Juan Perez",2,0,1,0)),str(Participant("Maria Rosa",5,3,0,2)),str(Participant("Danny Mek",2,0,2,0))]

def test_poller_excused():
    with Poller("./data/participants.csv", mock_open(["Juan Perez,1,0,1,0", "Maria Rosa,5,3,0,2", "Danny Mek,2,0,2,0"])) as poller:
        next(poller)
        poller.excused()
        participants_list = [str(participant) for participant in  poller.participants]  
        assert participants_list == [str(Participant("Juan Perez",2,0,1,1)),str(Participant("Maria Rosa",5,3,0,2)),str(Participant("Danny Mek",2,0,2,0))]

def test_poller_stop():
    with Poller("./data/participants.csv", mock_open(["Juan Perez,1,0,1,0", "Maria Rosa,5,3,0,2", "Danny Mek,2,0,2,0"])) as poller:
        poller.stop()
        assert poller.continue_iter == False

def test_poller_total():
    with Poller("./data/participants.csv", mock_open(["Juan Perez,1,0,1,0", "Maria Rosa,5,3,0,2", "Danny Mek,2,0,2,0"])) as poller:
        next(poller)
        poller.correct()
        next(poller)
        poller.missing()
        assert poller.total() == 2