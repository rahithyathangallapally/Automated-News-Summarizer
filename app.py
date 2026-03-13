import tkinter as tk
from tkinter import messagebox, scrolledtext

# Safe imports
try:
    from news_fetcher import fetch_news
    from summarizer import summarize_text
except Exception as e:
    print("IMPORT ERROR:", e)
    fetch_news = None
    summarize_text = None

def generate_summary():
    if not fetch_news or not summarize_text:
        messagebox.showerror(
            "Error",
            "Backend modules failed to load.\nCheck terminal for details."
        )
        return

    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a news article URL")
        return

    try:
        status_label.config(text="Fetching article...")
        window.update()

        article_text = fetch_news(url)

        if not article_text or len(article_text) < 200:
            output_box.delete("1.0", tk.END)
            output_box.insert(
                tk.END,
                "❌ Article extraction failed or site not supported."
            )
            status_label.config(text="Failed ❌")
            return

        status_label.config(text="Summarizing...")
        window.update()

        summary = summarize_text(article_text)

        if not summary or len(summary.strip()) < 50:
            output_box.delete("1.0", tk.END)
            output_box.insert(
                tk.END,
                "⚠ Article extracted but summarization works only for English articles."
            )
            status_label.config(text="Language not supported ⚠")
            return

        # Display summary
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, summary)
        status_label.config(text="Done ✅")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="")

# ---------------- GUI ----------------
window = tk.Tk()
window.title("Automated News Summarizer AI")
window.geometry("800x600")

tk.Label(window, text="📰 Automated News Summarizer AI",
         font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(window, text="Enter News Article URL:").pack()

url_entry = tk.Entry(window, width=80)
url_entry.pack(pady=5)

tk.Button(window, text="Generate Summary",
          command=generate_summary,
          bg="blue", fg="white",
          font=("Arial", 12)).pack(pady=10)

output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD,
                                      width=90, height=20)
output_box.pack(pady=10)

status_label = tk.Label(window, text="", fg="green")
status_label.pack()

window.mainloop()
