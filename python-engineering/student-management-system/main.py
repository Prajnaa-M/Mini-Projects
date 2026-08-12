from pathlib import Path 
import json
df=Path("students.json")   

def load_students():
    content=df.read_text()        #path.read_text gives u a string
    return(json.loads(content))    #reads json from a string

def save_students(students):
    js=json.dumps(students)       #writes as a json string
    df.write_text(js)


def main():
    students=load_students()
    print("1. Add student\n2. View students\n3. Exit")
    num=int(input("Enter your choice"))
    if num==1:
        student={}
        student["name"]=input("enter name: ")
        student["age"]=int(input("enter age: "))
        student["course"]=input("enter course: ")
        students.append(student)
        save_students(students)
    elif num==2:
        print(students)
    else:
        print('goodbye')

main()


