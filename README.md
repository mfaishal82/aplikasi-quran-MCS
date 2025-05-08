# Surah Maryam Verses Webpage

```
https://quran-seven-psi.vercel.app/
```

This project is a responsive web page that displays verses from Surah Maryam in Arabic along with their translations. The design is inspired by Islamic art and typography, using the Amiri font for an authentic look and feel.

## Features

- Fetches Surah Maryam verses dynamically from a remote API.
- Displays Arabic text with right-to-left direction and styled typography.
- Shows translations in italic style below each verse.
- Responsive design that adapts to different screen sizes including mobile devices.
- Decorative Islamic pattern border and hover effects for enhanced user experience.

## Technologies Used

- HTML5 and CSS3 for structure and styling.
- Google Fonts (Amiri) for Arabic typography.
- JavaScript (Fetch API) to retrieve verses from the API.

## Usage

1. Open `frontend/index.html` in a modern web browser.
2. The page will automatically fetch and display the verses from the API.
3. Ensure you have an active internet connection to load the font and fetch data.

## API Endpoint

The verses are fetched from the following API endpoint:

```
https://impartial-adaptation-production.up.railway.app/api/verses/maryam
```

## Running the Server

The backend server is built with FastAPI and serves the API endpoint for fetching Surah Maryam verses.

### Prerequisites

- Python 3.7 or higher
- PostgreSQL database with the Quran data
- A `.env` file in the `backend/` directory containing the `SUPABASE_CONNECTION_STRING` environment variable with your database connection string.

### Installation

1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

Run the FastAPI server using uvicorn:

```bash
uvicorn backend:app --host 0.0.0.0 --port 8000
```

If port 8000 is busy, the server will try port 8001.

### Accessing the API

The API endpoint for Surah Maryam verses will be available at:

```
http://localhost:8000/api/verses/maryam
```

## License

This project is open source and free to use.
