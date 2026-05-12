Step 1: Save the Python File

Save your code as:

sonar_prediction.py

Make sure:

sonar_prediction.py
sonar_data.csv

are in the SAME folder.

Example:

Streamlit_app/
│
├── sonar_prediction.py
├── sonar_data.csv
Step 2: Open Terminal

On MacBook:

Open Terminal
Go to your project folder

Example:

cd "/Users/rajsingh/Desktop/Video of sunny /Streamlit_app"
Step 3: Activate Virtual Environment

Run:

source .venv/bin/activate

After activation you will see:

(.venv)

in Terminal.

Step 4: Install Libraries

Run:

pip install pandas numpy scikit-learn
Step 5: Run the Program

Run:

python sonar_prediction.py

OR

python3 sonar_prediction.py
Expected Output
Accuracy: 0.76

or:

The object is a Rock
If Python Command Doesn't Work

Use:

python3 sonar_prediction.py
If You Want Streamlit App

Run:

streamlit run app.py

after creating the Streamlit file.
