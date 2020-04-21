from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# @app.route('/', methods=['GET'])
# def get():
#     return jsonify({'msg': 'Hello everyone!'})

if __name__ == '__main__':
    app.run(debug=True)