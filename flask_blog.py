from flask import Flask as f
app = f(__name__)  #create instance


@app.route('/')  #create route otherwise it  will give error 404..
def hello():
    return 'Hello Flask'


if __name__ == 'main':
    app.run()

    
