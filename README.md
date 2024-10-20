# Rule Engine Application

This is a simple 3-tier rule engine application that uses an Abstract Syntax Tree (AST) to determine user eligibility based on various attributes such as age, department, income, and spend.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)

## Features
- Create and store rules using a REST API
- Combine multiple rules into a single AST
- Evaluate rules against user data
- Store rules in a SQLite database

## Technologies
- Python
- Flask
- SQLite
- Docker
- Docker Compose

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/KanukuntlaAnjana/rule-engine.git
   cd rule-engine
