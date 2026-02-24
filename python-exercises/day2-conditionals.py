name = "Glory"
age = 21

if age >= 18:
    print(name + " is an adult")
else:
    print(name + " is not an adult")

#if conditionals and and/or
#AND
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter")
else:
    print("Access denied")

#ans:: you can enter

#or
is_student = True
has_coupon = False

if is_student or has_coupon:
    print("Discount applied")
else:
    print("No discount")

#ans::  discount applied

#trial
age = 20
is_student = False
has_coupon = True

if age > 18 and (is_student or has_coupon):
    print("Special access")
else:
    print("Normal access")
#special access