Description:
This appliction simulates a program where users of a company are able to sign in and view tasks that need to be completed. For users that are a manager, they are able to onboard (create a new user). Managers also have the ability to assign tasks to users that report to them. When every user is signed in, they are able to navigate the app to see what tasks are assigned to them and mark them as complete. They can also get a task removed from the dashboard with permission from their manager.

Set up and Run Instructions:


Overview of features and functionality:
All users are able to log in, log out, view the tasks they need to complete, change the completion status of their tasks, and request to have a task deleted.
Managers users that are also able to create a new user (this new user will report to the manager), assign a task to a user that reports to them. If a manager tries to assign a task to a user that does not report to them, an error will occur.
Tasks can be deleted (to clean up a users dashboard) by pressing the delete task button. From there, the manager's password must be put in to confirm that the task can be deleted

Tech Stack Used:
For this application, react and vite were used for the frontend. For the backend, Python, Flask, and SQLAlchemy were used. 