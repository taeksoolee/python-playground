from flask import Flask, render_template
app = Flask(__name__)

# python flast defualt exam
@app.route('/')
def index():
    #return 'Hello Flask'
    return  render_template(
        'index.html',
        title= 'Flask Template Test',
        home_str = 'Hello Flask!',
        home_list = [1,2,3,4,5]
        )
    
@app.route('/info')
def info():
    #return 'Info'
    return  render_template('info.html')

@app.route('/ts')
def ts():
    return '<h1>taeksoo<h1>'
#if __name__ == "__main__":              
#    app.run(host="127.0.0.1", port="8080")