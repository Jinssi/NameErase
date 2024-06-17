Have you accidentally added names to an .xlsx sheet and need to delete one matching specific criteria? Here's some logic that implements removing male names from a column. The script goes through your file, marks the rows where names matching the list are, prints the rows into terminal, deletes the rows and saves a new file without those rows.

Git clone to your pc
Install pandas and openpyxl
Save a copy of your original file in same folder with the script
Edit the filename in the script to match yours
Run the script with python ./malenames.py
