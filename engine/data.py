import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config.settings import *
import pandas as pd
import yfinance as yf

def load_hist_data(save_csv=False) -> pd.DataFrame:
    """
    Load historical price data for the specified universe of assets.
    If save_csv is True, saves the raw data to CSV files in the RAW_DATA_DIR.
    Returns a DataFrame with multi-index (Date, Ticker) and columns for Open, High, Low, Close, Volume.
    """
    df = yf.download(
        tickers=UNIVERSE,
        start=START_DATE,
        end=END_DATE,
        interval=BAR_FREQUENCY,
        group_by='ticker',
        auto_adjust=USE_ADJUSTED_PRICES,
        progress=False,
        threads=True
    )
    if df.empty:
        raise ValueError("No data downloaded. Check your settings and internet connection.")

    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)

    if save_csv:
        data_dir = RAW_DATA_DIR
        data_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(data_dir / "historical_data.csv")


        if save_csv:
            data_dir = RAW_DATA_DIR
            data_dir.mkdir(parents=True, exist_ok=True)
            for ticker in UNIVERSE:
                ticker_df = df[ticker]
                ticker_df.to_csv(data_dir / f"{ticker}.csv")
    return df

def clean_data(df: pd.DataFrame, ticker) -> pd.DataFrame:
    """
    Clean the raw data by handling missing values and ensuring correct data types.
    Returns a cleaned DataFrame ready for analysis.
    """
    df = df.dropna() if DROP_MISSING_ROWS else df.ffill().bfill()
    df = df.astype({"Open": float, "Close": float, "High": float, "Low": float, "Volume": int})
    df = df.sort_index()
    if len(df) < MIN_OBSERVATIONS:
        raise ValueError(f"Not enough data for {ticker}. Only {len(df)} observations available.")
    return df

def build_dataset(save_csv = False) -> pd.DataFrame:
    """
    Load and clean historical data for all assets in the universe, then combine into a single DataFrame.
    Returns a DataFrame with multi-index (Date, Ticker) and columns for Open, High, Low, Close, Volume.
    """
    all_data = []
    raw_df = load_hist_data(save_csv=False)
    for ticker in UNIVERSE:
        ticker_df = raw_df[ticker]
        cleaned_df = clean_data(ticker_df, ticker)
        cleaned_df['Ticker'] = ticker
        all_data.append(cleaned_df)
    combined_df = pd.concat(all_data)
    combined_df = combined_df.reset_index()
    combined_df = combined_df.set_index(['Date', 'Ticker'])

    if save_csv:
            data_dir = PROCESSED_DATA_DIR
            data_dir.mkdir(parents=True, exist_ok=True)
            for ticker in UNIVERSE:
                ticker_df = combined_df.xs(ticker, level='Ticker')
                ticker_df.to_csv(data_dir / f"{ticker}.csv")
    return combined_df



# add this temporarily at the bottom of data.py
if __name__ == "__main__":
    df = build_dataset(save_csv=True)
    print(df.head())
    print(df.shape)
    print(df.index.get_level_values('Ticker').unique())