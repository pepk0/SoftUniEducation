from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TRAIN_INCREMENT = 3

    def train(self):
        if self.speed <= 137:
            self.speed += 3
        elif self.speed < 140:
            self.speed = 140
