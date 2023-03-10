'''
Database = dictionary
keys -> ids for the patients
value: dict

{1: {"id": 1, "name": "David", "blood_type": "O+"},
 2: {"id": 1, "name": "David", "blood_type": "O+"},
 3: {"id": 1, "name": "David", "blood_type": "O+", "tests": []},


'''

from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type,
                   "tests": []}
    db[id] = new_patient
    print(db)


def add_test_to_db(id, test_name, test_value):
    db[id]["tests"].append((test_name, test_value))
    print(db)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # get input data
    in_data = request.get_json()
    # call other functions to do the work
    answer, status_code = new_patient_driver(in_data)
    # return a response
    return jsonify(answer), status_code


def new_patient_driver(in_data):
    # validate input
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    # do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # return an answer
    return "Patient successfully added", 200


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


def validate_input_data_generic(in_data, expected_keys, expected_types):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


@app.route("/add_test", methods=["POST"])
def post_add_test():
    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer), status_code


def does_patient_exist_in_db(id):
    if id in db:
        return True
    else:
        return False


def add_test_driver(in_data):
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    validation = validate_input_data_generic(in_data, expected_keys, expected_types)
    if validation is not True:
        return validation, 400
    does_id_exist = does_patient_exist_in_db(in_data["id"])
    if does_id_exist is False:
        return "Patient id {} does not exist in database"\
            .format(in_data["id"]), 400
    add_test_to_db(in_data["id"], in_data["test_name"], in_data["test_result"])
    return "Test successfully added", 200


if __name__ == '__main__':
    app.run()