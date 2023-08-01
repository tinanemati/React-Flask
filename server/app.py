from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
import rainbow as rb

app = Flask(__name__)

# Define the directory where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# TODO: Add option for allowed extentions so we get the extentions we need for agilent files

# TODO: Function for the handeling added files with the approved extentions 

# Enable CORS for all routes on your app
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('file')  # Get the list of files

    if not files:
        return jsonify({"error": "No file selected"}), 400

    success_count = 0
    for file in files:
        if file.filename == '':
            return jsonify({"error": "One or more selected files have no filename"}), 400

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        success_count += 1

    if success_count == len(files):
        return jsonify({"message": "All files uploaded successfully"}), 200
    else:
        return jsonify({"error": "Some files failed to upload"}), 500

if __name__ == '__main__':
    app.run(debug=True)
