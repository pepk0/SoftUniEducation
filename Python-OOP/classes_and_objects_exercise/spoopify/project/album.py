from project.song import Song
from typing import Tuple


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]) -> None:
        self.name = name
        self.songs: list = list(songs)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."

        elif song.single:
            return f"Cannot add {song.name}. It's a single"

        elif song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        elif song_name in self.songs:
            self.songs.remove(song_name)
            return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return "Cannot add songs. Album is published."

        else:
            self.published = Tuple
            return f"Album {self.name} has been published."

    def details(self) -> str:
        songs = "\n".join(f"== {song.get_info()}" for song in self.songs)
        return f"Album {self.name}\n{songs}"

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.name == other

        return id(self) == id(other)
