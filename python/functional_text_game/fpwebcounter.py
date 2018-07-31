from flask import render_template, redirect, url_for
from fpflask import FunctionalFlask
from effect.do import do, do_return
from effect import Effect, Func, base_dispatcher

counter = 0

def increment_counter(num):
    global counter
    counter += num

def get_counter(): return counter

app = FunctionalFlask('counter')

@app.route('/')
@do
def root(request):
    counter = yield Effect(Func(get_counter))
    yield do_return(render_template('counter.html', counter=counter))

@app.route('/increment', methods=['POST'])
@do
def increment(request):
    num = int(request.form['number'])
    yield Effect(Func(increment_counter, num))
    yield do_return(redirect(url_for('root')))

if __name__ == '__main__':
    app.flask.config.update(PROPAGATE_EXCEPTIONS=True)
    app.run(base_dispatcher)
