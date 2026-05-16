import json

"""
#error can find the file so to resolve use __init__
with open('_data.json', 'r') as _file:
    _json_data = json.loads(_file.read())

#in case name error and any other type of error we need to use exception handling for errors
if __name__ == '__main__':
    with open('_data.json', 'r') as _file:
        _json_data = json.loads(_file.read())
    _result = ','.join([*_json_data['employees'][0]])
    for _data in _json_data['employees']:
        _result += f"\n{_data["id"]}, {_data["firstName"]}, {_data["lastName"]}, {_data["position"]}, {_data["email"]}, {_data["active"]}"
    with open('_result.csv', 'w') as _file:
        _file.write(_result)

        
if __name__ == '__main__':
    try:
        with open('_data.json', 'r') as _file:
            _json_data = json.loads(_file.read())
        _result = ','.join([*_json_data['employees'][0]])
        for _data in _json_data['employees']:
            _result += f"\n{_data["id"]}, {_data["firstName"]}, {_data["lastName"]}, {_data["position"]}, {_data["email"]}, {_data["active"]}"
        with open('_result.csv', 'w') as _file:
            _file.write(_result)
    except Exception as ex:
        print(f"Error : {ex}")

"""

#how to make it better now?
#variable for json file name and csv file name
_json_file_name = '_data.json' #input('Enter FileName')
_csv_file_name = '_result.csv'
if __name__ == '__main__':
    try:
        with open(_json_file_name, 'r') as _file:
            _json_data = json.loads(_file.read())
        _result = ','.join([*_json_data['employees'][0]])
        for _data in _json_data['employees']:
            _result += f"\n{_data["id"]}, {_data["firstName"]}, {_data["lastName"]}, {_data["position"]}, {_data["email"]}, {_data["active"]}"
        with open(_csv_file_name, 'w') as _file:
            _file.write(_result)
    except Exception as ex:
        print(f"Error : {ex}")