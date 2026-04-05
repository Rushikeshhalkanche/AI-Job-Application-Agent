def detect_ats(url):
    if "workday" in url:
        return "Workday"
    elif "greenhouse" in url:
        return "Greenhouse"
    elif "lever" in url:
        return "Lever"
    else:
        return "Unknown"