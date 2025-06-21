# ☕ Best Coffee Store – Virtual Coffee Seller

This is a Streamlit-based chatbot application that simulates a virtual coffee seller. The app uses a large language model to help users choose from a set of predefined coffee options.

## 🚀 Features

- Friendly chatbot designed to simulate a coffee shop assistant
- Suggests options from six types of coffee:
  - Roast Black Coffee
  - Seasonal Coffee
  - Starbucks Coffee
  - Strong Coffee
  - Casual Coffee
  - Pink Coffee
- Clean, responsive Streamlit interface
- Easily configurable with your OpenAI API key

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vertocode/best-coffee-ai.git
   cd best-coffee-ai
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_key_here
   ```

## ▶️ Running the App

```bash
streamlit run src/app.py
```

The app will open in your browser. Just type your coffee preference and the assistant will suggest a drink!

## 🧠 How It Works

The app uses `langchain` to build a conversational prompt with a system message that defines the assistant as a coffee seller. It passes the user input through the chain to get a response from OpenAI.

## ✨ Customization

You can customize the coffee types, tone, or assistant personality by modifying the system prompt in `agent.py`.

## 📄 License

MIT License. Feel free to modify and use this project for your own virtual store experiments!