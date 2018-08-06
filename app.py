from flask import Flask, render_template, redirect, url_for, session
from form import BookForm

app = Flask(__name__)

# Set secret for CSRF protection from Flask WTF to work.
app.secret_key = "thisissupersecret"

@app.route("/", methods=('GET', 'POST'))
def book():

    # Set BookForm so we can send it's data to the template for rendering.
    form = BookForm()

    if form.validate_on_submit():
        # Save form data to special Flask session. This
        # persists data for the entire client's session
        # with the server.
        session['first_name'] = form.first_name.data
        session['last_name'] = form.last_name.data
        session['publisher'] = form.publisher.data
        session['book_title'] = form.book_title.data
        session['year'] = form.year.data
        # Reset the form field to blank.
        form.first_name.data = ''
        form.last_name.data = ''
        form.publisher.data = ''
        form.book_title.data = ''
        form.year.data = ''
        # redirect after form submit.
        return redirect(url_for('book'))

    # Set the key we will be testing for.
    key = 'year'

    # See if the key exists already, if it does, then send the session data
    # to the template.
    if key in session:
        return render_template("book.html", 
                                first_name=session['first_name'], 
                                last_name=session['last_name'], 
                                publisher=session['publisher'],
                                book_title=session['book_title'],
                                year=session['year'],
                                form=form)
    
    # If it doesn't exist, render the template without sending the session data.
    else:
        return render_template("book.html", form=form)

# This is an example of another route for translated books.
@app.route('/trans-book')
def trans_book():
    return render_template('trans_book.html')