from flask import Flask, render_template, url_for
import os 
import csv


app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/participants/')
def participants():
    participants = []

    with open("../data/participants.csv", "r") as filecsv:
        participant_csvfile = csv.reader(filecsv, delimiter=" ")
        print(participant_csvfile)
        for participant in participant_csvfile:
            tmp_list = [participant[0]]
            explode = participant[1].split(',')
            tmp_list.extend(explode)
            participants.append(tmp_list)
                
            
    print(participants)
    return render_template('participants.html', participants=participants)

if __name__ == '__main__':
    app.run(debug=True)