# Multimedia interactive Library Fetch Bot (MiLF Bot)

## Description
ATM can only fetch Photos, Animations (GIFs) and videos from rule34 site and danbooru
> TODO...

## USAGE:
### Requirements:
1.  Python 3.10+
2.  aiogram
3.  aiohttp
4.  python-dotenv 
### Installation:
1.  **Clone the repository:**

    ```bash
    git clone 
    ```
2.  **Navigate to the project directory:**

    ```bash
    cd milfbot
    ```
3.  **(Recommended) Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```
    Or adaptive it for your system/shell
4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Launch
1.  **Copy `.env.example` to `.env`:**

    ```bash
    cp .env.example .env
    ```
2.  **Enter your Telegram bot token:**

    - Open the `.env` and replace `BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN` with your actual bot token.

3.  **(Optional) Replace the Rule34 site token:**

    - If necessary, modify the `RULE34_URL` variable in the `.env` file

4.  **Run the script:**

    ```bash
    python main.py
    ```
### Using
1.  **Make sure that your bot using inline mode!**

2.  **Enter your Telegram chat**

3.  **Start writing message**

    - example: `@YOURBOT pic/vid/gif r34/danbooru [TAGS]`

## Contributing

We welcome contributions to MiLF Bot!  
If you have ideas, bug reports, or feature requests, please open an issue.

### How to contribute

1. **Fork the repository** and create your branch from `main`.
2. **Make your changes** (code, documentation, tests).
3. **Ensure your code follows project style** and passes all checks.
4. **Submit a pull request** with a clear description of your changes.


If you need help, feel free to open an issue or start a discussion.

Thank you for helping improve MiLF Bot!