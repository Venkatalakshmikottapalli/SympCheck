# SympCheck

SympCheck is a health diagnostic tool that identifies potential diseases based on user-provided symptoms.

## Project Structure
```sh
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

```
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



# Git Workflow for SympCheck Project

This README file provides the essential Git commands used in the development process of the SympCheck project.

## Branching Strategy

### 1. Check Current Branch
```bash
git branch
```
- **Explanation:** Lists all branches and highlights the current branch.

### 2. Switch to `master` Branch
```bash
git checkout master
```
- **Explanation:** Switches to the `master` branch, which holds the production-ready code.

### 3. Create a `develop` Branch
```bash
git checkout -b develop
```
- **Explanation:** Creates a new `develop` branch from `master` and switches to it.

### 4. Push `develop` Branch to GitHub
```bash
git push -u origin develop
```
- **Explanation:** Pushes the `develop` branch to the remote repository and sets it to track the remote `develop` branch.

## Development Workflow

### 5. Stage All Changes
```bash
git add .
```
- **Explanation:** Stages all changes in the working directory for the next commit.

### 6. Commit Changes
```bash
git commit -m "Your commit message"
```
- **Explanation:** Commits the staged changes with a descriptive message.

### 7. Push Changes to `develop` Branch
```bash
git push origin develop
```
- **Explanation:** Pushes the committed changes in the `develop` branch to the remote repository.

## Merging `develop` into `master` for Production

### 8. Switch to `master` Branch
```bash
git checkout master
```
- **Explanation:** Switches back to the `master` branch before merging.

### 9. Pull Latest Changes from `master`
```bash
git pull origin master
```
- **Explanation:** Updates the local `master` branch with the latest changes from the remote repository.

### 10. Merge `develop` into `master`
```bash
git merge develop
```
- **Explanation:** Merges the `develop` branch into `master`, incorporating the new features or fixes.

### 11. Push Merged `master` to GitHub
```bash
git push origin master
```
- **Explanation:** Pushes the updated `master` branch to the remote repository to update production code.

## Resuming Development

### 12. Switch Back to `develop` Branch
```bash
git checkout develop
```
- **Explanation:** Switches back to the `develop` branch to continue working on new features or fixes.




