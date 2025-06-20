import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
USER_SESSION = os.getenv("USER_SESSION")

GROUP1_ID = int(os.getenv("GROUP1_ID"))      # Основная группа (откуда пересылать)
GROUP2_ID = int(os.getenv("GROUP2_ID"))      # Группа модерации

# Перечислите id модераторов через запятую в секрете MODERATOR_IDS
MODERATOR_IDS = [int(i) for i in os.getenv("MODERATOR_IDS", "").split(",") if i.strip()]
