from flask import Flask, render_template

app=Flask(__name__)

@app.route('/', methods=['GET'])
def home():
 return render_template("index.html")
 
@app.route('/msg/<msg>', methods=['GET'])
def msg(msg):
 return msg
 
if __name__=='__main__':
 app.run(host="0.0.0.0", port="88")