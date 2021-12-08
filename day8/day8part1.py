import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# get digits
# check len of each digit
with open(abs_file_path, "r") as f:
    digits = list()
    counter = 0
    for line in f.readlines():
        nine, four = line.split("|")
        digits = four.split()
        for dig in digits:
            if len(dig) in [2, 4, 3, 7]:
                counter += 1
    print(counter)

        