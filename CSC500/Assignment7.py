# Course Room Dictionary
course_room_dict = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

# Instructors Dictionary
instructors_dict = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

# Meeting Time Dictionary
meeting_time_dict = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

course_number = input("Enter a course number: ")

if course_number in course_room_dict:
    room_number = course_room_dict[course_number]
    instructor = instructors_dict[course_number]
    meeting_time = meeting_time_dict[course_number]

    print(f"Room Number: {room_number}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")
else:
    print("Course not found.")






