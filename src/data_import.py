import argparse
from typing import List
import pandas as pd
import sys
import os
from pathlib import Path


def main(args: List[str]) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=str)
    parser.add_argument("output_dir", type=str)
    parsed_args = parser.parse_args()

    input_df = pd.read_csv(Path(parsed_args.input_dir, "input.csv"))
    train_df = input_df.iloc[:2]
    test_df = input_df.iloc[2:]

    os.makedirs(parsed_args.output_dir, exist_ok=True)

    train_df.to_csv(Path(parsed_args.output_dir, "train.csv"), index=False)
    test_df.to_csv(Path(parsed_args.output_dir, "test.csv"), index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
