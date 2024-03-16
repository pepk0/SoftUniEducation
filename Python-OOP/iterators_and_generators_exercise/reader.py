def read_next(*collections: tuple):
    for collection in collections:
        for char in collection:
            yield char
