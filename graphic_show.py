# Youtube link: https://youtu.be/PsP9Tgq1WbQ

# we were not able to create a webpage/deploy the code so build a GUI which works on our laptop
# So we will be uploading a video of how GUI works 

import sqlite3
import tkinter as tk
from moviepy.editor import VideoFileClip

root = tk.Tk()
root.title("Video Player")

found_videos = []  # Declare found_videos as a global variable

# Function to search videos
def search_videos():
    global found_videos  
    keywords = entry.get().split()  
    placeholders = ' OR '.join(['description LIKE ?' for _ in range(len(keywords))]) 
    query = "SELECT * FROM videos WHERE " + placeholders
    c.execute(query, ['%' + keyword + '%' for keyword in keywords])
    found_videos = c.fetchall()
    update_result_list(found_videos)


# Function to update the listbox with found videos (showing only names)
def update_result_list(videos):
    result_listbox.delete(0, tk.END)
    for video in videos:
        result_listbox.insert(tk.END, video[1])  # Display only the video name 

# Function to play selected video
def play_video():
    selected_index = result_listbox.curselection()
    if selected_index:
        selected_video = found_videos[selected_index[0]]
        video_path = selected_video[3]  
        clip = VideoFileClip(video_path)
        clip.preview()

# Create a connection to the database
conn = sqlite3.connect('videos.db')
c = conn.cursor()

# Create a GUI window
root.title("Video Search")

# Search bar
search_label = tk.Label(root, text="Enter keywords:")
search_label.pack()
entry = tk.Entry(root)
entry.pack()

# Search button
search_button = tk.Button(root, text="Search", command=search_videos)
search_button.pack()

# Display search results in a listbox
result_listbox = tk.Listbox(root, width=50, height=10)
result_listbox.pack()

# Play button
play_button = tk.Button(root, text="Play Video", command=play_video)
play_button.pack()

root.mainloop()
conn.close()
