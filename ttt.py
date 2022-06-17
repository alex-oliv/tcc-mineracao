import json


f = open('result3.json')

data = json.load(f)
f.close()


dates = [
    {"20210407": {"author": "Diego Winter", "files_changed": 1}},
    {"20210516": {"author": "Diego Winter", "files_changed": 2}},
    {"20210516": {"author": "Diego Winter", "files_changed": 7}},
    {"20210516": {"author": "Leandro Oliveira", "files_changed": 15}},
    {"20210517": {"author": "Diego Winter", "files_changed": 10}},
    {"20210518": {"author": "Leandro Oliveira", "files_changed": 15}},
    {"20210519": {"author": "Leandro Oliveira", "files_changed": 15}},
]


# Função que captura o total de arquivos modificados de um usuario durante x periodo

def count_files_changed(date, key, count):
    if not count.__contains__(date[key]['author']):
        count.update({date[key]['author']: date[key]['files_changed']})
    else:
        files = count.get(date[key]['author'])
        total_files = date[key]['files_changed'] + files
        count.update({date[key]['author']: total_files})


def total_files_changed(dates, authors_files, begin=None, final=None):
    for date in dates:
        for key in date:
            if(begin == None and final == None):
                count_files_changed(date, key, authors_files)
            elif(begin and final == None):
                if key >= begin:
                    count_files_changed(date, key, authors_files)
            elif(begin == None and final):
                if key <= final:
                    count_files_changed(date, key, authors_files)
            else:
                if key >= begin and key <= final:
                    count_files_changed(date, key, authors_files)


# print(len(data['commits']))
commit_dates = {}
total_files_changed(data['commits'], commit_dates)
print(commit_dates)
