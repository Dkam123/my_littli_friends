from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '8ae018993e9acd1794d791e91d5f0fb9'
app.config['TEMPATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('home/index.html', context={
        'page_title': 'Home page'
    })


@app.route('/about')
def about():
    return render_template('home/about.html', context={
        'page_title': 'About the site'
    })


@app.route('/news')
def news():
    return render_template('news/index.html', context={
        'page_title': 'News'
    })


@app.route('/deps')
def deps():
    return render_template('deps/index.html', context={
        'page_title': 'Departaments'
    })


@app.route('/contacts')
def contacts():
    return render_template('home/contacts.html', context={
        'page_title': 'Contacts'
    })




if __name__ == '__main__':
    app.run(debug=True)