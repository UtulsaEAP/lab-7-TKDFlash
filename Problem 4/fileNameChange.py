"""
Sean Killian
Thursday @ 2pm
"""

def fileNameChange():
    #type your code here
    file_path = input().strip()

    with open(file_path,"r") as f:
        for line in f:
            modified_flename = line.strip().replace('_photo.jpg', '_info.txt')
            print(modified_flename)
    return

if __name__ == '__main__':
    fileNameChange()


    