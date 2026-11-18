def greet(name: str) -> str:
    return f'Welcome, {name}!'
def main():
    for person in ['Aina', 'Ben']:
        print(greet(person))
if __name__ == '__main__':
    main()

