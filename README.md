# Quant-Model
This project demonstrates a quantitative trading model that analyzes price action on ES (E-mini S&P 500 futures) using technical indicators and bounce detection signals.

## What It Does
The model identifies when price touches a 20-day simple moving average and subsequently bounces away from it. These bounce signals can indicate potential support or resistance levels where the market reverses direction.

## Key Components
- **Data Source**: Historical ES futures data via yfinance
- **Primary Indicator**: 20-day Simple Moving Average (SMA)
- **Signal Logic**: Detects price proximity to the SMA and identifies upward or downward bounces
- **Visualization**: Charts price action with SMA overlay and bounce signal markers

## Files
- `first_script.py`: Main model script with data processing and signal generation
- `README.md`: Project documentation

## Technologies Used
- Python 3.9
- Pandas (data manipulation)
- yfinance (data retrieval)
- Matplotlib (visualization)

## Future Enhancements
- Sentiment analysis from news headlines
- Fair value gap detection
- Order flow analysis
- Multi-timeframe analysis

## How to Run
1. Install dependencies: `pip3 install pandas numpy matplotlib yfinance`
2. Run the script: `python3 first_script.py`
3. View the generated chart with bounce signals
