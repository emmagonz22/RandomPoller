import os 
import csv
import random

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

    def participate(self):
        self.attempted_counter += 1

    def increase_correct_counter(self):
        self.correct_counter += 1
    
    def increase_excused_counter(self):
        self.excused_counter += 1

    def increase_polled_counter(self):
        self.polled_counter += 1


class Poller:
    def __init__(self, filename: str):
        self.filename : str = filename
        self.participants = []
        self.execution_attempteds = 0
    def __enter__(self):
        if os.stat("./data/participant.csv").st_size == 0:
            raise ValueError("File is empty")
        else:
            with open(self.filename, "r") as filecsv:
                participant_csvfile = csv.reader(filecsv, delimiter=" ")
                print(participant_csvfile)
                for participant in participant_csvfile:
                    explode_line = participant[1].split(',')                
                    self.participants.append(  Participant(f"{participant[0]} {explode_line[0]}",explode_line[1],explode_line[2],explode_line[3],explode_line[4])  )
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        formated_list = []
        
        for participant in self.participants:
            participant_lst = [participant.name, participant.polled_counter, participant.correct_counter, participant.attempted_counter, participant.excused_counter]
            formated_list.append(participant_lst)

        with open('../data/participants.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(formated_list)

        #self.participant_csvfile.close()
    def __iter__(self):
        self.current_index = 0
        return self
    def __next__(self): #Fix to select random participant


        polled_num_set = set()
        for participant in self.participants:
            explode = participant[1].split(',')
            polled_num_set.add(int(explode[1]))
                
        min_poll_num = min(polled_num_set)
        qualified_participants = []
        for participant in self.participants:
            if int(participant[2]) == min_poll_num:
                qualified_participants.append(participant)

        if (len(qualified_participants) > 0):
            random_participant_index = random.randint(0,len(qualified_participants)-1)
            selected_participant = qualified_participants[random_participant_index]
        else:
            selected_participant = None

        return selected_participant
    def select_random_participant(self):
        pass
    def correct(self):
        pass
    def attempted(self):
        pass
    def excused(self):
        pass
    def missing(self):
        pass    
    def stop(self): #Research
        pass
    def total(self):
  
        for participant in self.participants:
            print(str(participant))

p = Poller("./data/participants.csv")
p.total()
p.stop()


'''

'''