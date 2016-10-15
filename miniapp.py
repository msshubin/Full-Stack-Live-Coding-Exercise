__author__ = 'ms.shubin'
from flask import Flask, render_template, flash, request
from wtforms import Form, validators, StringField
from findmodule import find

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = StringField('Enter a search string, queries Stack Exchange ', validators=[validators.required()])

class Item(object):
    def __init__(self, link, date, question, posted, answerscount):
        self.link = link
        self.date = date
        self.question = question
        self.posted = posted
        self.answerscount = answerscount

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print
    form.errors
    Items = []
    qount = None

    if request.method == 'POST':
        name = request.form['name']
        print
        name

        if form.validate():
            qs = find(name)
            qount = 0
            for q in qs:
                Items.append(Item(q.link, q.creation_date.strftime("%d.%m.%Y"), q.title, q.owner.display_name if hasattr(q, 'owner') else '', q.answer_count))
                qount += 1

        else:
            Items = []
            qount = 0

    return render_template('hello.html', form=form, qount = qount, Items = Items)

if __name__ == "__main__":
    app.run()