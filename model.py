import note
import fileoperation
import constants
import datetime

def create_note():
    notes = fileoperation.read_all_notes(constants.note_file_name)
    maxId = 0
    for item in notes:
        currentId = item['id']
        if maxId < currentId:
            maxId = currentId
    id_note = maxId + 1
    data_note = datetime.now()
    new_note = note.get_note(id_note, note.get_header, 
        note.get_text, data_note)
    notes['notes'].append({
        'id': new_note['id'],
        'header': new_note['header'],
        'text': new_note['text'],
        'data': new_note['data']
    })
    fileoperation.write_file_json(constants.note_file_name, notes)