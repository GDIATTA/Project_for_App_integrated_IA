from flask import Flask, render_template, request, redirect, flash, url_for
from flask_scss import Scss
import psycopg2
from pymongo import MongoClient
from datetime import date
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
Scss(app)

UPLOAD_FOLDER = 'app/flask/static/uploads/'
  
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
  
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# function which allows to connect from my database
#def get_db_connect():
#    conn = psycopg2.connect(host="localhost",
#                             user="postgres",
#                             database="flask_db",
#                             password="root")
#    return conn

# MongoDB connection setup
def get_db_connect():
    client = MongoClient(host='mongo1',
                          port=27017)
    db = client.shopify
    current_collection = db.items
    return current_collection



@app.route("/posting/", methods=["GET","POST"])
def home():
    # retrieve data posted and insert inside my table items
    if request.method=="POST":
    # upload the picture
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
          # Ensure the upload directory exists
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        items_data={
            'name' : request.form['Name'],
            'price' : request.form['Price'],
            'category' : request.form['Category'],
            'instock' : request.form['inStock'] in ['true', '1', 't', 'y', 'yes'],
            'tags' : request.form['Tags'],
            'description' : request.form['Description'],
            'filename': filename
        }


        try:
            current_collection = get_db_connect()
            items=current_collection.insert_one(items_data)
            return redirect("/")
        except Exception as e:
            return f"error {e}"
    
    else:
        return render_template("posting.html")

    
    
        
@app.route("/", methods=["GET"])
def posting():
    try:
        current_collection = get_db_connect()
        items=current_collection.find()
        return render_template("home.html",items=items)
    except Exception as e:
        return f"Error {e}"
        
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('app/flask/static/', filename='uploads/' + filename), code=301)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


