from services.home_service import get_home_data, get_health_status

def home():
    return get_home_data()

def health():
    return get_health_status()