import re

val = "01063667963"

# pattern = "^01[016789][1-9]\\d{6,7}$"
        # "^01[016789]\\d{7,8}을 안하는 이유는 0~9까지 숫자가 나오기떄문
pattern = r"^01[016789][1-9]\d{6,7}$" # raw

if re.match(pattern, val):
    print("matched")
else:
    print("invalid")
