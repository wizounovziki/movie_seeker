## SECTION 1 : Movie Seeker - Movie Recommender System

<img src="/SystemCode/frontend/public/WebBG.png"
     style="float: left; margin-right: 0px;" />

---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
The content providing website has become a trend recently. The website will provide contents in forms of many media vectors like video, audio and passages. In a time of open-source while most resources are monopolized by giants, most of the content providing websites could not earn money from the user payment, thus the data gained from the users has become a rather more important part for them to survive. 

Thus as a team of 2 who not only participate as users but also might head into such an industry to earn for living, we are keen to fully make use of the provided user data. Movie is a good object to start with, as there is existing data to use and has a long history of development which potentially has a great scale of people giving comments and it will absolutely last for a long time in the future.

In this project, we build up a movie recommendation system using the knowledge and techniques learned in classes and self-learning. We firstly find data from open source, then extend the data by using crawlers and take the extra dimensions to build up the model and algorithm. At last, we have a reactJS based frontend together with flask-api back end, not only to perform the recommendation, but also in usage of continuously collecting the data from users.  


---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Wang Futong | A0191584W | Crawler, backend development, algorithm coding and model training| e0338228@u.nus.edu |
| Ding Yuxing | A0186876E | Frontend development, backend api prototype design, modeling discussion and testing| e0321114@u.nus.edu |


---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Sudoku AI Solver](https://www.youtube.com/watch?v=Oy-dffrQq_Q "Sudoku AI Solver")[Sudoku AI Solver]

---

## SECTION 5 : USER GUIDE

### [ 1 ] Prepare basic enviorment

1. Install [nodejs (npm)](https://nodejs.org/en/download/) on the computer

2. Install yarn by typing in nodejs path : 

`$npm install yarn`

3. Install [python >=3.5](https://www.python.org/downloads/)

> Option: create an virtual enviorment of python:

`$python -m venv ./venv`

`$source activate venv/bin/activate` for Linux

`$venv/script/activate` for Windows

4. cd to the backend folder, run pip install requirements.txt

`$cd PATH/OF/Virtual`

`$pip install -r requirements.txt`

5. cd to the frontend folder, run yarn build

`$yarn build`

### [ 2 ] Run the server

6. Run the system, firstly go to the backend folder, run main.py (taking port 5001), then go to the frontend folder (taking port 3000), run yarn start. 
`$ python main.py`
`$ yarn start`
8. **Go to URL using web browser** http://0.0.0.0:3000 or http://127.0.0.1:3000
9. Account for testing:

username:user3321@test.com password:user3321 (A sample of experienced user)

username:user3323@test.com password:user3323 (A sample of new user)

---
## SECTION 6 : PROJECT REPORT / PAPER

`Refer to project report at Github Folder: ProjectReport`

**Recommended Sections for Project Report / Paper:**
- Executive Summary / Paper Abstract
- Market Reasearch
- Problem Description
- Problem Objectives
- Business Case
- Recommend System
- System Structure
- SVD++ Algorithm
- Recommendation Workflow
- Web Solution
- Movie web
- Project Scope
- Limitations
- Conclustion
- Improvements
- Appendix of report: Project Proposal
- Appendix of report: Survey on Recommmend System
- Appendix of report: Individual Project Report
- Appendix of report: Installation and User Guide
