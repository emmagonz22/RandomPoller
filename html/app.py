from flask import Flask, render_template, url_for, redirect, request

import os 
import csv
import random
import jsonpickle

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', get_random_participant=get_random_participant)


@app.route('/participants/')
def participants():
    participants = []
    openDialog = False
    with open("../data/participants.csv", "r") as filecsv:
        participant_csvfile = csv.reader(filecsv, delimiter=" ")
        print(participant_csvfile)
        for participant in participant_csvfile:
            tmp_list = [participant[0]]
            explode = participant[1].split(',')
            tmp_list.extend(explode)
            participants.append(tmp_list)
                
            
    print(participants)
    return render_template('participants.html', participants=participants, openDialog=openDialog)

@app.route('/add_participants/', methods=['POST'])
def add_participant():
    new_row = [request.form["name"], 0, 0, 0, 0]
    
    with open("../data/participants.csv", "a") as filecsv:
        participant_csvfile = csv.writer(filecsv)
        participant_csvfile.writerow(new_row)
    return redirect(url_for('participants'))
    
@app.route('/delete_participants/', methods=['POST', 'GET'])
def delete_participant(): ## Search participant by name and delete (This is going to change after and ID is assigned)
    print("Se va a borrar: " + request.form.get("delete-participant-name"))
    lines = list()

    with open('../data/participants.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == request.form.get("delete-participant-name"):
                    lines.remove(row)

    with open('../data/participants.csv', 'w') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(lines)

    return redirect(url_for('participants'))


@app.route('/get_random_participant/', methods=['GET', 'POST'])       
def get_random_participant():

    all_participants = []
    polled_num_set = set()
    with open("../data/participants.csv", "r") as filecsv:
        participant_csvfile = csv.reader(filecsv, delimiter=" ")
        for participant in participant_csvfile:
            tmp_list = [participant[0]]
            explode = participant[1].split(',')
            tmp_list.extend(explode)
            all_participants.append(tmp_list)
            polled_num_set.add(int(explode[1]))
            
    min_poll_num = min(polled_num_set)
    qualified_participants = []
    for participant in all_participants:
        if int(participant[2]) == min_poll_num:
            qualified_participants.append(participant)

    if (len(qualified_participants) > 0):
        random_participant_index = random.randint(0,len(qualified_participants)-1)
        selected_participant = qualified_participants[random_participant_index]
    else:
        selected_participant = "There is not participant that qualifies"

    return jsonpickle.encode(selected_participant)
@app.route('/increment_participant_value/<participant>/<action>', methods=['GET', 'POST'])    
def increment_participant_value(name, action):
    print("Increment participant", name , action)
    participants = []
    with open("../data/participants.csv", "r") as filecsv:
        participant_csvfile = csv.reader(filecsv, delimiter=" ")
        for participant in participant_csvfile:
            tmp_list = [participant[0]]
            explode = participant[1].split(',')
            tmp_list.extend(explode)
            participants.append(tmp_list)

    for participant in participants:
        if participant[0] + " " + participant[1] == name:
            if action == "correct":
                participant[3] = 1 + int(participant[3])
            elif action == "attempted":
                participant[4] = 1 + int(participant[4])
            elif action == "excused":
                participant[5] = 1 + int(participant[5])
            participant[2] = 1 + int(participant[2])

    with open('../data/participants.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(participant)
    
    return "Participant have been modified"

if __name__ == '__main__':

    app.run(debug=True)
