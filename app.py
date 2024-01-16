from flask import Flask

# init flash APP
app = Flask(__name__)

# main
@app.route('/', methods = ['GET', 'POST'])
def main():
    return 'Hello World'

if __name__ == '__main__':
    app.run("0.0.0.0", port = 80)