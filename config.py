import os
from os import getenv


API_ID = int(getenv("API_ID", "14944661"))
API_HASH = getenv("API_HASH", "f3585362239143a3e3f54f1f55b4fbee")
BOT_USERNAME = getenv("BOT_USERNAME", "grp_mnger_bot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "5614436810:AAF8TSe-8wDX3ArnwTtCOtSNuMSv3pz4WDg")
OWNER_ID = int(getenv("OWNER_ID", "2138327453"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6691393517").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://rahul:rahulkr@cluster0.szdpcp6.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "AQFMuUIAbQYZTm9hLpl6WtZTJNP3kckeZ5Yy-WFQIkGuBJqPCKLcWBY9FJjTWDQQqPUViRRXs95mcot3nNeZbOQBIRfd1LoH2HBgM4rOa17XByH_HwO_sfmPN9xYt8786mxnLd6b9X8vfqZ325Bq9C6zWnPLrVNDqpU70XxvCmnQBt8tY7fcTv5R6_kWElAoMNdETLoBpJnEK-6DwWhic5l2GEKBjQDOjEh-zyvljgKFRWI58bJQB9PLV9LKoW0a4ldcvnkeByXZEZLLEUp-x_S6zHeBtPuNhJQ5vsfzb82wAB1kASsqfZELkS4LmV2oIbRchOaqfBu8AEMoHj_8QJN-fqsI0AAAAAGAkGbDAA")
