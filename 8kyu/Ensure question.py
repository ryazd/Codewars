def ensure_question(s):
    return s if len(s) > 0 and s[-1] == '?' else s + '?'