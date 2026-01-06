import json

def load_data():
    try:
        with open("youtube.txt", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def list_all_videos(videos):
        print("\n")
        print("*"*70)
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']}, Duration: {video['time']}")
        print("*"*70)

def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the time duration: ")
    videos.append({'name': name, 'time': time})
    auto_save(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the video name: ")
        time = input("Enter the time duration: ")
        videos[index-1] = {'name':name, 'time':time}
        auto_save(videos)
    else:
        print("Enter the valid index number")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        auto_save(videos)
    else:
        print("Enter the valid index!!")


def auto_save(videos):
    with open("youtube.txt", "w") as f:
        json.dump(videos, f)


def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager | choose an option")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")

        option = int(input("Enter your choice: "))

        match option:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid choise")

if __name__ == "__main__":
    main()