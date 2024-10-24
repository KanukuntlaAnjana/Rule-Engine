## Rule Engine Application
This is a simple rule engine that parses rules, combines them into a single abstract syntax tree (AST), and evaluates them against user-provided data. The application is built using Python, SQLite, and Flask.

## Features
- **Parse rules**: Convert logical expressions into an Abstract Syntax Tree (AST).
- **Combine rules**: Combine multiple parsed rules using logical operators.
- **Evaluate rules**: Evaluate the rules against a data set.
- **SQLite storage**: Store rules persistently in an SQLite database.
- **Flask API**: Provide RESTful endpoints to interact with the rule engine.
## Requirements
Make sure you have the following dependencies installed:

- Python 3.x
- Flask
- SQLite3
- Regex (re module is part of the Python standard library)
To install the required packages, run:
- pip install Flask
## Setup
**Step 1: Clone the Repository**
- git clone <repository_url>
- cd <repository_folder>
**Step 2: Initialize the Database**
- Before running the application, ensure the SQLite database is set up by executing the following command:
- python app.py
- This will automatically create the rules.db file and set up the required database schema for storing rules.

## Usage
Running the Application
Start the Flask server with the following command:
- python app.py
The server will run in debug mode on http://127.0.0.1:5000.

## API Endpoints
1.**Create a Rule**
- **Endpoint**: /create_rule
- **Method**: POST
- **Description**: Parses a logical rule expression and saves it to the database.
- **Request Body**:
json
Copy code
{
  "rule": "your_rule_expression"
}
- **Response**:
json
Copy code
{
  "ast": "parsed_ast_representation"
}

2.**Combine Rules**

- **Endpoint**: /combine_rules
- **Method**: POST
- **Description**: Combines multiple rules into a single rule using logical operators (default: AND).
- **Request Body**:
json
Copy code
{
  "rules": ["rule1_expression", "rule2_expression"]
}
- **Response:**
json
Copy code
{
  "combined_ast": "combined_ast_representation"
}
3. **Evaluate Rule**

- **Endpoint**: /evaluate
- **Method**: POST
- **Description**: Evaluates a parsed rule against the provided data.
- **Request Body**:
json
Copy code
{
  "ast": "your_rule_expression",
  "data": {
    "key": "value"
  }
}
- **Response**:
json
Copy code
{
  "result": true/false
}
## Example Usage
**Creating a Rule**:

Copy code
- curl -X POST http://127.0.0.1:5000/create_rule -H "Content-Type: application/json" -d '{"rule": "(age > 18) AND (country == \'USA\')"}'
**Combining Rules:**

Copy code
- curl -X POST http://127.0.0.1:5000/combine_rules -H "Content-Type: application/json" -d '{"rules": ["age > 18", "country == \'USA\'"]}'
**Evaluating a Rule:**

Copy code
- curl -X POST http://127.0.0.1:5000/evaluate -H "Content-Type: application/json" -d '{"ast": "(age > 18) AND (country == \'USA\')", "data": {"age": 21, "country": "USA"}}'
## Code Structure
- **app.py**: Main application file containing the rule parsing, evaluation logic, and Flask API routes.
- **rules.db**: SQLite database file where the rules are stored.
- **Node**: Class representing a node in the Abstract Syntax Tree (AST).
License
This project is licensed under the MIT License.

**Author**
Kanukuntla Anjana
