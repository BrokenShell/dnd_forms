from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/monster')
def monster():
    return render_template('monster.html')

@app.route('/monster-results')
def monster_results():
    return render_template('monster-results.html')

@app.route('/trap')
def trap():
    return render_template('trap.html')

@app.route('/trap-results')
def trap_results():
    return render_template('trap-results.html')

@app.route('/dungeon')
def dungeon():
    return render_template('dungeon.html')

@app.route('/dungeon-results')
def dungeon_results():
    return render_template('dungeon-results.html')


if __name__ == "__main__":
    app.run()