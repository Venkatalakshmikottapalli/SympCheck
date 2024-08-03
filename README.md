# SympCheck

SympCheck is a health diagnostic tool that identifies potential diseases based on user-provided symptoms.

## Project Structure

Symp_check_UI_project/
├── app/
│ ├── components/
│ │ └── header_component.py
│ ├── pages/
│ │ └── main.py
│ ├── styles/
│ │ └── style.css
│ ├── utils/
│ │ ├── helper_functions.py
│ │ └── config.py
│ ├── assets/
│ │ └── queries.csv
├── .gitignore
├── README.md
├── requirements.txt


## How to Run

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    set the path
    $env:PYTHONPATH="$env:PYTHONPATH;."

2. Start the application:
    ```sh
    streamlit run app/pages/main.py
    ```

## Configuration

- The API URL can be configured in `app/utils/config.py`.

## Deployment

- For deployment, ensure that all dependencies are installed and the application is configured properly.

## License

This project is licensed under the MIT License.

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Virtual environment (optional but recommended)
- Streamlit

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/SympCheck.git
   cd SympCheck

2.  Create a virtual environment and activate it:

    python -m venv env
    env\Scripts\activate  # On Windows
    source env/bin/activate  # On macOS/Linux

3.  Install the required dependencies:

    pip install -r requirements.txt

4.  Run the Streamlit app:

    streamlit run app/pages/main.py

## Git Commands
1.  Initialize a Git Repository
    git init

2.  Create a .gitignore File
    Add the following content to .gitignore:

    # .gitignore

    __pycache__/
    *.pyc
    *.pyo
    *.pyd
    env/
    *.env
    public/assets/queries.csv

3.  Add and Commit Files
    git add .
    git commit -m "Initial commit of SympCheck project"

4.  Create and Push to GitHub Repository
    a). Create a repository on GitHub.
    b). Add remote repository URL:
        git remote add origin https://github.com/yourusername/SympCheck.git
        git remote add origin https://github.com/Venkatalakshmikottapalli/SympCheck.git
    c). Push local repository to GitHub:
        git push -u origin master
## Usage
After setting up, you can access the SympCheck app in your web browser at http://localhost:8501.



