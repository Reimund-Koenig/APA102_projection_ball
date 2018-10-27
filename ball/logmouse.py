global log_levels
log_levels = {
    "debug":10,
    "info":20,
    "warning":30,
    "critical":40,
    "error":50
}

def log(lvl, message):
    # writeInFile = False
    enabledLogLevel = log_levels["info"]
    if lvl < enabledLogLevel:
        return
    if lvl >= log_levels["error"]:
        print("Error: " +  message)
    elif lvl >= log_levels["critical"]:
        print("Critical: " +  message)
    elif lvl >= log_levels["warning"]:
        print("Warning: " +  message)
    elif lvl >= log_levels["info"]:
        print("Info: " +  message)
    elif lvl >= log_levels["debug"]:
        print("Debug: " +  message)
