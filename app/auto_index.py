def suggest_indexes(query_logs):
    suggestions = {}
    for log in query_logs:
        query = log['query'].lower()
        if "where" in query:
            tokens = query.split()
            if "where" in tokens:
                idx = tokens.index("where")
                col = tokens[idx + 1] if idx + 1 < len(tokens) else None
                if col:
                    suggestions[col] = suggestions.get(col, 0) + 1
    top_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)[:3]
    return [col for col, _ in top_suggestions]