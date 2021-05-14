from flask import Flask, render_template, Response, request, redirect, url_for
import hcskr
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route('/ok')
def ok():
    hcskr.selfcheck("정지민","060730","경기도","김포한가람중학교","중학교","0730")
    return render_template('ok.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
