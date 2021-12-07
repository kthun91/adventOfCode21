import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# slow
with open(abs_file_path, "r") as f:
    day = 0
    end = 80
    fish = f.readline()
    fish = list(map(int, fish.split(',')))
    print(fish)
    for d in range(0,end):
        day += 1 # debugging purpose
        for idx, elem in enumerate(fish[:len(fish)]):
            fish[idx] = elem - 1
            if fish[idx] == -1:
                fish[idx] = 6
                fish.append(8)
    print(f"day: {day} : {fish}")
    print(len(fish))