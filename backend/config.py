from dotenv import load_dotenv
import os 


load_dotenv()


DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
JWT_SECRET = os.environ.get('JWT_SECRET')

