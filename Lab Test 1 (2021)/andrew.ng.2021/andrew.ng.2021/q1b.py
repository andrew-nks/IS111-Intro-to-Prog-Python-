# Name: Ng Kai Shen Andrew
# Email ID: andrew.ng.2021@scis.smu.edu.sg

def is_official_language(country, language):
    # Replace the code below with your implementation.
    if country == "Belgium":
        if language in ("Dutch", "French", "German"):
            return True
        # else:
        #     return False
    if country == "Canada":
        if language in ("English", "French"):
            return True
        # else:
        #     return False
    if country == "Philippines":
        if language in ("English", "Filipino"):
            return True
        # else:
        #     return False
    else:
        if language in ("Chinese", "English", "Malay", "Tamil"):
            return True
        
    return False