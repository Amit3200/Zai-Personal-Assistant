from flask import Flask
app= Flask(__name__)
@app.route('/hello')
def hello_world():
    html="""
    <html>
    <h1>Welcome Flask</h1>
    </html>
"""
    return(html)

