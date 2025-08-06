# 📰 Tkinter News App

A simple GUI-based News Application built using Python's Tkinter library that fetches the latest top headlines from the **NewsAPI** and displays them with images, titles, and descriptions. Users can read full articles in a web browser and navigate through the news items using "Previous", "Read More", and "Next" buttons.

---

## 📌 Features

- Fetches real-time top headlines from [NewsAPI.org](https://newsapi.org/)
- Displays:
  - News image
  - News title
  - News description
- Navigation buttons:
  - Previous article
  - Read More (opens full article in browser)
  - Next article
- Default fallback image when no image is available
- Simple and clean layout using `Tkinter`

---

## 📦 Requirements

Install the following Python libraries before running the project:

```bash
pip install requests 
pip install pillow
```

## 🔑 API Key Setup
-This app uses NewsAPI to fetch headlines.

1. Create a free account at https://newsapi.org
2. Copy your API Key
3. Replace "yourAPIKEY" in the code with your actual key:

```python
self.data = requests.get(
    'https://newsapi.org/v2/top-headlines?country=us&apiKey=yourAPIKEY'
).json()
```
## 🚀 How to Run the Project
-Clone the repository or download the .py file.
-Ensure all requirements are installed.
-Run the script:

## 📁 File Structure
```bash
news_app/
│
├── app.py                       # Main Python file with GUI code
├── images-not-found.png         # Local fallback image for missing news images
└── README.md                    # Project documentation
```


## 🧠 Concepts Used
1. Python requests for API calls
2. PIL (Pillow) for image handling
3. io.BytesIO to handle raw image byte streams
4. urllib.request.urlopen to fetch image data
5. Tkinter for GUI development
6. webbrowser to open full articles
