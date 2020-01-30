from flask import Flask, request, jsonify, redirect, url_for, make_response, render_template

app = Flask(__name__)


@app.route('/<name>/<int:age>', methods=['GET'])
def main(name, age):
    return f'Hello {name} e idade {age}', 200


@app.route('/<int:id>', methods=['POST'])
def post_test(id):
    return f'id: {id}', 200


@app.route('/request', methods=['POST'])
def request_meu():
    print(request.args)
    name = request.form['name']
    age = request.form['age']
    person = request.args.get('person')
    print(person)
    return f'Hello my name is {name} and age {age}', 200


@app.route('/response', methods=['POST'])
def response():
    obj = {
        'username': 'fosilva',
        'facebook': 'https://fb.me/fosilva',
        'notas': ['10', '8'],
        'perfil': {
            'anos': ['2019', '2020']
        }

    }

    return jsonify(user=obj), 200


@app.route('/redirect', methods=['GET'])
def redirecionar():
    return redirect(url_for('redirecionado'))


@app.route('/redirecionado', methods=['GET'])
def redirecionado():
    return 'Redirecionando', 200


@app.route('/audios', methods=['GET', 'POST', 'PUT'])
def audios():
    resp = make_response(jsonify(data=request.form), 201)
    resp.headers['Dono'] = 'Fernando'
    return resp


@app.route('/view/<name>', methods=['GET'])
def main_view(name):
    return render_template('main.html', name=name)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        return redirect(url_for('main_view', name=request.form['name']))


@app.errorhandler(404)
def page_not_found(d):
    print(d)
    return render_template('404.html', erro=d), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
