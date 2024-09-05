import tkinter as tk
import pyperclip
import pyshorteners




def shorten_url():
     long_url=entry_long_url.get()
     s = pyshorteners. Shortener()
     short_url=s.tinyurl.short(long_url) 
     entry_short_url.delete(0,tk.END)
     entry_short_url.insert(tk. END, short_url)
     pyperclip.copy(short_url)

root = tk.Tk()
root.title("URL Shortener")

label_long_url = tk.Label(root, text="Long URL:") 
label_long_url.grid(row=0, column=0, padx=10, pady=10)
label_short_url = tk.Label(root, text="Short URL:")
label_short_url.grid(row=1, column=0, padx=18, pady=10)

entry_long_url=tk.Entry(root, width=40)
entry_long_url.grid(row=0, column=1, padx=10, pady=10)
entry_short_url= tk.Entry(root, width=48) 
entry_short_url.grid(row=1, column=1, padx=10, pady=10)

btn_shorten = tk.Button(root, text="Shorten", command=shorten_url) 
btn_shorten.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()