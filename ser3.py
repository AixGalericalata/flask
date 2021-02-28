from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('n.html', prof=prof)


@app.route('/list_prof/<list>')
def prof_list(list):
    return render_template('prof_list.html', list=list)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
