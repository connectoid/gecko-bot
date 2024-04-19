from dataclasses import dataclass
from environs import Env


proxy_list = [
    'http://LJ64PB:2FeTxb@94.131.19.56:9701',
    'http://LJ64PB:2FeTxb@95.164.201.179:9911',
    'http://LJ64PB:2FeTxb@95.164.202.85:9327',
    'http://LJ64PB:2FeTxb@94.131.54.35:9085',
    'http://LJ64PB:2FeTxb@186.179.61.133:9579',
    'http://LJ64PB:2FeTxb@91.218.50.161:9997',
    'http://LJ64PB:2FeTxb@38.153.57.53:9190',
    'http://LJ64PB:2FeTxb@38.152.246.128:9310',
    'http://LJ64PB:2FeTxb@94.131.87.20:9548',
    'http://LJ64PB:2FeTxb@94.131.89.115:9108',
    'http://0P7hy1:gQwmN3@91.216.186.243:8000', 
    'http://0P7hy1:gQwmN3@91.216.186.52:8000',
    'http://nmjXXw:C3FhBp@185.77.139.24:8000',
    'http://nmjXXw:C3FhBp@185.77.139.213:8000',
    'http://TNRBbV:qKF1Ar@168.181.54.57:8000',
]


@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных
    

@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту 
    admin_chat_id: str


@dataclass
class Payment:
    paymen_provider_token: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
    payment: Payment


def load_config(path: str = None):

    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_chat_id=env('ADMIN_CHAT_ID')),
                    db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD')),
                    payment=Payment(paymen_provider_token=env('PAYMENTS_PROVIDER_TOKEN')),
                    )
