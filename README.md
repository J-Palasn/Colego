# 🥑 Colego – AI Cover Letter Generator  

Colego is a **Streamlit-based AI-powered cover letter generator** that helps students, professionals, and job seekers create **personalized and professional cover letters** in seconds.  

With a clean interface, local storage support, and AI-driven generation, you can save time while tailoring your applications to specific job opportunities.  

---

## ✨ Features  

- 🎨 **User-Friendly Interface** – Built with **Streamlit**, offering a modern, responsive design.  
- 📑 **Personal & Job Information Forms** – Enter details such as your name, skills, job title, and job description.  
- 💾 **Local Storage Support** – Automatically **save and restore personal information** using browser `localStorage`.  
- 🤖 **AI-Powered Generation** – Uses **OpenRouter + GLM-4.5 Air** model to generate tailored cover letters.  
- 🌓 **Unified Theme** – Ensures consistent look & feel across both light and dark modes.  

---

## 🚀 Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/colego-cover-letter.git
cd colego-cover-letter
```

### 2. Install Dependencies  
Make sure you have **Python 3.9+** and **pip** installed.  
```bash
pip install -r requirements.txt
```

### 3. Set API Key  
Update your OpenRouter API key in the code:  
```python
TOKEN_KEY = "your_openrouter_api_key"
```

> 🔑 Get your API key from [OpenRouter](https://openrouter.ai/).  

### 4. Run the Application  
```bash
streamlit run app.py
```

---

## 🖼️ Interface Overview  

### **Personal Information Form**  
- Full Name  
- Email Address  
- Phone Number  
- Technical & Soft Skills  
- Personal Background  

### **Job Information Form**  
- Position Title  
- Company Name  
- Job Description  
- Focus Points (optional)  

### **Output Section**  
- Displays your **AI-generated cover letter**  
- Option to re-generate if needed  

---

## ⚙️ Tech Stack  

- [Streamlit](https://streamlit.io/) – Web interface  
- [OpenRouter](https://openrouter.ai/) – AI API provider  
- [GLM-4.5 Air](https://openrouter.ai/models/z-ai/glm-4.5-air) – LLM used for cover letter generation  
- [streamlit-js-eval](https://pypi.org/project/streamlit-js-eval/) – For `localStorage` support  

---

## 📂 Project Structure  

```
colego/
│── app.py               # Main Streamlit application
│── Service.py           # Handles API calls to OpenRouter
│── prompt.json          # Prompt template for AI
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation
```

---

## 📌 Future Improvements  

- ⬇️ Export cover letters to **PDF / DOCX**  
- 🌐 Multi-language support (EN/中文)  
- 🎯 More customization (tone, format, company-specific highlights)  
- ☁️ Cloud storage for saved profiles  

---

## 📜 License  

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.  

---

## 👨‍💻 Author  

**Jack Jin**  
Computer Science & Business Minor @ McMaster University  
🔗 [GitHub](https://github.com/your-username)  
