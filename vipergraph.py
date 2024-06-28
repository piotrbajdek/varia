#!/usr/bin/env python3

import sys
import os
import pandas as pd
import mplfinance as mpf


def main():
    if len(sys.argv) != 2:
        print("Użycie: python vipergraph.py <nazwa_pliku.csv>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        df = pd.read_csv(
            filename,
            header=None,
            names=["Date", "Time", "Open", "High", "Low", "Close", "Volume"],
        )

        print(df.head())
        print("\nNazwy kolumn:")
        print(df.columns)

        df["DateTime"] = pd.to_datetime(df["Date"] + " " + df["Time"])
        df.set_index("DateTime", inplace=True)
        df.drop(["Date", "Time"], axis=1, inplace=True)

        for col in ["Open", "High", "Low", "Close", "Volume"]:
            df[col] = df[col].astype(float)

        title = os.path.basename(filename)

        mpf.plot(
            df,
            type="candle",
            style="classic",
            volume=True,
            title=title,
            ylabel="Cena",
            ylabel_lower="Wolumen",
            figsize=(12, 8),
        )

        print(
            f"Wykres dla pliku '{title}' został wygenerowany. Sprawdź, czy nie został otwarty w nowym oknie."
        )

    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {filename}")
    except pd.errors.EmptyDataError:
        print(f"Plik {filename} jest pusty.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    main()
