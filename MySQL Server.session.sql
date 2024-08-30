cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                bname VARCHAR(100) NOT NULL,
                bcode VARCHAR(100) NOT NULL ,
                total INT NOT NULL,
                subject VARCHAR(255) NOT NULL
            );
            """);
INSERT INTO books (bname, bcode,subject,total) VALUES
('Clean Code', 'B004', 'Software Engineering', 4),
('The Pragmatic Programmer', 'B005', 'Software Engineering' , 6),
('Design Patterns: Elements of Reusable Object-Oriented Software', 'B006', 'Software Engineering',2),
('Introduction to Algorithms', 'B007', 'Computer Science', 8),
('Artificial Intelligence: A Modern Approach', 'B008', 'Artificial Intelligence', 5),
('JavaScript: The Good Parts', 'B009', 'Web Development' , 7),
('You Don\'t Know JS', 'B010', 'Web Development', 10),
('Effective Java', 'B011', 'Programming', 3),
('Head First Design Patterns', 'B012', 'Software Engineering', 6),
('Deep Learning with Python', 'B013', 'Artificial Intelligence' , 4);
            
select * from books;

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
            """);
INSERT INTO issues (name, reg_No, bcode, contact, email, issued_date, issued_at) VALUES
('Alice Johnson', 'REG003', 'B006', '345-678-9012', 'alice.johnson@example.com', '2024-08-03', '2024-08-03'),
('Bob Brown', 'REG004', 'B007', '456-789-0123', 'bob.brown@example.com', '2024-08-04', '2024-08-04'),
('Charlie Davis', 'REG005', 'B008', '567-890-1234', 'charlie.davis@example.com', '2024-08-05', '2024-08-05'),
('Eve Miller', 'REG006', 'B009', '678-901-2345', 'eve.miller@example.com', '2024-08-06', '2024-08-06'),
('Frank Wilson', 'REG007', 'B010', '789-012-3456', 'frank.wilson@example.com', '2024-08-07', '2024-08-07'),
('Grace Lee', 'REG008', 'B011', '890-123-4567', 'grace.lee@example.com', '2024-08-08', '2024-08-08'),
('Hannah White', 'REG009', 'B012', '901-234-5678', 'hannah.white@example.com', '2024-08-09', '2024-08-09'),
('Isaac Green', 'REG010', 'B013', '012-345-6789', 'isaac.green@example.com', '2024-08-10', '2024-08-10');

select * from issues;


cursor.execute("""
            CREATE TABLE IF NOT EXISTS submit_book (
                submit_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                reg_No VARCHAR(100) NOT NULL,
                bcode VARCHAR(100) NOT NULL,
                submit_date DATE NOT NULL,
                
            );
            """);

INSERT INTO submit_book (name, reg_No, bcode, submit_date) VALUES
('Alice Johnson', 'REG003', 'B006', '2024-08-17'),
('Bob Brown', 'REG004', 'B007', '2024-08-18'),
('Charlie Davis', 'REG005', 'B008', '2024-08-19'),
('Eve Miller', 'REG006', 'B009', '2024-08-20'),
('Frank Wilson', 'REG007', 'B010', '2024-08-21'),
('Grace Lee', 'REG008', 'B011', '2024-08-22'),
('Hannah White', 'REG009', 'B012', '2024-08-23'),
('Isaac Green', 'REG010', 'B013', '2024-08-24');

select * from submit_book;