from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd
from googleapiclient.discovery import build


class Parent:
    def __init__(self): 
        window = Tk()

        def scrape_comments():
            try:
                url = txtfld_url.get()
                url_i = url.split('?v=')
                url_id = url_i[1].split('&list=')
            except:
                messagebox.showinfo("showinfo", "Error in URL format")
                return

            api_key = 'ENTER YOUR YOUTUBR API'  #enter youtube api
            youtube = build('youtube', 'v3', developerKey=api_key)
            ID = url_id[0] 

            box = [['Name', 'Comment']]

            def scrape_comments_with_replies():
                try:
                    data = youtube.commentThreads().list(part='snippet', videoId=ID, maxResults='100', textFormat="plainText").execute()
                    
                    for i in data["items"]:
                        name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
                        comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
                        box.append([name, comment])
                        
                    while "nextPageToken" in data:
                        data = youtube.commentThreads().list(part='snippet', videoId=ID, pageToken=data["nextPageToken"], maxResults='100', textFormat="plainText").execute()
                        
                        for i in data["items"]:
                            name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
                            comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
                            box.append([name, comment])

                    df = pd.DataFrame(box[1:], columns=box[0])  # Use only comment data
                    title = 'comments.csv'
                    df.to_csv(title, index=False, header=True)
                    messagebox.showinfo("showinfo", "Comments Scrapped Successfully! Saved to comments.csv")
                except:
                    messagebox.showinfo("showinfo", "Invalid URL or error in scraping comments")

            scrape_comments_with_replies()

        window.title('YouTube Comment Scraper by team AI FORGE (under development)')
        window.geometry("500x300")
        window.configure(bg='#2E3B4E')  # Dark Navy Blue

        lbl = Label(window, text="Enter YouTube Video URL", fg='#333333', bg='#F7F7F7')  # Dark Gray text on        Light Gray
        lbl.pack(pady=10)

        txtfld_url = Entry(window, bd=0, width=40, bg='#FFFFFF', fg='#333333', highlightbackground='#C0C0C0',       highlightcolor='#007BFF')  # White background with Dark Gray text
        txtfld_url.pack(pady=5)
        
        btn_dwn = Button(window, text="Start Scraping", fg='#FFFFFF', bg='#007BFF', bd=0,       command=scrape_comments)  # White text on Bright Blue
        btn_dwn.pack(pady=20)


        window.mainloop()


if __name__ == "__main__":
    Parent()
