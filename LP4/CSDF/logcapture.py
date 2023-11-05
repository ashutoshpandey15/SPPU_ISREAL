import time

# Simulating log sources with sample data
log_sources = {
    "Server_A": ["Data processed", "Error occurred"],
    "Server_B": ["Connection established","Error occurred"],
    "Server_C": ["Error occurred","Connection established"]
}

# Log capturing and event correlation
def capture_and_correlate_logs(log_sources):
    # Record logs with timestamps
    logs_with_timestamps = {}
    for server, logs in log_sources.items():
        timestamp = int(time.time())
        logs_with_timestamps[server] = [(log, timestamp) for log in logs]

    # Event correlation - Find patterns or associations
    correlation_results = {}
    for server, logs in logs_with_timestamps.items():
        for log, timestamp in logs:
            if log not in correlation_results:
                correlation_results[log] = []
            correlation_results[log].append((server, timestamp))

    # Display the correlated events
    print("Correlated Events:")
    for log, servers in correlation_results.items():
        print(f"{log}:")
        for server, timestamp in servers:
            print(f"  - Occurred on {server} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}")

if __name__ == "__main__":
    capture_and_correlate_logs(log_sources)
