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

3.  **(Optional) Use a custom API endpoint:**

    - If you want to use your own service or a different mirror, modify the corresponding URL variables (e.g. `RULE34_URL`, `DANBOORU_URL`, etc.) in your `.env` file.
    - You can add new variables for other services as needed and update the

4.  **Run the script:**

    ```bash
    python main.py
    ```
### Using
1.  **Make sure that your bot using inline mode!**

2.  **Enter your Telegram chat**

3.  **Start writing message**

    - example: `@YOURBOT pic/vid/gif r34/danbooru [TAGS]`
        > **Note:** Danbooru restricts tag searches for users without an upgraded account.  
        > You can only use **one tag** per search unless you have a gold danbooru profile.  
        > If you use more tags, you may get an error and empty results

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