import sqlite3
import re
from flask import Flask, request, jsonify

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"

# Step 4: Parse Rules into an AST
def parse_expression(expression):
    tokens = re.findall(r"[()<>!=]+|AND|OR|NOT|[a-zA-Z0-9_']+", expression)

    def build_ast(tokens):
        if not tokens:
            return None
        token = tokens.pop(0)
        
        if token == "(":
            left = build_ast(tokens)
            operator = tokens.pop(0)
            right = build_ast(tokens)
            tokens.pop(0)  # Remove closing parenthesis ')'
            return Node("operator", operator, left, right)
        
        elif re.match(r"[a-zA-Z_]+", token):
            # Return operand node with value as token
            return Node("operand", token)

        return None

    return build_ast(tokens)

# Step 5: Combine Rules into a Single AST
def combine_rules(rules, operator="AND"):
    if not rules:
        return None
    
    combined = rules[0]
    
    for rule in rules[1:]:
        combined = Node("operator", operator, combined, rule)
    
    return combined

# Step 6: Evaluate Rule Against User Data
def evaluate_rule(node, data):
    if not node:
        return False
    
    if node.type == "operand":
        # Assuming operand value is a key in data and returns true if it's present
        return data.get(node.value, False)
    
    if node.type == "operator":
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)
        
        if node.value == "AND":
            return left_result and right_result
        elif node.value == "OR":
            return left_result or right_result
        elif node.value == ">":
            return left_result > right_result
        elif node.value == "<":
            return left_result < right_result
        elif node.value == "==":
            return left_result == right_result
        elif node.value == "!=":
            return left_result != right_result
        # Add other operators as needed

    return False

# Step 5 (part of the script): Database Setup
def setup_database():
    conn = sqlite3.connect("rules.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_name TEXT,
        rule_expression TEXT
    )""")
    conn.commit()
    conn.close()

# Step 6 (part of the script): Flask API Setup
app = Flask(__name__)

@app.route("/create_rule", methods=["POST"])
def create_rule():
    rule_expression = request.json.get("rule")
    ast = parse_expression(rule_expression)
    
    # Save rule to database
    conn = sqlite3.connect("rules.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_name, rule_expression) VALUES (?, ?)", ("Rule", rule_expression))
    conn.commit()
    conn.close()
    
    return jsonify({"ast": str(ast)})

@app.route("/combine_rules", methods=["POST"])
def combine():
    rules = request.json.get("rules")
    combined = combine_rules([parse_expression(r) for r in rules])
    return jsonify({"combined_ast": str(combined)})

@app.route("/evaluate", methods=["POST"])
def evaluate():
    rule_ast = parse_expression(request.json.get("ast"))
    data = request.json.get("data")
    result = evaluate_rule(rule_ast, data)
    return jsonify({"result": result})

# Run Flask application
if __name__ == "__main__":
    setup_database()  
    app.run(debug=True)
