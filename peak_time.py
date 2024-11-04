import pandas as pd

def peak():
    path_file = "signal_time.xlsx"
    df = pd.read_excel(path_file)
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df.set_index('datetime', inplace=True)
    
    peak_values = {
        "North": df['north'].max(),
        "East": df['east'].max(),
        "South": df['south'].max(),
        "West": df['west'].max()
    }

    peak_times = {
        "North": df['north'].idxmax(),
        "East": df['east'].idxmax(),
        "South": df['south'].idxmax(),
        "West": df['west'].idxmax()
    }

    time_range = {
        direction: {
            "peak_time": peak_times[direction],
            "start_time": df.index[df.index.get_loc(peak_times[direction]) - 1] if df.index.get_loc(peak_times[direction]) > 0 else df.index[0],
            "end_time": df.index[df.index.get_loc(peak_times[direction]) + 1] if df.index.get_loc(peak_times[direction]) < len(df.index) - 1 else df.index[-1]
        }
        for direction in peak_times
    }

    return time_range

