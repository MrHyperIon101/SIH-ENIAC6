# SIH.2024.ENIAC6
_For those people who want to collaborate in GitHub, Follow the steps below:_
1. Download Git For Windows from your preferred browser. During Installation dont interfare with any customized options.
2. Open Github, and create a fork of this repository on your profile.
3. Create a folder on your drive where you want to work on this repo. Then go to the address bar, and click on it. Then Type CMD and a command prompt window will open.
4. then type:  git clone ___(Paste the HTTPS link of this repo in the blank space)
5. Then Type code ____(Paste the HTTPS link of this repo in the blank space)
6. Then type:  code./
7. It will finally open a VS Code Windows with your directory connected.
8. Now Here are some prerequisites required to be installed on your pc to run the aforementioned code.
_To run the provided Flask application, you need to install several Python modules. Here is a list of the required modules and how you can install them:
Flask: This is the main framework used to create the web application.

pip install Flask

NLTK (Natural Language Toolkit): This is used for text processing tasks such as tokenization.

pip install nltk

CSV: The csv module is part of Python's standard library, so no additional installation is required.
OS: The os module is also part of Python's standard library, so no additional installation is required.
Datetime: The datetime module is included in Python's standard library, so no installation is needed.
Additionally, it is a good practice to use a virtual environment to manage your project's dependencies. You can set up a virtual environment and install the required packages using the following steps:
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

pip install Flask nltk
# SIH.2024.ENIAC6

Welcome to the **SIH.2024.ENIAC6** project! This guide will help you set up your environment and contribute to the project effectively.

## Collaboration Steps

_For those who want to collaborate on GitHub, follow the steps below:_

1. **Download Git**
   - Download Git for Windows from your preferred browser.
   - During installation, do not interfere with any customized options.

2. **Fork the Repository**
   - Open GitHub and create a fork of this repository on your profile.

3. **Clone the Repository**
   - Create a folder on your drive where you want to work on this repo.
   - Go to the address bar, click on it, type `CMD`, and press Enter to open a command prompt window.
   - Type: 
     ```bash
     git clone <HTTPS-link-of-this-repo>
     ```

4. **Open in VS Code**
   - Type:
     ```bash
     code <HTTPS-link-of-this-repo>
     ```
   - Then type:
     ```bash
     code .
     ```
   - This will open a VS Code window with your directory connected.

## Prerequisites

_To run the provided Flask application, you need to install several Python modules. Here is a list of the required modules and how you can install them:_

- **Flask**: This is the main framework used to create the web application.
  ```bash
  pip install Flask
- **NLTK**: NLTK (Natural Language Toolkit)
  ```bash
  pip install nltk
## Download necessary NLTK data:
In your Python script or interpreter, run:
python
import nltk
nltk.download('punkt')

By following these steps, you will have all the necessary modules installed to run your Flask application._

## Contribution Workflow
Now you can finally work on this code. Collaborate and add more features as much as you want. After your work is complete, do the following steps in order to upload it again to your forked repo:
1. Navigate to your project directory:

-cd SIH.2024.ENIAC6

2. For those working on code:

-cd chatbot

3. For frontend team:
- First execute the above line, then:
cd static  # For CSS
cd templates  # For HTML

4. Initialize Git (if not already initialized):

-git init

5. Check status and stage changes:

-git status
-git add <file-name>
-git status  # Ensure file is staged

6. Commit and push changes:

-git commit -m "Updated by 'Your Name'"
-git push

Congratulations!
You have successfully completed all the steps! Happy collaborating!
