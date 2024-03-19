from canvasapi import Canvas
from datetime import datetime

# Canvas API URL and API key
API_URL = "https://canvas.illinois.edu"
API_KEY = "14559~DCtQVi6rrMLxGl55yELjUKZMRF7YvGtIY6XJk0jHJ5KWR9Vuud1vSWu27UDD1fmR"

# Initialize Canvas object
canvas = Canvas(API_URL, API_KEY)

def get_user_assignments(user_id):
    try:
        # Get user by Canvas ID
        user = canvas.get_user(user_id)
        
        # Retrieve all courses for the user
        courses = user.get_courses()
        
        # Dictionary to store assignments grouped by due date
        assignments_by_date = {}
        
        # Iterate through courses
        for course in courses:
            # Retrieve assignments for the course
            assignments = course.get_assignments()
            # Iterate through assignments
            for assignment in assignments:
                # Check if the assignment has a due date
                if assignment.due_at:
                    # Parse the due date into a datetime object
                    due_date = datetime.strptime(assignment.due_at, '%Y-%m-%dT%H:%M:%SZ')
                    # Add the assignment to the dictionary, grouped by due date
                    if due_date in assignments_by_date:
                        assignments_by_date[due_date].append((assignment, course.name))
                    else:
                        assignments_by_date[due_date] = [(assignment, course.name)]
        
        # Sort the assignments by due date
        sorted_assignments = sorted(assignments_by_date.items())
        
        # Output the assignments in the order of their due dates
        for due_date, assignments in sorted_assignments:
            print("Due Date:", due_date.strftime('%Y-%m-%d %H:%M:%S'))
            for assignment, course_name in assignments:
                print("Course:", course_name)
                print("Assignment:", assignment.name)
                print()
    except Exception as e:
        print("Error:", e)

# Replace 1 with the actual Canvas ID of the user you want to retrieve assignments for
user_id = 1

# Call the function to retrieve and output user assignments
get_user_assignments(user_id)