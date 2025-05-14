from rapidfuzz import fuzz, process

def fuzzy_match_name(name, df):
    if df.empty:
        return None, 0
    result, score, _ = process.extractOne(name, df['name'], scorer=fuzz.token_sort_ratio)
    return result, score
