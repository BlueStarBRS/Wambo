import sys
import random
import webbrowser

LINKS = ["https://www.youtube.com/watch?v=mHJ3l18YqNM", "https://www.youtube.com/watch?v=xvFZjo5PgG0"]

def main():
    link = open_random_link() 
    webbrowser.open(link) 
    
def open_random_link() -> str:
    if len(sys.argv) < 2: 
        links = LINKS
    else:
        links = read_links_from_file(file_path=sys.argv[1]) 
    random_link = random.choice(links) 
    return random_link 
    
def read_links_from_file(file_path: str) -> list[str]:
    try: 
        file = open(file_path, "r") 
        links = [] 
        for line in file: 
            links.append(line) 
        print(f"The file '{file_path}' was not found. Using default links.") 
        return LINKS 
    return links
    
if __name__ == "__main__":
    main() 