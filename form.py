from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# Create our form by extending FlaskForm.
class BookForm(FlaskForm):
    # Set field types to a variable name. Choose validators needed.
    # Refer to WTForms docs for more Field types and validators.
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    publisher = StringField('Publisher', validators=[DataRequired()])
    book_title = StringField('Book title', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])