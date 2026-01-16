def generate_refresh_plan(status: str):
    if status == "Critical":
        return {"days": 14, "minutes_per_day": 45}
    elif status == "At-Risk":
        return {"days": 7, "minutes_per_day": 30}
    return {"days": 3, "minutes_per_day": 15}
