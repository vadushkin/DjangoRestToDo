Backend Assignment: Simple Todos and Reminder API
-------------------------------------------------

The assignment involves the creation of a TODO and Reminder REST JSON API using Django. 

Create a CRUD API for a simple TODO Management application. 

TODOs are organized in boards, on every board there can be multiple TODOs. 

A TODO contains a title (str), done (bool), a created (datetime) and updated (datetime) timestamp. 
A board has a name (str).

Via a REST API it must be possible to:
-------------------------------------
* List all boards
* Add a new board
* Change a board's title
* Remove a board
* List all TODOs on a board
* List only uncompleted TODOs
* Add TODOs to a board
* Change a TODOs title or status
* Delete a TODO


User management and authentication are required.

Constraints:
-----------
*	When listing all boards the JSON should have a todo_count field, but not the list of all todos
*	In the board's detail view all todos should be serialized and the todo_count should not be visible
Reminder API
Another endpoint should allow the user to set reminders. A reminder contains an email address, a reminder text and a delay in minutes when it will be triggered.

Via the REST API it must be possible to:
---------------------------------------
*	List all reminders
*	Create a new reminder
*	Remove a reminder

After the user provided delay the user should receive an email

Constraints
-----------
Please use celery to implement the delayed execution.

How to work on the assessment:
------------------------------
*	Start working on the assignment
*	Please do periodic commits with meaningful commit messages
*	Once you are done push your final results
*	Please include a brief description how to run your solution

Please note that we don't accept solutions without periodic commits.


