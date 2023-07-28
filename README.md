### React-Flask File Upload 

This application allows the user to upload files to their web applicaton. 

The user will be invoked to import a file from the website, after the file has been uploaded successfuly, we can see it in the upload folder of the flask backend. 

## How to run the application 

1. Set Up the Backend: Make sure you have Python and Flask installed on your system. If not, install them using pip: `pip install flask` 

2. Create the Uploads Folder: Create a folder named "uploads" in the same directory as your app.py file. This folder will be used to store the uploaded files

3. Run the flask backend by running the `app.py` file as follows: `python app.py` 

4. Set up the Frontend: Make sure you have Node.js, npm and axios dependency installed
    - You can install the dependency using: `npm install axios` 

5. Run the frontend: `npm start` 
    - The react app will be available at `http://localhost:3000/`


## How to test the functionality of the application

- Select one or more files to upload using file input and click the "upload button"
    - if the upload is successful, you should see a success message 
    - if there was an issue, an error messsage displays on

- Check the "uploads" folder, in the server directory to ensure that the files have been uploaded and successfully saved. 
