from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from mysql.connector import Error
# import mysql.connector
from datetime import datetime
from Connection_db import create_connection  # Ensure this is the correct path
from bookhub import create_connection, add_book, book_update, delete_book, issue_book, issue_update, delete_issue_record, submit_book  # Import your functions

app = Flask(__name__)
CORS(app)

 
# def create_connection():
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='suraj',
#             database='library_sys_db'
#         )
#         if conn.is_connected():
#             return conn
#     except Error as e:
#         print(f"Error connecting to MySQL: {e}")
#         return None

# @app.route('/')
# def home():
#     return "Library Management System API"
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Library Management System API</title>
        </head>
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
            <div style="text-align: center;">
                <h1>Library Management System API!</h1>
                <a href="http://localhost:3000" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;">
                    Go to Library Management
                </a>
            </div>
        </body>
    </html>
    """

@app.route('/books', methods=['POST'])
def add_book_api():
    data = request.json
    bname = data.get('bname')
    bcode = data.get('bcode')
    total = data.get('total')
    subject = data.get('subject')

    try:
        add_book(bname, bcode, total, subject)
        return jsonify({"message": f"Book '{bname}' added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books/<bcode>', methods=['PUT'])
def update_book_api(bcode):
    data = request.json
    new_bname = data.get('bname')
    new_total = data.get('total')
    new_subject = data.get('subject')

    try:
        book_update(bcode, new_bname, new_total, new_subject)
        return jsonify({"message": f"Book with bcode '{bcode}' updated successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books/<bcode>', methods=['DELETE'])
def delete_book_api(bcode):
    try:
        delete_book(bcode)
        return jsonify({"message": f"Book with bcode '{bcode}' deleted successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/issues', methods=['POST'])
def issue_book_api():
    data = request.json
    name = data.get('name')
    reg_No = data.get('reg_No')
    bcode = data.get('bcode')
    contact = data.get('contact')
    email = data.get('email')
    issued_date = data.get('issued_date')
    issued_at = data.get('issued_at')

    try:
        issue_book(name, reg_No, bcode, contact, email, issued_date, issued_at)
        return jsonify({"message": f"Book with bcode '{bcode}' issued to '{name}' successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/issues/<int:issue_id>', methods=['PUT'])
def update_issue_api(issue_id):
    data = request.json
    new_contact = data.get('contact')
    new_email = data.get('email')
    new_issued_date = data.get('issued_date')
    new_issued_at = data.get('issued_at')

    try:
        issue_update(issue_id, new_contact, new_email, new_issued_date, new_issued_at)
        return jsonify({"message": f"Issue record with issue_id '{issue_id}' updated successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/issues/<int:issue_id>', methods=['DELETE'])
def delete_issue_api(issue_id):
    try:
        delete_issue_record(issue_id)
        return jsonify({"message": f"Issue record with issue_id '{issue_id}' deleted successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books', methods=['GET'])
def view_books_api():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            
            # Fetch column names to use as dictionary keys
            column_names = [desc[0] for desc in cursor.description]
            
            # Convert fetched data to a list of dictionaries
            books = []
            for row in rows:
                book = dict(zip(column_names, row))
                books.append(book)
            
            cursor.close()
            conn.close()
            
            # Return the list of dictionaries as a JSON response
            return jsonify(books)
        except Error as e:
            print(f"SQL Error: {e}")
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Failed to connect to the database."}), 500
    

@app.route('/issues', methods=['GET'])
def view_issues_api():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM issues")
            issues = cursor.fetchall()
            cursor.close()
            conn.close()

            # Assuming your issues table has columns named: id, name, reg_No, bcode, contact, email, issued_date, issued_at
            issues_list = []
            for issue in issues:
                issue_dict = {
                    "id": issue[0],
                    "name": issue[1],
                    "reg_No": issue[2],
                    "bcode": issue[3],
                    "contact": issue[4],
                    "email": issue[5],
                    "issued_date": issue[6].strftime('%Y-%m-%d'),  # Convert date to string
                    "issued_at": issue[7].strftime('%Y-%m-%d')  # Convert date to string
                }
                issues_list.append(issue_dict)

            return jsonify(issues_list), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Failed to connect to the database."}), 500

@app.route('/submissions', methods=['POST'])
def submit_book_api():
    data = request.json
    name = data.get('name')
    reg_No = data.get('reg_No')
    bcode = data.get('bcode')
    submit_date = data.get('submit_date')

    try:
        submit_book(name, reg_No, bcode, submit_date)
        return jsonify({"message": f"Book with bcode '{bcode}' submitted by '{name}' successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/submissions', methods=['GET'])
def view_submissions_api():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM submit_book")
            submissions = cursor.fetchall()
            cursor.close()
            conn.close()
            return jsonify(submissions)
        except Error as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Failed to connect to the database."}), 500

if __name__ == "__main__":
    app.run(debug=True)
