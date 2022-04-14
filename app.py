#GET() - Is used to request data from a specified resource. when you access a websites page your
#browser makes a get request to your api. The api will return the front end that is displayed 
#in the browser
#for example - get request is printing "bye world" for us in the local host port no. 8000.

#POST() - is used to send data to the server to create or update a resource. 
#for example - changing the password of an account

#PUT() - put is used to send data to server to create or update a resource. 
#for example - put request is used to create only one copy of the resource. like signing up for the first time

#DELETE() - is used to delete a resource.
#for example - to delete an account

from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        'id' : 1,
        'title' : 'Buy groceries',
        'description' : 'milk, cheese, vegies, fruits',
        'done' : False
    },
    {
        'id' : 2,
        'title' : 'learning python',
        'description' : 'in whitehatjr',
        'done' : False
    }
]

@app.route("/ add-data", methods = ["POST()"])
def sample2():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please Provide The Data"
        }, 400)
    task={
        'id': tasks[-1]['id']+ 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "Success!!",
        "message": "The task is added successfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks,
    })



@app.route("/")
def sample():
    return("bye world")

if (__name__ == "__main__"):
    app.run(debug=True, port=8000)

