print(
    sum(
        sorted([sum(map(int, items.split('\n'))) for items in
                open('input.txt').read().split('\n\n')])[-3:]
    )
)