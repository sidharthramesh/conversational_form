from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')


@app.route('/post',methods= ['POST'])
def submit_form():
    app.logger.info(request.form)
    return jsonify(request.form)
if __name__ == '__main__':
    app.run()
