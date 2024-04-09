def read_next(*collections: tuple):
    for collection in collections:
        # for element in collection:
        #   yield element
        yield from collection  # can be a short form for a second loop
