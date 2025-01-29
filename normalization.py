def normalize(data):
    """Normalize a list of numbers using min-max normalization."""
    if not data:
        return []
    
    min_val = min(data)
    max_val = max(data)
    
    if min_val == max_val:
        return [0] * len(data)  # Avoid division by zero

    return [(x - min_val) / (max_val - min_val) for x in data]

# Example usage
data = [10, 20, 30, 40, 50]
normalized_data = normalize(data)
print(normalized_data)
