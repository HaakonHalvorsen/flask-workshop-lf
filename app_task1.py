from flask import Flask

app = Flask(__name__)

# Only run this when code is runned directly by Python interpreter
# Not runned during import
if __name__ == '__main__':
    app.run(debug=True)
    
@app.get("/")
def get_world():
    return "Hello world!"