# FILE-INTEGRITY-CHECKER
"COMPANY" : CODTECH IT SOLUTIONS

"NAME" : SAYAN PANIGRAHI

"INTERN ID" : CT04DR1763

"DOMAIN" : CYBER SECURITY AND ETHICAL HACKING

"DURATION" : 4 WEEKS

"MENTOR" : NEELA SANTOSH

"DESCRIBED ABOUT THE TASK"

This project focuses on developing a File Integrity Monitoring (FIM) System using Python to track changes in files within a specified directory. As data security becomes increasingly important, detecting unauthorized or accidental modifications to files is essential. This system uses cryptographic hash functions to ensure the integrity of files and identify any changes in real time.

The tool works by generating a unique hash value for every file in the target folder using the SHA-256 hashing algorithm. A hash serves as a digital fingerprint of the file’s content. If a file is altered in any way—even by a single character—the resulting hash will be completely different. This makes hashing a reliable method for detecting modifications.

At startup, the system performs an initial scan of the folder and records each file’s hash value. It then enters a continuous monitoring loop, scanning the folder at regular intervals. During each scan, the program compares the current hash of each file with the previously stored hash values. Based on this comparison, the system can detect three major events:

1.New File Added: When a file appears that did not exist during the previous scan.

2.Deleted File: When a file present earlier cannot be found in the current scan.

3.Modified File: When an existing file’s hash value does not match the previously stored hash, indicating changes in its content.

Whenever such events occur, the program immediately prints a message to alert the user. This real-time feedback allows users to track all file activities inside a sensitive folder, helping detect suspicious behavior or unintentional changes.

The project is built using standard Python libraries such as os, time, and hashlib, making it lightweight and easily portable. The SHA-256 hashing function from the hashlib module ensures high security and accuracy in monitoring changes. The system does not require any external dependencies and can run on any machine with Python installed.

This File Integrity Monitoring System has several practical applications. It can be used to safeguard important documents, monitor shared file directories, track changes in system configuration files, and help detect malware or unauthorized user activity. It is especially useful in cybersecurity environments where data integrity and access monitoring are crucial.

In conclusion, the project successfully demonstrates how hashing and directory scanning techniques can be combined in Python to create a functional file integrity monitoring tool. The system is simple, efficient, and effective for real-time change detection. It can also be expanded with additional features such as logging, GUI interface, or email notifications. Overall, this project provides a strong foundation for understanding file integrity, hashing algorithms, and security monitoring concepts.
