from flask import Flask, request, jsonify 
import json

app = Flask(__name__)

path= "task.json"


def read_file():
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def write_file(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


@app.route('/create_task', methods=['POST'])
def create_tasks():

    incoming_data = request.get_json()
    
    if not incoming_data:
        return jsonify({"error": "No data was provided"}), 400


    status = incoming_data.get("task_status", "").strip().lower()

    permitted_statuses = {
        "to do": "To do",
        "in progress": "In progress",
        "completed": "Completed"
    }
    
    if status not in permitted_statuses:
        return jsonify({"error": "Invalid status. Please add 'To do', 'In progress', or 'Completed'"}), 400

    new_task = {
        "identifier": incoming_data.get("identifier"),
        "task_title": incoming_data.get("task_title"),
        "task_description": incoming_data.get("task_description"),
        "task_status": permitted_statuses[status]
    }
    

    if not all(new_task.values()):
        return jsonify({"error": "All fields must be completed"}), 400  

    entries = read_file()

    identifier_exists = False
    for entry in entries:
        if entry.get("identifier") == new_task["identifier"]:
            identifier_exists = True
            break

    if identifier_exists:   
        return jsonify({"error": "Task with this identifier already exists"}), 400
    
    file = read_file()
    file.append(new_task)
    write_file(file)

    return jsonify({"message": "Task created successfully", "task": new_task}), 201
    


@app.route('/view_tasks', methods=['GET'])
def get_data():
    data = read_file()
    if not data:
        return jsonify({"error": "No tasks found"}), 404
    return jsonify(data), 200


@app.route('/view_task/<task_status>', methods=['GET'])
def get_task_by_status(task_status):
    data = read_file()
    filtered_data = []
    for task in data:
        if task["task_status"].lower() == task_status.lower():
            filtered_data.append(task)
    
    if not filtered_data:
        return jsonify({"message": "No task found with the given status"}), 404
    
    return jsonify(filtered_data), 200


@app.route('/update_task/<identifier>', methods=['PUT'])
def update_task(identifier):
    incoming_data = request.get_json()
    
    if not incoming_data:
        return jsonify({"error": "No data provided"}), 400

    if "identifier" in incoming_data and incoming_data["identifier"] != identifier:
        return jsonify({"error": "Identifier cannot be updated"}), 400

    allowed_fields = {"task_title", "task_description", "task_status"}

    in_allowed_fields = False

    for field in allowed_fields:
        if field in incoming_data:
            in_allowed_fields = True
            break       

    if not in_allowed_fields:
        return jsonify({"error": "At least one field (task_title, task_description, task_status) must be provided to update"}), 400
    
    status = incoming_data.get("task_status", "").strip().lower()

    permitted_statuses = {
        "to do": "To do",
        "in progress": "In progress",
        "completed": "Completed"
    }

    if "task_status" in incoming_data:
        if status not in permitted_statuses:
            return jsonify({"error": "Invalid status. Must be 'To do', 'In progress', or 'Completed'"}), 400

        incoming_data["task_status"] = permitted_statuses[status]
    
    

    data = read_file()

    for task in data:
        if str(task["identifier"]) == str(identifier):
            for field in allowed_fields:
                if field in incoming_data:
                    task[field] = incoming_data[field]
            write_file(data)
            return jsonify({"message": "Task updated successfully", "task": task}), 200

    return jsonify({"error": "Task not found"}), 404



@app.route('/delete_task/<identifier>', methods=['DELETE'])
def delete_task(identifier):
    data = read_file()

    new_data = []
    for task in data:
        if str(task["identifier"]) != str(identifier):
            new_data.append(task)

    if len(new_data) == len(data):
        return jsonify({"error": "Task not found with the identifier"}), 404

    write_file(new_data)
    return jsonify({"message": f"Task with identifier {identifier} deleted successfully"}), 200



if __name__ == "__main__":
    app.run(host= "localhost", debug=True)


