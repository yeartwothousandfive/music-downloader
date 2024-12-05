
def is_valid_url(url):
    """Check if the given string is a valid URL."""
    return url.startswith("http://") or url.startswith("https://")
