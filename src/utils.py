import json
from random import random, seed
from tabulate import tabulate

def get_random_number():
    seed()
    return random()

def print_msg(msg):
    if isinstance(msg, dict):
        msg = json.dumps(msg, indent=2)

    print("\n" + "*" * 50)
    print(msg)
    print("*" * 50)

def print_data(data):
    print_msg("INPUT DATA INFORMATION")
    
    # Available departments
    print_msg("Available departments")
    for dept in data.depts:
        courses = ', '.join(str(course) for course in dept.courses)
        print(f"name: {dept.name}, courses: {courses}")

    # Available courses
    print_msg("Available courses")
    for course in data.courses:
        instructors = ', '.join(str(instr) for instr in course.instructors)
        print(f"Course no.: {course.number}, Name: {course.name}, Max no. of students: {course.max_number_of_students}, Instructors: {instructors}")

    # Available rooms
    print_msg("Available rooms")
    for room in data.rooms:
        print(f"Room No: {room.number}, Max seating capacity: {room.seating_capacity}")

    # Available instructors
    print_msg("Available instructors")
    for instructor in data.instructors:
        print(f"ID: {instructor.id}, Name: {instructor.name}")

    # Available meeting times
    print_msg("Available meeting times")
    for meeting_time in data.meeting_times:
        print(f"ID: {meeting_time.id}, Meeting Time: {meeting_time.time}")

def print_population_schedules(population, generation_number):
    print_msg(f"Generation Number: {generation_number}")

    schedules = [
        [
            idx,
            str(schedule),
            schedule.fitness,
            schedule.number_of_conflicts
        ]
        for idx, schedule in enumerate(population.schedules)
    ]

    headers = ["Schedule #", "Classes [dept, class, room, instructor, meeting-time]", "Fitness", "Conflicts"]
    print(tabulate(schedules, headers=headers))

def print_schedule_as_table(data, schedule, generation):
    table_data = []
    headers = ["Class #", "Dept", "Course (number, max # of students)", "Room (capacity)", "Instructor (Id)", "Meeting Time"]

    for class_num, _class in enumerate(schedule.classes, start=1):
        major_idx = next(idx for idx, dept in enumerate(data.depts) if dept.name == _class.department.name)
        course_idx = next(idx for idx, course in enumerate(data.courses) if course.name == _class.course.name)
        room_idx = next(idx for idx, room in enumerate(data.rooms) if room.number == _class.room.number)
        instructor_idx = next(idx for idx, instructor in enumerate(data.instructors) if instructor.id == _class.instructor.id)
        meeting_time_idx = next(idx for idx, meeting_time in enumerate(data.meeting_times) if meeting_time.id == _class.meeting_time.id)

        table_data.append([
            class_num,
            data.depts[major_idx].name,
            f"{data.courses[course_idx].name} ({data.courses[course_idx].number}, {data.courses[course_idx].max_number_of_students})",
            f"{data.rooms[room_idx].number} ({_class.room.seating_capacity})",
            f"{data.instructors[instructor_idx].name} ({data.instructors[instructor_idx].id})",
            f"{data.meeting_times[meeting_time_idx].time} ({data.meeting_times[meeting_time_idx].id})"
        ])

    print(tabulate(table_data, headers=headers))

    if schedule.fitness == 1.0:
        print_msg(f"Solution Found in {generation + 1} generations")
