from argparse import ArgumentParser
from poller import Poller
from subprocess import run
from mock_open import mock_open


parser = ArgumentParser(prog = "RandoPoll",
                    description = "What the program does")
parser.add_argument("filename")

args = parser.parse_args()

def main():
    with Poller(args.filename, mock_open(["Juan Perez,1,0,1,0"])) as poller:
        for participant in poller:
            while True:
                print("%s: (A)nswered (C)orrect (E)xcused (M)issing (Q)uit" % participant)
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
                    poller.stop()
                    break
                elif command == "m":
                    poller.missing()
                    break
                print("Unknown response")         

if __name__ == "__main__":
    main()