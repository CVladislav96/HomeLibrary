import time
from sqlalchemy import text
from database.database import engine

def wait_for_database(max_attempts: int = 10, delay: int = 2) -> bool:
    """
    Wait for database availability
    
    Args:
        max_attempts: Maximum number of attempts
        delay: Delay between attempts in seconds
    
    Returns:
        bool: True if database is available, False otherwise
    """
    for attempt in range(max_attempts):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print(f"✅ Database connected successfully on attempt {attempt + 1}")
            return True
        except Exception as e:
            print(f"⏳ Attempt {attempt + 1}/{max_attempts}: Database not ready - {e}")
            if attempt < max_attempts - 1:
                time.sleep(delay)
    
    print(f"❌ Database not available after {max_attempts} attempts")
    return False

def check_database_connection() -> bool:
    """
    Quick database connection check
    
    Returns:
        bool: True if database is available
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False