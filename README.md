# Japan Post Digital Address (for Biz) - API Client

A simple, secure Python script to fetch address data from Japan Post's **Digital Address for Biz** API. This client handles JWT (Bearer) authentication and retrieves address details using zip codes or digital addresses.

## Features

- **OAuth 2.0 Flow**: Automatically fetches a JWT token using your Client ID and Secret Key.
- **Address Search**: Retrieves detailed address information (Prefecture, City, Town, Business Name, etc.).
- **Security**: Environment variable support (via `.env`) to keep your credentials safe.
- **Environment Support**: Easily switch between Stub (test) and Production endpoints.

## Prerequisites

- Python 3.8 or higher
- A valid Client ID and Secret Key provided by Japan Post (JP Digital).

## Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:stprec-yuu/jp-digital-address-biz.git
   cd seach-addr

```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



## Configuration

Create a `.env` file in the root directory of the project and add your API credentials:

```env
JP_CLIENT_ID=your_client_id_here
JP_SECRET_KEY=your_secret_key_here
JP_API_BASE_URL=[https://stub-qz73x.da.pf.japanpost.jp/api/v1](https://stub-qz73x.da.pf.japanpost.jp/api/v1)

```

> [!CAUTION]
> Never commit your `.env` file to a public repository. It is already included in the `.gitignore`.

## Usage

Run the script by providing a zip code or digital address as an argument:

```bash
python search-addr.py 1008791

```

### Example Output:

```text
[1008791] 東京都千代田区大手町２－３－１ (日本郵政　株式会社)

```

## Error Handling

* **401 Unauthorized**: Check if your credentials in `.env` are correct or if the token has expired.
* **404 Not Found**: The zip code does not exist in the current database (Note: Stub environments have limited test data).
* **500 Error**: Connection issues or server-side problems.

## License

This project is for internal use and demonstration purposes.

