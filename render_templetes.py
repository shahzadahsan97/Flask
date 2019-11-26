from flask import Flask  , render_template
from data import Articles
app = Flask(__name__) 

Articles = Articles()

@app.route('/') 
def hello():
    return render_template('home.html') #it goes to html file....

@app.route('/about')
def about():
    return render_template('aboutt.html') #it goes to about.html file.....


@app.route('/articles')
def articles():
    return render_template('articles.html' , articles = Articles)



if __name__ == 'main':
    app.run(debug=True) 