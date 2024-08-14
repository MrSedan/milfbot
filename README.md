# Multimedia Interactive Fetch Bot (MiLF Bot)

## Description
ATM can only fetch photos from rule34 site
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

## Contributing

> TODO...

Feel free for oppening issues