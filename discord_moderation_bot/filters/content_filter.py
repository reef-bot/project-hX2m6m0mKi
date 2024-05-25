# content_filter.py

import re

class ContentFilter:
    def __init__(self):
        self.blacklist = []
    
    def load_blacklist(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.blacklist = [line.strip() for line in file]
        except FileNotFoundError:
            print("Blacklist file not found.")
    
    def add_to_blacklist(self, word):
        if word not in self.blacklist:
            self.blacklist.append(word)
    
    def remove_from_blacklist(self, word):
        if word in self.blacklist:
            self.blacklist.remove(word)
    
    def filter_content(self, content):
        filtered_content = content
        for word in self.blacklist:
            filtered_content = re.sub(r'\b' + re.escape(word) + r'\b', '[censored]', filtered_content, flags=re.IGNORECASE)
        return filtered_content

# End of content_filter.py