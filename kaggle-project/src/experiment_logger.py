import os
import pandas as pd
from datetime import datetime
from typing import Dict, Optional

LOG_FILE = 'experiments_log.csv'


def log_experiment(
    experiment_name: str,
    model_name: str,
    params: Dict,
    cv_score: float,
    comment: Optional[str] = None
) -> None:
    """
    Loguje eksperyment do pliku CSV.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = {
        'timestamp': timestamp,
        'experiment_name': experiment_name,
        'model_name': model_name,
        'params': str(params),
        'cv_score': cv_score,
        'comment': comment if comment is not None else ''
    }
    columns = ['timestamp', 'experiment_name', 'model_name', 'params', 'cv_score', 'comment']
    file_exists = os.path.isfile(LOG_FILE)
    df = pd.DataFrame([entry], columns=columns)
    if not file_exists:
        df.to_csv(LOG_FILE, index=False, mode='w')
    else:
        df.to_csv(LOG_FILE, index=False, mode='a', header=False)


def load_experiments() -> pd.DataFrame:
    """
    Ładuje logi eksperymentów jako DataFrame.
    """
    if not os.path.isfile(LOG_FILE):
        return pd.DataFrame(columns=['timestamp', 'experiment_name', 'model_name', 'params', 'cv_score', 'comment'])
    return pd.read_csv(LOG_FILE) 