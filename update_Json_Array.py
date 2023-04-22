import json
def add_to_json_array(existing_json, new_object):

    with open("podcast.json", "w") as outfile:
        json.dump(data, outfile)

    # Load the existing JSON string into a Python list
    existing_list = json.loads(existing_json)

    # Load the new JSON string into a Python dictionary
    new_dict = json.loads(new_object)

    # Append the new dictionary to the existing list
    existing_list.append(new_dict)

    # Convert the updated list back to a JSON string
    updated_json = json.dumps(existing_list)

    # Return the updated JSON string
    return updated_json

