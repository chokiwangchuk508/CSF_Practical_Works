from cmath import e


name = " Choki Wangchuk"
Age = 19
height = 1.77
is_student = True

person_info = {
    "name": name,
    "age": Age,
    "height": height,
    "is_student": is_student
}
print(person_info)

person_info["favourite_color"] = "Red"
print(person_info)

print(person_info["weight"])
print(f"Error: {e}")



