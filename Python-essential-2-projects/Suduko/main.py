right_answer = "123456789"
final_result = True
user_answer = []
for i in range(9):
    user_input = input(f"Enter The {i+1} Row Answer: ")
    user_answer.append(user_input)


columns = []

for col in range(9):
    column = ""
    for row in range(9):
        column += user_answer[row][col]
    columns.append(column)

sub_squares = []

for row_start in range(0, 9, 3):
    for col_start in range(0, 9, 3):
        square = ""
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                square += user_answer[r][c]
        sub_squares.append(square)

for item in user_answer:
    sorted_s = ''.join(sorted(item))
    if sorted_s != right_answer:
        final_result = False

for item in columns:
    sorted_s = ''.join(sorted(item))
    if sorted_s != right_answer:
        final_result = False

for item in sub_squares:
    sorted_s = ''.join(sorted(item))
    if sorted_s != right_answer:
        final_result = False

if final_result:
    print("Yes")
else:
    print("No")
  
