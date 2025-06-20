import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
USER_SESSION = os.getenv("USER_SESSION")

GROUP1_ID = int(os.getenv("GROUP1_ID"))  # ID основной группы
GROUP2_ID = int(os.getenv("GROUP2_ID"))  # ID группы для пересылки

# Список ID модераторов через запятую в secrets
MODERATOR_IDS = [int(i) for i in os.getenv("MODERATOR_IDS", "").split(",") if i]