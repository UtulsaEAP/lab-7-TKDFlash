"""
Sean Killian
Thursday @ 2pm
"""

def wordInRange():
    #Type your code here
    file_path = input().strip()
    lower_bound = input().strip()
    upper_bound = input().strip()

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        word = line.strip()
        if lower_bound <= word <= upper_bound:
            print(f"{word} - in range")
        else:
            print(f"{word} - not in range")

if __name__ == '__main__':
    wordInRange()