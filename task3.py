import sys
from pathlib import Path
from collections import Counter

def parse_log_line(line: str) -> dict:
    date, time, level, message = line.strip().split(maxsplit=3)
    return {"date": date, "time": time, "level": level.upper(), "message": message}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r") as f:
            for lines in f:
                logs.append(parse_log_line(lines))    #save dict from parse to list with all dicts
            return logs
    except FileNotFoundError:
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level.upper()]

def count_log_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]  #makes list of levels
    level_counts = Counter(levels)          #counts levels
    return level_counts

def display_log_counts(counts):
    print(f"Рівень логування | Кількість")
    print(f"{"-"* 17}|{"-" *10}")
    for key, val in counts.items():         #key is level, val is counts
        print(f"{key:<16} | {val}")

def main():    
    if len(sys.argv) < 2:
        return print("Write absolute path of log after file name")
    p = Path(sys.argv[1])
    need_to_filter = None
    if p.stat().st_size == 0:
        return print("File is empty")           #check if file is empty
    
    get_logs = load_logs(p)
    if get_logs == []:
        return print("Incorrect path")
    
    count_logs = count_log_by_level(get_logs)
    display_log_counts(count_logs)
    
    try:
        if sys.argv[2].lower() in ["info", "error", "debug", "warning"]:  # find this words in command and use func
            need_to_filter = sys.argv[2].lower()        
    except IndexError:
        pass
    if need_to_filter != None:      #if user writes smt from this ^ dict, print abt info that user wrote
        filtered_logs = filter_logs_by_level(get_logs, need_to_filter)
        print(f"Деталі логів для рівня '{need_to_filter.upper()}':")
        for dict in filtered_logs:
            print(f"{dict["date"]} {dict["time"]} - {dict["message"]}")

if __name__ == "__main__":
    main()