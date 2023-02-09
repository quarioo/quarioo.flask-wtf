from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def index(prof: str):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        return render_template('base.html', prof='Инженерные тренажеры')
    return render_template('base.html', prof='Научные симуляторы')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
