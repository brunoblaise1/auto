# infinite_write.py

# Code that will be written repeatedly to the output file
code_to_write = '''import random
import string
import time

# Helper function to generate random strings
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# User class to manage user data
class User:
    def __init__(self, username, email, age, activities=None):
        self.username = username
        self.email = email
        self.age = age
        self.activities = activities if activities else []

    def add_activity(self, activity):
        self.activities.append(activity)
    
    def get_activity_summary(self):
        return f"{self.username} has participated in {len(self.activities)} activities."

    def __str__(self):
        return f"User({self.username}, {self.email}, {self.age})"

# Activity class to track user activities
class Activity:
    def __init__(self, name, description, date):
        self.name = name
        self.description = description
        self.date = date
    
    def __str__(self):
        return f"Activity({self.name}, {self.description}, {self.date})"

# Database simulation: Storing users and their activities
class Database:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user):
        if user.username not in self.users:
            self.users[user.username] = user
            print(f"User {user.username} added to the database.")
        else:
            print(f"User {user.username} already exists.")

    def get_user(self, username):
        return self.users.get(username, None)

    def list_users(self):
        return [str(user) for user in self.users.values()]

# Generate random activities
def generate_random_activity():
    activities = ['Running', 'Swimming', 'Reading', 'Cooking', 'Hiking', 'Cycling']
    descriptions = ['A fun outdoor activity.', 'A relaxing indoor activity.', 'A group sport activity.', 
                    'A personal hobby.', 'An adventurous outdoor activity.', 'A health-conscious activity.']
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    
    name = random.choice(activities)
    description = random.choice(descriptions)
    
    return Activity(name, description, date)

# Function to simulate an activity being logged by a user
def simulate_user_activity(database, username):
    user = database.get_user(username)
    if user:
        activity = generate_random_activity()
        user.add_activity(activity)
        print(f"Logged activity for {username}: {activity}")
    else:
        print(f"User {username} not found in the database.")

# Simulate reading and writing data to a file
def save_to_file(database, filename="user_data.txt"):
    with open(filename, "w") as file:
        for user in database.users.values():
            file.write(f"{user.username},{user.email},{user.age}\n")
            for activity in user.activities:
                file.write(f"\t{activity.name},{activity.description},{activity.date}\n")
    print(f"Data saved to {filename}.")

def load_from_file(filename="user_data.txt"):
    database = Database()
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            current_user = None
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("\t"):
                    # Activity line
                    if current_user:
                        parts = line[1:].split(",")
                        activity = Activity(parts[0], parts[1], parts[2])
                        current_user.add_activity(activity)
                else:
                    # User line
                    parts = line.split(",")
                    username = parts[0]
                    email = parts[1]
                    age = int(parts[2])
                    current_user = User(username, email, age)
                    database.add_user(current_user)
    except FileNotFoundError:
        print(f"No existing data file found. Starting fresh.")
    return database

# Main function to run the simulation
def main():
    db = Database()

    # Simulate adding users to the database
    for _ in range(10):
        username = generate_random_string(10)
        email = generate_random_string(5) + "@example.com"
        age = random.randint(18, 65)
        user = User(username, email, age)
        db.add_user(user)
    
    # Simulate logging activities for each user
    for _ in range(50):  # Simulate 50 activities
        random_username = random.choice(list(db.users.keys()))
        simulate_user_activity(db, random_username)
    
    # Display the users and their activities
    print("\nUser Database Summary:")
    for user in db.users.values():
        print(f"{user.get_activity_summary()}")

    # Save the data to a file
    save_to_file(db)

    # Load the data from the file and print it again
    print("\nLoading data from file:")
    db_from_file = load_from_file()
    for user in db_from_file.users.values():
        print(f"{user.username}: {len(user.activities)} activities")

if __name__ == "__main__":
    main()

'''

# Specify the file name where the code will be written
output_file = 'infinite_generated_code.py'

# Open the file in append mode and write the code in an infinite loop
while True:
    with open(output_file, 'a') as file:  # 'a' mode for appending
        file.write(code_to_write)
    print(f"Code written to {output_file}... (Press CTRL+C to stop)")
