@echo off

rem Create a virtual environment
python -m venv venv

rem Activate the virtual environment (for Windows)
call venv\Scripts\activate

rem Update pip
pip install --upgrade pip

rem Install required packages
pip install -r requirements.txt

rem Run Streamlit app
python -m streamlit run app.py