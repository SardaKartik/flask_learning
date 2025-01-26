from flask import Flask,jsonify, request

app = Flask(__name__)

items = [
    {"id" : 1 ,"name" : "item1" , "description" : "This is item1"},
    {"id" : 2 ,"name" : "item2" , "description" : "This is item2"} 
]

@app.route('/')
def home():
    return "<html><H1>welcome to the to do list web page</H1></html>"

# Get :: Reterive all the item 

@app.route('/item',methods=['GET'])
def get_item():
    return jsonify(items)

# Get :: Reterive the item by id
@app.route('/item/<int:id>',methods=['GET'])
def get_item_by_id(id):
    item = next((item for item in items if item['id'] == id), None)
    if item == None:
        return jsonify({"message" : "Item not found"})
    return jsonify(item)

# post :: used to create a new task
@app.route('/item',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"message" : "Please provide the data in json format"})
    new_item = {
        'id' : items[-1]['id'] + 1,
        'name' : request.json['name'],
        'description' : request.json.get('description', "")
    }

    items.append(new_item)
    return jsonify({"message" : "Item added successfully"})

# put :: update an existing item

@app.route('/item/<int:id>',methods=['PUT'])
def update_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item == None:
        return jsonify({"message" : "Item not found"})
    item.update(request.json)
    return jsonify({"message" : "Item updated successfully"})

# delete :: delete an item
@app.route('/item/<int:id>',methods=['DELETE'])
def delete_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item == None:
        return jsonify({"message" : "Item not found"})
    items.remove(item)
    return jsonify({"message" : "Item deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)