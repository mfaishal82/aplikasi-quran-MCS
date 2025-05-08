from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import psycopg2
from dotenv import load_dotenv
from typing import List, Dict
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = FastAPI()

# Konfigurasi CORS yang lebih sederhana
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    try:
        connection_string = os.getenv('SUPABASE_CONNECTION_STRING')
        if not connection_string:
            logger.error("SUPABASE_CONNECTION_STRING tidak ditemukan di .env file")
            return None
        
        logger.info("Mencoba koneksi ke database...")
        conn = psycopg2.connect(connection_string)
        logger.info("Koneksi database berhasil")
        return conn
    except Exception as e:
        logger.error(f"Error koneksi database: {str(e)}")
        return None

@app.get("/api/verses/maryam")
async def get_maryam_verses():
    try:
        logger.info("Memulai request untuk mengambil ayat Maryam")
        conn = get_db_connection()
        
        if not conn:
            return JSONResponse(
                status_code=500,
                content={"error": "Tidak dapat terhubung ke database"}
            )
            
        cur = conn.cursor()
        
        query = """
        SELECT 
            verse_id,
            verse_text,
            indo_text
        FROM quranidn
        WHERE surah_name = 'Maryam'
        ORDER BY verse_id;
        """
        
        logger.info("Menjalankan query database...")
        logger.info(f"Query: {query}")
        
        try:
            cur.execute(query)
            verses = cur.fetchall()
            logger.info(f"Berhasil mengambil {len(verses)} ayat")
            
            # Format hasil query
            result = [
                {
                    "verse_number": verse[0],
                    "text_arabic": verse[1],
                    "text_translation": verse[2]
                }
                for verse in verses
            ]
            
            return JSONResponse(content=result)
            
        except Exception as e:
            logger.error(f"Error saat menjalankan query: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"error": f"Error saat menjalankan query: {str(e)}"}
            )
        finally:
            cur.close()
            conn.close()
            
    except Exception as e:
        logger.error(f"Error umum: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Error umum: {str(e)}"}
        )

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except OSError:
        logger.info("Port 8001 sudah digunakan, mencoba port 8001...")
        uvicorn.run(app, host="0.0.0.0", port=8001) 