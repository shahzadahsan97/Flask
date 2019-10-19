from flask import Flask as f
app = f(__name__)  #create instance

# app.debug = True

@app.route('/')  #create route otherwise it  will give error 404..
def hello():
    return 'Hello Flask111'


if __name__ == 'main':
    app.run(debug=True)   # if we add debug = true its mean that we dont have to refresh our page again n again...

    
