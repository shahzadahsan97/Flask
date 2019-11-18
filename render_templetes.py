from flask import Flask  , render_template
app = Flask(__name__) 

@app.route('/') 
def hello():
    return render_template('home.html') #it goes to html file....

@app.route('/about')
def about():
    return render_template('aboutt.html') #it goes to about.html file.....



if __name__ == 'main':
    app.run(debug=True) 