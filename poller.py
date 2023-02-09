import os 
import csv
import random
import sys

class Participant:
    """Participant model with name and polled information

    The Participant class is the model on which contains the name of the particpant, it also include
    how many times the participant was polled and how many times it was correct, attempted, excused and missing
    when the participant is missing the polled counter increase and the other counter are unaffected.

    Attributes:
        polled_counter: A integer indicating the number of time a participant was poll.
        correct_counter: A integer indicating the number of time a participant was poll.
        attempted_counter: A integer indicating the number of time a participant was poll.
        excused_counter: A integer indicating the number of time a participant was poll.
    """
    def __init__(self, name: str, poll_counter: int,correct_counter: int, attempted_counter: int , excused_counter: int):
        ##<name>,<#polled>,<#correct>,<#attempted>,<#excused>
        self.name : int = name
        self.poll_counter : int = poll_counter
        self.attempted_counter : int = attempted_counter
        self.correct_counter : int = correct_counter
        self.excused_counter : int = excused_counter
   
      
    def __str__(self):
        return f"{self.name},{self.poll_counter},{self.correct_counter},{self.attempted_counter},{self.excused_counter}"

    def increase_attempted_counter(self):
        """Increment the attempt and poll counter"""
        self.attempted_counter += 1
        self.poll_counter += 1

    def increase_correct_counter(self):
        """Increment the correct and poll counter"""
        self.correct_counter += 1
        self.poll_counter += 1

    def increase_excused_counter(self):
        """Increment the excused and poll counter"""
        self.excused_counter += 1
        self.poll_counter += 1

    def increase_poll_counter(self):
        """Increment the poll counter"""
        self.poll_counter += 1


class Poller:
    """The poller class returns in the _next__ a random participant with the less possible amount of poll

    The Poller class 

    Attributes:
        filename: A string indicating the name of the csv file .
        open_file: Open function use for dependecy injection, this should only be use for testing if not leave the default function

    """
    def __init__(self, filename: str, open_file = open):
        """Inits Poller class with the filename and the participant list that is going to be filled with the data in the filename, the execution_attempts count how many times a participant was selected by __next__
        The selected_participant is a variable that holds the user selected by __next__, continue_iteration is use to stop the program"""
        self.filename : str = filename
        self.participants = []
        self.execution_attempts = 0
        self.selected_participant = None
        self.open_file = open_file
        self.continue_iter: bool = True
        
    def __enter__(self):
        """Enters Poller class and it fill the data of the filename csv to the participants list."""
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
        """Exit Poller class and overwrite (save) the current participants list to the filename"""
        formated_list = []
        
        for participant in self.participants:
            participant_lst = [participant.name, participant.poll_counter, participant.correct_counter, participant.attempted_counter, participant.excused_counter]
            formated_list.append(participant_lst)
        ##
        with self.open_file(self.filename, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(formated_list)

        #self.participant_csvfile.close()
    def __iter__(self):
        """Create the random iteration index variable."""
        self.random_index = -1
        return self
    def __next__(self): 
        """Select next random participant with less poll in the filename csv
        
        The __next__ select next random participant with less poll in the filename csv if the participant list is empty is going to 
        assign None to the self.selected_participant
        
        
        Raises:
            StopIteration: Quitting the program
        """
        if not self.continue_iter:
            raise StopIteration()
        polled_num_set = set()
        for participant in self.participants:
            polled_num_set.add(int(participant.poll_counter))
  
        #Get the minimum number of polled in the entire file
        min_poll_num = min(polled_num_set)

        #Create and fill a list with the participants with the minimum poll num
        qualified_participants = []
        for participant in self.participants:
            if int(participant.poll_counter) == min_poll_num:

                qualified_participants.append(participant)
        #If there is a participant in the file is going to select a random participant that have the less poll in the participant list
        if (len(qualified_participants) > 0):
            self.random_index = random.randint(0,len(qualified_participants)-1)
            self.selected_participant = qualified_participants[self.random_index]
            self.execution_attempts += 1
        else:
            self.selected_participant = None
    
        return self.selected_participant
    def correct(self):
        """Increment the Participant correct value by one.

        Increment the correct value of the Participant in random_index in the participants list
        """
        self.selected_participant.increase_correct_counter()

    

    def attempted(self):
        """Increment the Participant attempt value by one.

        Increment the attempted value of the Participant in random_index in the participants list

        """
        self.selected_participant.increase_attempted_counter()

    def excused(self):
        """Increment the Participant excused value by one.

        Increment the excused value of the Participant in random_index in the participants list
        
        """
        self.selected_participant.increase_excused_counter()
     
    def missing(self):
        """Increment the Participant missing value by one.

        Increment the missing value of the Participant in random_index in the participants list

        """
    
        self.selected_participant.increase_poll_counter()

    def stop(self): 
        """Stop the program"""
        self.continue_iter = False
        print("End of program")

    
    def total(self): 
        """Returns print the total number of participant polled during execution"""
        print(f"The total number of person called: {self.execution_attempts}")
        return self.execution_attempts


