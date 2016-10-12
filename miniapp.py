from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from findmodule import find
from flask_table import Table, Col

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = StringField('Enter a search string, queries Stack Exchange ', validators=[validators.required()])

class Item(object):
    def __init__(self, link, date, question, posted, haveanswer):
        self.link = link
        self.date = date
        self.question = question
        self.posted = posted
        self.haveanswer = haveanswer

class ItemTable(Table):
    link = Col('Link')
    date = Col('Question date')
    question = Col('Question')
    posted = Col('Author')
    haveanswer = Col('Answered')

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print
    form.errors

    if request.method == 'POST':
        name = request.form['name']
        print
        name

        if form.validate():
            Items = []
            qs = find(name)
            for q in qs:
                try:
                    Items.append(Item('/<a href=' + q.link + '/>link/</a/>', q.creation_date.strftime("%d.%m.%Y"), q.title, q.owner.display_name, 'v' if q.answer_count > 0 else ''))
                except:
                    Items.append(Item('/<a href=' + q.link + '/>link/</a/>', q.creation_date.strftime("%d.%m.%Y"), q.title, '', 'v' if q.answer_count > 0 else ''))

            table = ItemTable(Items)
            flash('some', )
            flash(table)
        else:
            flash('Enter something please')

    return render_template('hello.html', form=form)

if __name__ == "__main__":
    app.run()