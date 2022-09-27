"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from Pollock import app

@app.route('/')
@app.route('/home')

def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contact page',
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Create in the style of great artists',
    )

@app.route('/history')
def history():
    """Renders the history page."""
    return render_template(
        'history.html',
        title='History of the Artists',
        year=datetime.now().year,
        message='Find Inspiration',
    )

@app.route('/pollock')
def pollock():
    """Renders the pollock page."""
    return render_template(
        'pollock.html',
        title='Pollock',
        message='Create in the style of Pollock',
    )

@app.route('/mondrian')
def mondrian():
    """Renders the about page."""
    return render_template(
        'mondrian.html',
        title='Mondrian',
        year=datetime.now().year,
        message='Create in the style of Mondrian'
    )

@app.route('/monet')
def monet():
    """Renders the about page."""
    return render_template(
        'monet.html',
        title='Monet',
        year=datetime.now().year,
        message='Create in the style of Monet'
    )

@app.route('/sale')
def sale():
    """Renders the sale page."""
    return render_template(
        'sale.html',
        title='Gift Shop',        
        year=datetime.now().year,
        message='Create a Personalized Gift',        
    )

@app.route('/preview')
def preview():
    """Renders the sale page."""
    return render_template(
        'preview.html',
        title='Preview Your Creation',        
        year=datetime.now().year,
        message='',        
    )

