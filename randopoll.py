from argparse import ArgumentParser, BooleanOptionalAction
from poller import Poller
from subprocess import run
from mock_open import mock_open



"""

Task to  do

keep track dont call 
Add flag to command line to commit like --save
Focus on unit test --priotity
write integration test

"""

parser = ArgumentParser(prog = "RandoPoll",
                    description = "Select a random participant from the participants.csv with the lowest poll")
parser.add_argument("filename")
parser.add_argument("-c", "--commit", dest="commit_message", help="Add participant.csv and commit changes with the inserted message", type=str)
parser.add_argument("-p", "--push", action=BooleanOptionalAction, help="When use in convinatition of -c it push the commit to remote repo")

args = parser.parse_args()
print(args)
def main():
    print(f"Welcome to RandoPoll if you want to commit the participant.csv add the flag -c following with the message and -p to push to remote repo after quiting the program")
    with Poller(args.filename) as poller:
        for participant in poller:
            while True:
                print("%s: (A)nswered (C)orrect (E)xcused (M)issing (T)otal (Q)uit" % participant)
                command = input().lower()
                if command == "a":
                    poller.attempted()
                    break
                elif command == "c":
                    poller.correct()
                    break
                elif command == "e":
                    poller.excused()
                    break
                elif command == "q":
                    if args.commit_message:
                        #subprocess call
                        run(["git", "add", './data/participants.csv'])
                        run(["git", "commit", "-m", args.commit_message])
                        if args.push:
                            run(["git", "pull"]) #Update branch before pushing
                            run(["git", "push"])
                    poller.stop()
                    break
                elif command == "m":
                    poller.missing()
                    break
                elif command == "t":
                    poller.total()
                    break
                print("Unknown response")         

if __name__ == "__main__":
    main()