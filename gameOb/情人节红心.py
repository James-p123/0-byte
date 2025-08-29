import time
from rich import print

def create_heart(word):
    """Generate heart-shaped ASCII art with the given word"""
    lines = []
    for y in range(12, -12, -1):
        line = []
        for x in range(-30, 30):
            # Heart equation
            if ((x*0.05)**2 + (y*0.1)**2 - 1)**3 - (x*0.05)**2 * (y*0.1)**3 <= 0:
                # Wrap around the word characters
                char = word[(x - y) % len(word)]
                line.append(char)
            else:
                line.append(' ')
        lines.append(''.join(line))
    return '\n'.join(lines)

def main():
    words = input('Please input the words you want to say!: ')
    for word in words.split():
        heart = create_heart(word)
        print(f'[bold red]{heart}[/bold red]')  # Using rich's color formatting
        time.sleep(1.5)

if __name__ == '__main__':
    main()