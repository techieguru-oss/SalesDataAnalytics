import pandas as pd
def load_dataset(filepath):
    """
    Load Superstore dataset.
    """

    df = pd.read_csv(filepath, encoding='latin-1')

    print(
        f"Dataset loaded successfully: {df.shape}"
    )

    return df