from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: list = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        if photos_count > 4:
            photos_count = ceil(photos_count / 4)
        return cls(photos_count)

    def add_photo(self, label: str) -> str:
        page = 1
        slot = 0

        for idx in range(len(self.photos)):
            if len(self.photos[idx]) < 4:
                self.photos[idx].append(label)
                page += idx
                slot += len(self.photos[idx])
                return (f"{label} photo added successfully "
                        f"on page {page} slot {slot}")

        return "No more free slots"

    def display(self) -> str:
        sep_line = "-" * 11
        display_string = sep_line + "\n"

        for page in self.photos:
            display_string += ("[] " * len(page)).rstrip() + "\n"
            display_string += sep_line + "\n"

        return display_string

