def add numbers@:
total = 0.0
print("Enter numbers to add. Type "done' when you?ne finished. *)

while True:
= input (Number (or 'done'): *).strip()
if entry. lower () -- "done":
break

try:

total += float(entry)
except ValueError:
print("T
continue
That wasn't a valid number-try again.")
continue
print(fAnThe sum of your numbers is: (total)")
Cancel
Commit changes
if name --*_main*:
add numbers ()
