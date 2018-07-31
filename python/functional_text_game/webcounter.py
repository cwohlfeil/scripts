from flask import Flask, request, render_template, redirect, url_for

counter = 0

def increment_counter(num):
    global counter
    counter += num

app = Flask('counter')

@app.route('/')
def root():
    return render_template('counter.html', counter=counter)

@app.route('/increment', methods=['POST'])
def increment():
    num = int(request.form['number'])
    increment_counter(num)
    return redirect(url_for('root'))

if __name__ == '__main__':
    app.config.update(PROPAGATE_EXCEPTIONS=True)
    app.run()
