

import pandas as pd


def get_label_map(conn):
    """Returns {Id: 'User N'}, sorted by Id so labels stay consistent."""
    ids = pd.read_sql("SELECT DISTINCT Id FROM daily_activity ORDER BY Id", conn)["Id"].tolist()
    return {uid: f"User {i + 1}" for i, uid in enumerate(ids)}