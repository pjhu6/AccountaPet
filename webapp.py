from flask import Flask, render_template
import petbehavior
import foodrecc
import pet_setup

app = Flask(__name__)

pet = pet_setup.VirtualPet("Fluffy", "cat", 3)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/pet_status')
def pet_status():
    return render_template('pet_status.html', pet=pet)

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run()
