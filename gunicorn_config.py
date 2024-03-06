import multiprocessing

bind = "0.0.0.0:8080"  # Adjust the host and port as needed
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2

# Adjust the path to your application object
app_module = "your_app_module_name:app"

# Optional: Set the log level
loglevel = "info"

# Optional: Set the error log file path
#errorlog = "/error.log"
