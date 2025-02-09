def check_number(x):
    state = ""
    if x > 0:
        state = "Positive"
    elif x < 0:
        state = "Negative"
    else:
        state = "Zero"
    return state
