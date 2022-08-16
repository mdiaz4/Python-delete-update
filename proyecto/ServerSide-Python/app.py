from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)

@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)




@app.route("/person_update/<id>")
def update_person(id):
    return render_template("person_update.html", value=id)


@app.route("/person_up", methods=["POST"])
def person_up():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    for i in model:
        if i.id_person == id_person:
            model.remove(i)
            p = Person(id_person=id_person, name=first_name, last_name=last_name)
            model.append(p)
            return people()

@app.route("/person_delete/<id>")
def delete_person(id):
    for i in model:
        if i.id_person == id:
            temp = i
            model.remove(i)

    return render_template ('person_detail.html', value=("Persona Eliminada: "+ "(" + temp.id_person +" - "+temp.name + " - "+ temp.last_name + ")"))
if __name__ == '__main__':
    app.run()