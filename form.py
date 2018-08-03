from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    publisher = StringField('Publisher', validators=[DataRequired()])
    book_title = StringField('Book title', validators=[DataRequired()])