class Weapon:
    def __init__(self, bullets: int) -> None:
        self.bullets = bullets

    def shoot(self) -> str:
        if self.bullets:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self) -> str:
        return f"Remaining bullets: {self.bullets}"

# tests
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
