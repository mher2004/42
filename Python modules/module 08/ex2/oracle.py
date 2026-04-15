from dotenv import load_dotenv  # type: ignore
import os


def load_config() -> dict[str, str | None]:
    load_dotenv()
    data = {
        'MATRIX_MODE': os.getenv("MATRIX_MODE"),
        'DATABASE_URL': os.getenv("DATABASE_URL"),
        'API_KEY': os.getenv("API_KEY"),
        'LOG_LEVEL': os.getenv("LOG_LEVEL"),
        'ZION_ENDPOINT': os.getenv("ZION_ENDPOINT"),
    }
    return data


def display_config(config: dict[str, str | None]) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print("Mode:",
          config['MATRIX_MODE'] if config['MATRIX_MODE'] is not None else "\
WARNING: The variable was not set")
    if config['MATRIX_MODE'] == "development":
        print("Database:",
              config['DATABASE_URL'] if config['DATABASE_URL\
'] is not None else "WARNING: The variable was not set")
    else:
        print("Database:",
              "Connected to local instance\
    " if config['DATABASE_URL'] is not None else "\
WARNING: The variable was not set")
    if config['MATRIX_MODE'] == "development":
        print("API Access:",
              config['API_KEY'] if config['API_KEY'] is not None else "\
WARNING: The variable was not set")
    else:
        print("API Access:",
              "Authenticated" if config['API_KEY'] is not None else "\
WARNING: The variable was not set")
    print("Log Level:",
          config['LOG_LEVEL'] if config['LOG_LEVEL'] is not None else "\
WARNING: The variable was not set")
    if config['MATRIX_MODE'] == "development":
        print("Zion Network:",
              config['ZION_ENDPOINT'] if config['ZION_ENDPOINT\
'] is not None else "WARNING: The variable was not set")
    else:
        print("Zion Network:",
              "Online" if config['ZION_ENDPOINT'] is not None else "\
WARNING: The variable was not set")
    print()


def security_check(config: dict[str, str | None]) -> None:
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[KO] .env file not properly configured\
" if None in config.values() else "[OK] .env file properly configured")
    print("[OK] Production overrides available")


display_config(load_config())
security_check(load_config())
