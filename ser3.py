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


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    param = {}
    param['surname'] = "Watny"
    param['name'] = "Mark"
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на Марсе!'
    param['ready'] = True
    return render_template('auto_answer.html', param=param)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
