from flask import Flask
import subprocess


app = Flask(__name__)


@app.route('/')
def hello_world():
    reply = subprocess.run(["python3", "friends_online.py", "70412660"], stdout=subprocess.PIPE)
    return reply.stdout


@app.route('/fuck')
def fuck():
    return 'fuck'


if __name__ == '__main__':
    app.run()
