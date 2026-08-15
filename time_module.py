import time

# ---------------------------------------------------------
# 1. time.time() -> returns current time in seconds since epoch (float)
# WHY: Used to measure elapsed time / calculate duration of code execution
# WHERE: Performance benchmarking, logging timestamps, measuring API response time
# ---------------------------------------------------------
start = time.time()
# ... some code to measure ...
for i in range(1000000):
    pass
end = time.time()
print(f"Elapsed time: {end - start:.4f} seconds")


# ---------------------------------------------------------
# 2. time.sleep(seconds) -> pauses program execution
# WHY: Used to delay execution / avoid overwhelming a server / simulate wait
# WHERE: Rate-limiting API calls, retry logic, polling loops, animations
# ---------------------------------------------------------
print("Starting task...")
time.sleep(2)  # pause for 2 seconds (e.g., waiting before retrying a failed request)
print("Task resumed after delay")


# ---------------------------------------------------------
# 3. time.perf_counter() -> high-resolution timer (best for benchmarking)
# WHY: More precise than time.time(), unaffected by system clock changes
# WHERE: Precise performance testing / micro-benchmarking algorithms
# ---------------------------------------------------------
start = time.perf_counter()
sum([i for i in range(100000)])
end = time.perf_counter()
print(f"Precise elapsed time: {end - start:.6f} seconds")


# ---------------------------------------------------------
# 4. time.localtime() -> converts epoch time to local time (struct_time)
# WHY: Used to get human-readable date/time components (year, month, day, etc.)
# WHERE: Logging events, displaying current date/time to users, timestamping files
# ---------------------------------------------------------
current = time.localtime()
print(f"Year: {current.tm_year}, Month: {current.tm_mon}, Day: {current.tm_mday}")
print(f"Time: {current.tm_hour}:{current.tm_min}:{current.tm_sec}")


# ---------------------------------------------------------
# 5. time.strftime(format, struct_time) -> formats time into readable string
# WHY: Used to display time in a custom, human-friendly format
# WHERE: Report generation, log files, filenames with timestamps, UI display
# ---------------------------------------------------------
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"Formatted time: {formatted_time}")
# WHERE (example use): naming a backup file
filename = f"backup_{time.strftime('%Y%m%d_%H%M%S')}.zip"
print(f"Backup filename: {filename}")


# ---------------------------------------------------------
# 6. time.strptime(string, format) -> parses a string into struct_time
# WHY: Used to convert a text date/time (e.g., from user input or file) into a usable time object
# WHERE: Parsing dates from logs, CSV files, or user-entered forms
# ---------------------------------------------------------
time_string = "2026-08-15 10:30:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed year: {parsed_time.tm_year}, month: {parsed_time.tm_mon}")


# ---------------------------------------------------------
# 7. time.ctime() -> converts epoch seconds into a readable string directly
# WHY: Quick, simple way to convert timestamp to readable date without formatting manually
# WHERE: Quick debug prints, simple logs where exact format doesn't matter
# ---------------------------------------------------------
print(f"Current readable time: {time.ctime()}")
print(f"Readable time from epoch 0: {time.ctime(0)}")  # useful to check epoch start


# ---------------------------------------------------------
# 8. time.monotonic() -> a clock that never goes backward (unaffected by system clock adjustments)
# WHY: Safer than time.time() for measuring durations, since NTP sync or manual clock 
#      changes won't cause negative/incorrect elapsed time
# WHERE: Timeout logic, scheduling, measuring intervals in long-running services
# ---------------------------------------------------------
start = time.monotonic()
time.sleep(1)
end = time.monotonic()
print(f"Monotonic elapsed time: {end - start:.4f} seconds")