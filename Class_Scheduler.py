
import random

subjects = ["Maths", " biology", "Physics", "Chemistry", "English", "Geography", "History", "Hindi"]# subjects excluding lunch.
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#Time slots
time = ["9am-9:45am", "10am-10:45am", "11am-11:45am", "12pm-12:45pm", "1pm-1:45pm", "2pm-2:45pm", "3pm-3:45pm"]

# Function to add a new subject
def add_subject(name):
    if name not in subjects:
        subjects.append(name)

#counter to balance 6 subjects a week
subject_counter = {sub: 0 for sub in subjects}

max_classes = 4 #each subjects appears 3-4 times a week.

time_table = {}

for day in days:
    chosen = []
    while len(chosen) < 6:
        subject = random.choice(subjects)

        # condition
        #1. No duplicate in a same day
        #2. Subject count < max_classes
        if subject not in chosen and subject_counter[subject] < max_classes:
            chosen.append(subject)
            subject_counter[subject] += 1
    # insert lunch at 4th period
    chosen.insert(3, "Lunch")
    
    time_table[day] = chosen

#print time table
for day in days:
    print(f"\n{day}:")
    for i in range(len(time)):
        print(f"{time[i]}: {time_table[day][i]}")
    


    




    



