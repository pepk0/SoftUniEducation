from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAIN_INCREMENT = 2

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        elif self.speed < 120:
            self.speed = 120
