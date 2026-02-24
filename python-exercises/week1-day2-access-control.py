# Mini Exercise: Access Control

age = 19
is_student = True
has_coupon = False
has_invite = True

if age >= 18 and (is_student or has_coupon or has_invite):
    print("Access granted to special event")
else:
    print("Access denied")
#ans::Access granted to special event
#if its age 16, it'll print :: Access denied

age = 19
is_student = False
has_coupon = False
has_invite = True
if age >= 18 and (is_student or has_coupon or has_invite):
    print("Access granted to special event")
else:
    print("Access denied")
#prints Access granted to special event