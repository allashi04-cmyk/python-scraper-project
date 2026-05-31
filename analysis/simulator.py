import numpy as np
import pandas as pd

def apply_visualization_noise(df: pd.DataFrame, noise_factor: float = 0.05, seed_offset: int = 0) -> pd.DataFrame:

    df = df.copy()
    
    df['scraped_at'] = pd.to_datetime(df['scraped_at'])
    df['run_id'] = df['scraped_at'].dt.floor('min').astype(str) 
    
    for run_id in df['run_id'].unique():
        mask = df['run_id'] == run_id
        np.random.seed(hash(run_id) % (2**32) + seed_offset) 
        
        df.loc[mask, 'price_viz'] = df.loc[mask, 'price_num'] * np.random.uniform(
            1 - noise_factor, 1 + noise_factor, size=mask.sum()
        )
    
    return df.round(2)