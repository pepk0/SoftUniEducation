from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str) -> None:
        self.name = name
        self.albums: list = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return (f"Band {self.name} already has "
                    f"{album.name} in their library.")

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:

        if album_name in self.albums:
            album = self.albums[self.albums.index(album_name)]

            if album.published:
                return "Album has been published. It cannot be removed."

            self.albums.remove(album_name)
            return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self) -> str:
        albums = "\n".join(album.details() for album in self.albums)
        return f"Band {self.name}\n{albums}"


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
