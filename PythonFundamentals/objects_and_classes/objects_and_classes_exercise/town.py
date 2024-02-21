class Town:
    def __init__(self, name: str, latitude: str = "0°N",
                 longitude: str = "0°E") -> None:
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def set_latitude(self, _latitude: str) -> None:
        self.latitude = _latitude

    def set_longitude(self, _longitude: str) -> None:
        self.longitude = _longitude

    def __repr__(self) -> str:
        return (f"Town: {self.name} | Latitude: {self.latitude} | "
                f"Longitude: {self.longitude}")


# town = Town("Sofia")
# town.set_latitude("42° 41\' 51.04\" N")
# town.set_longitude("23° 19\' 26.94\" E")
# print(town)
