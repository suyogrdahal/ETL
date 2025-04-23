from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.util import setup_logging
from src.visualization import create_visuals

def main():
    setup_logging() 

    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    load_data(df_clean)
    create_visuals(df_clean)

if __name__ == "__main__":
    main()
