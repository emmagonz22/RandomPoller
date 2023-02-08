import os 
import csv
import random
import sys

class Participant:
    ##<name>,<#polled>,<#correct>,<#attempted>,<#excused>
    def __init__(self, name: str, polled_counter: int,correct_counter: int, attempted_counter: int , excused_counter: int):
        self.name : int = name
        self.polled_counter : int = polled_counter
        self.attempted_counter : int = attempted_counter
        self.correct_counter : int = correct_counter
        self.excused_counter : int = excused_counter
      
    def __str__(self):
        return f"{self.name},{self.polled_counter},{self.correct_counter},{self.attempted_counter},{self.excused_counter}"

    def increase_attempted_counter(self):
        self.attempted_counter += 1
        self.polled_counter += 1

    def increase_correct_counter(self):
        self.correct_counter += 1
        self.polled_counter += 1

    def increase_excused_counter(self):
        self.excused_counter += 1
        self.polled_counter += 1

    def increase_polled_counter(self):
        self.polled_counter += 1


class Poller:
    def __init__(self, filename: str, open_file = open):
        self.filename : str = filename
        self.participants = []
        self.execution_attempts = 0
        self.selected_participant = None
        self.open_file = open_file
    def __enter__(self):
        if os.stat(self.filename).st_size == 0:
            raise ValueError("File is empty")
        else:
            with self.open_file(self.filename, "r") as filecsv:
                participant_csvfile = csv.reader(filecsv, delimiter=" ")
          
                for participant in participant_csvfile:
                
                    explode_line = participant[1].split(',')                
                    self.participants.append(  Participant(f"{participant[0]} {explode_line[0]}",int(explode_line[1]),int(explode_line[2]), int(explode_line[3]), int(explode_line[4]) ))
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        formated_list = []
        
        for participant in self.participants:
            participant_lst = [participant.name, participant.polled_counter, participant.correct_counter, participant.attempted_counter, participant.excused_counter]
            formated_list.append(participant_lst)
        ##
        with self.open_file(self.filename, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(formated_list)

        #self.participant_csvfile.close()
    def __iter__(self):
        self.random_index = -1
        return self
    def __next__(self): #Fix to select random participant
        print(self.participants)
        polled_num_set = set()
        for participant in self.participants:
            polled_num_set.add(int(participant.polled_counter))
  
        min_poll_num = min(polled_num_set)
      
        qualified_participants = []
        for participant in self.participants:
            if int(participant.polled_counter) == min_poll_num:

                qualified_participants.append(participant)
    
        if (len(qualified_participants) > 0):
            self.random_index = random.randint(0,len(qualified_participants)-1)
            self.selected_participant = qualified_participants[self.random_index]
            self.execution_attempts += 1
        else:
            self.selected_participant = None
        
        return self.selected_participant
    def correct(self):
        if self.random_index != -1:
            self.selected_participant.increase_correct_counter()
            self.random_index = -1
        else:
            raise Exception("Index of participant not found")
    
    """Increment the Participant correct value by one.

    Increment the correct value of the Participant in random_index in the participants list

    Raises:
        Exception: Index of participant not found.
    """
    def attempted(self):
        if self.random_index != -1:
            self.selected_participant.increase_attempted_counter()
            self.random_index = -1
        else:
            raise Exception("Index of participant not found")
    def excused(self):
        if self.random_index != -1:
            self.selected_participant.increase_excused_counter()
            self.random_index = -1
        else:
            raise Exception("Index of participant not found")
    def missing(self):
        if self.random_index != -1:
            self.selected_participant.increase_polled_counter()
            self.random_index = -1
        else:
            raise Exception("Index of participant not found")
    def stop(self): 
        sys.exit("End of program")
    def total(self):
        print(self.execution_attempts)

p = Poller("./data/participants.csv")
p.total()

'''

'''