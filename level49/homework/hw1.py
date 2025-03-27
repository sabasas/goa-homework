# Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"



def remove_url_anchor(url):
    if '#' in url:
        cleaned_url = url.split('#')[0]
        return cleaned_url
    
    return url