# Chat Bot Project

This README file provides an extensive guide on setting up and running a Chat Bot using Streamlit and Cohere API. The bot allows for interactive conversation and showcases messages from both the user and the assistant.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project implements a simple chat bot using Streamlit for the web interface and Cohere's API for generating responses. The chat bot can engage in a conversation with users, displaying messages from both the user and the assistant in a chat-like format.

## Features

- Interactive chat interface
- Real-time message display
- Uses Cohere API for generating responses
- Session state management to keep track of conversation history

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Streamlit library
- Cohere library
- A Cohere API key

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/chat-bot.git
    cd chat-bot
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required libraries:

    ```bash
    pip install streamlit cohere
    ```

## Usage

1. Set up your Cohere API key in Streamlit secrets. Create a file named `.streamlit/secrets.toml` in the root directory of your project and add the following:

    ```toml
    [secrets]
    COHERE_API_KEY = "your_cohere_api_key"
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

3. Open your web browser and navigate to `http://localhost:8501` to interact with the chat bot.

## Project Structure

chat-bot/
├── .streamlit/
│ └── secrets.toml
├── app.py
├── README.md
└── venv/


- `.streamlit/secrets.toml`: Contains the API key for Cohere.
- `app.py`: The main script for running the Streamlit app.
- `README.md`: This README file.
- `venv/`: The virtual environment directory (not included in the repository).

## Configuration

### Streamlit Secrets

The Cohere API key is stored securely in Streamlit secrets. Ensure you add your key in the `.streamlit/secrets.toml` file as shown above.

### Session State

The app uses Streamlit's session state to keep track of the conversation history. Messages are stored in `st.session_state["messages"]` and are displayed in the chat container.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are reviewed on a regular basis.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This README provides a comprehensive guide to setting up and using the chat bot. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or contribute to the project.
