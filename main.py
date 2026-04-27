from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/get-user/<user_id>')
def get_user(user_id):
    userdata = {
        'user_id': user_id,
        'name': request.args.get('name'),
        'email': request.args.get('email'),
    }

    extra = request.args.get("extra")
    if extra:
        userdata['extra'] = extra

    return jsonify(userdata), 200

@app.route('/create-user')
def create_user():
    data = request.json

    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)