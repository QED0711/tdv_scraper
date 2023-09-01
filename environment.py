import os, datetime
DATA_OUTPUT_DIR = os.getenv("DATA_OUTPUT_DIR", "/app/charts")

BASE_PATH = os.path.join(DATA_OUTPUT_DIR, str(datetime.date.today()))