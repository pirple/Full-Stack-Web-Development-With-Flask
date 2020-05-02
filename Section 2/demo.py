from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/football', methods=['GET'])
def football():
    return render_template('football.html')

if __name__ == '__main__':
    app.run(port = 7000, debug= True)
