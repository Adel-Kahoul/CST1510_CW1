def is_valid_id(student_id):
    return (
        student_id.startswith("M00")
        and len(student_id) == 9
        and student_id[3:].isdigit()
    )


student_ids = ["M00123456", "M0012345", "X00123456", "M00ABCDEF", "M00987654"]

for sid in student_ids:
    print(f"{sid}: {is_valid_id(sid)}")