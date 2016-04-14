from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def home():
    """
    The main page of the website. Enter questions here.
    """
    return "Hello world!"

if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
