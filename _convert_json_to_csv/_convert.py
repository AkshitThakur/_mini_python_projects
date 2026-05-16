#json to csv

import json

if __name__=='__main__':
    try:
        #Open json file
        with open('_data.json', 'r') as _file:
            _json_data = json.loads(_file.read())
        #Extrat the heading
        _result = ','.join([*_json_data['employees'][0]])
        #collect the data
        for _data in _json_data['employees']:
            _result += f"\n{_data['id']},{_data['firstName']},{_data['lastName']},{_data['position']},{_data['email']},{_data['active']}"
        #wrote the data in csv file
        with open('_result.csv', 'w') as _file:
            _file.write(_result)
    except Exception as err:
        print(f"Error : {err}")