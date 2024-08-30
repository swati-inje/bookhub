# from Connection_db import create_connection
import mysql.connector
from mysql.connector import Error
from datetime import datetime


def create_connection():
    """
    Creates and returns a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='suraj',
            database='library_sys_db'
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Function to connect to the database
def create_tables():
    """
    Creates the tables in the MySQL database.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            #Drop the existing table if it exists
            # cursor.execute("DROP TABLE IF EXISTS books;")
            
            # Create books table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                bname VARCHAR(100) NOT NULL,
                bcode VARCHAR(100) NOT NULL ,
                total INT NOT NULL,
                subject VARCHAR(255) NOT NULL
            );
            """)
            print("Books table created successfully.")
            
            # Create issues table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS issues (
                issue_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                reg_No VARCHAR(100) NOT NULL,
                bcode VARCHAR(100) NOT NULL,
                contact VARCHAR(20),
                email VARCHAR(255),
                issued_date DATE NOT NULL,
                issued_at DATE NOT NULL,
                
            );
            """)
            print("Issues table created successfully.")
            
            #Create submit_book table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS submit_book (
                submit_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                reg_No VARCHAR(100) NOT NULL,
                bcode VARCHAR(100) NOT NULL,
                submit_date DATE NOT NULL,
                
            );
            """)
            print("Submit Book table created successfully.")
            
            connection.commit()
        except Error as e:
            print(f"Error while creating tables: {e}")
        finally:
            cursor.close()
            connection.close()
# Function to add a book
# Function to add a book
def add_book(bname, bcode, total, subject):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO books (bname, bcode, total, subject) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (bname, bcode, total, subject))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Book '{bname}' added successfully.")
    else:
        print("Failed to connect to the database.")
# Function to update/edit a book
def book_update(bcode, new_bname=None, new_total=None, new_subject=None):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "UPDATE books SET bname = %s, total = %s, subject = %s WHERE bcode = %s"
            cursor.execute(query, (new_bname, new_total, new_subject, bcode))
            conn.commit()
            print(f"Book with bcode '{bcode}' updated successfully.")
        except Error as e:
            print(f"Error while updating book: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")

# Function to delete a book
def delete_book(bcode):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM books WHERE bcode = %s"
            cursor.execute(query, (bcode,))
            conn.commit()
            print(f"Book with bcode '{bcode}' deleted successfully.")
        except Error as e:
            print(f"Error while deleting book: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")

# Function to issue a book
def issue_book(name, reg_No, bcode, contact, email, issued_date, issued_at):
    try:
        # Convert dates from 'DD-MM-YYYY' to 'YYYY-MM-DD'
        issued_date = datetime.strptime(issued_date, '%d-%m-%Y').strftime('%Y-%m-%d')
        issued_at = datetime.strptime(issued_at, '%d-%m-%Y').strftime('%Y-%m-%d')
    except ValueError as e:
        print(f"Error in date format: {e}")
        return

    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO issues 
                (name, reg_No, bcode, contact, email, issued_date, issued_at) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, reg_No, bcode, contact, email, issued_date, issued_at))
            conn.commit()
            print(f"Book with bcode '{bcode}' issued to '{name}' successfully.")
        except Error as e:
            print(f"Error while issuing book: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")
# Function to update/edit an issue record
def issue_update(issue_id, new_contact=None, new_email=None, new_issued_date=None, new_issued_at=None):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            UPDATE issues
            SET contact = %s, email = %s, issued_date = %s, issued_at = %s
            WHERE issue_id = %s
            """
            cursor.execute(query, (new_contact, new_email, new_issued_date, new_issued_at, issue_id))
            conn.commit()
            print(f"Issue record with issue_id '{issue_id}' updated successfully.")
        except Error as e:
            print(f"Error while updating issue record: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")

# Function to delete an issue record
def delete_issue_record(issue_id):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM issues WHERE issue_id = %s"
            cursor.execute(query, (issue_id,))
            conn.commit()
            print(f"Issue record with issue_id '{issue_id}' deleted successfully.")
        except Error as e:
            print(f"Error while deleting issue record: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")

# Function to view all books
def view_books():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            for book in books:
                print(book)
        except Error as e:
            print(f"Error while retrieving books: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")

# Function to view all issue records
def view_issue_records():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM issues")
            issues = cursor.fetchall()
            if issues:
                for issue in issues:
                    print(issue)
            else:
                print("No issues found.")
        except Error as e:
            print(f"Error while retrieving issue records: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")
# Function to submit a book
def submit_book(name, reg_No, bcode, submit_date):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO submit_book (name, reg_No, bcode, submit_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, reg_No, bcode, submit_date))
            conn.commit()
            print(f"Book with bcode '{bcode}' submitted by '{name}' successfully.")
        except Error as e:
            print(f"Error while submitting book: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")

# Function to view all submission records
def view_submission_records():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM submit_book")
            submissions = cursor.fetchall()
            for submission in submissions:
                print(submission)
        except Error as e:
            print(f"Error while retrieving submission records: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")

def main():
    while True:
        print("\n-----------------------------------------------------------------------------")
        print("\nLibrary Management System")
        print("1. Add a New Book")
        print("2. Book Update/Edit")
        print("3. Book Delete")
        print("4. Issue New Book")
        print("5. Issue Update/Edit")
        print("6. Delete Issue Book Record")
        print("7. View All Book List")
        print("8. View All Issue Book Record")
        print("9. Submit Books")
        print("10. View Submission Records")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bname = input("Enter book name: ")
            bcode = input("Enter book code: ")
            total = int(input("Enter total number of copies: "))
            subject = input("Enter subject: ")
            add_book(bname, bcode, total, subject)
        elif choice == '2':
            bcode = input("Enter book code to update: ")
            new_bname = input("Enter new book name (press Enter to skip): ") or None
            new_total = input("Enter new total number of copies (press Enter to skip): ")
            new_total = int(new_total) if new_total else None
            new_subject = input("Enter new subject (press Enter to skip): ") or None
            book_update(bcode, new_bname, new_total, new_subject)
        elif choice == '3':
            bcode = input("Enter book code to delete: ")
            delete_book(bcode)
        elif choice == '4':
            name = input("Enter name of the person: ")
            reg_No = input("Enter registration number: ")
            bcode = input("Enter book code: ")
            contact = input("Enter contact number: ")
            email = input("Enter email address: ")
            issued_date = input("Enter issued date (DD-MM-YYYY): ")
            issued_at = input("Enter issued at date (DD-MM-YYYY): ")
            issue_book(name, reg_No, bcode, contact, email, issued_date, issued_at)
        elif choice == '5':
            issue_id = int(input("Enter issue ID to update: "))
            new_contact = input("Enter new contact number (press Enter to skip): ") or None
            new_email = input("Enter new email address (press Enter to skip): ") or None
            new_issued_date = input("Enter new issued date (DD-MM-YYYY, press Enter to skip): ") or None
            new_issued_at = input("Enter new issued at date (DD-MM-YYYY, press Enter to skip): ") or None
            issue_update(issue_id, new_contact, new_email, new_issued_date, new_issued_at)
        elif choice == '6':
            issue_id = int(input("Enter issue ID to delete: "))
            delete_issue_record(issue_id)
        elif choice == '7':
            view_books()
        elif choice == '8':
            view_issue_records()
        elif choice == '9':
            name = input("Enter name of the person: ")
            reg_No = input("Enter registration number: ")
            bcode = input("Enter book code: ")
            submit_date = input("Enter submit date (DD-MM-YYYY): ")
            submit_book(name, reg_No, bcode, submit_date)
        elif choice == '10':
            view_submission_records()
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()