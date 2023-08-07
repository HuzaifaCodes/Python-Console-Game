import time


class Character:
    def __init__(self, name, hp, ap, dp, sp, mp, image, job_class):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.ap = ap
        self.dp = dp
        self.sp = sp
        self.mp = mp
        self.image = image
        self.job_class = job_class
        self.defend_turns = 0

    def attack(self, target):
        damage = self.ap - target.dp
        if damage > 0:
            target.take_damage(damage)

    def defend(self):
        self.dp *= 1.5
        self.defend_turns = 1

    def use_skill(self, skill, target):
        if self.job_class == "Defender":
            if skill == "Heal":
                self.heal()
            elif skill == "Thunder Miracle":
                self.thunder_miracle(target)
            else:
                print("Invalid skill.")
        elif self.job_class == "Warrior":
            if skill == "Angel Hand":
                self.angel_hand(target)
            elif skill == "Helping Hand":
                self.helping_hand(target)
            elif skill == "Overtake":
                self.overtake(target)
            else:
                print("Invalid skill.")
        else:
            print("Invalid job class.")

    def heal(self):
        if self.mp >= 20:
            healed_amount = int(self.max_hp * 0.2)  # Restores 20% of maximum HP
            self.hp = min(self.hp + healed_amount, self.max_hp)
            print(f"{self.name} healed for {healed_amount} HP.")
            self.mp-=20

    def thunder_miracle(self, target):
        if self.mp >= 20:
            damage = self.ap - target.dp * 2
            target.take_damage(damage)
            self.dp *= 1.2
            self.mp -= 20
            print(f"{self.name} used Thunder Miracle on {target.name}!")

    def angel_hand(self, target):
        if self.mp >= 20:
            damage = self.ap - target.dp * 2
            target.take_damage(damage)
            self.hp += 5
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.mp -= 20
            print(f"{self.name} used Angel Hand on {target.name}!")

    def helping_hand(self, target):
        if self.mp >= 20:
            damage = self.ap - target.dp
            target.take_damage(damage)
            self.heal()
            self.mp -= 20
            print(f"{self.name} used Helping Hand on {target.name}!")

    def overtake(self, target):
        if self.mp >= 20:
            damage = -(self.ap - target.dp * 2.5)
            target.take_damage(damage)
            self.sp += 5
            self.mp -= 25
            print(f"{self.name} used Overtake on {target.name}!")

    def take_damage(self, damage):
        if self.defend_turns > 0:
            damage = max(damage - self.dp, 0)
            self.defend_turns = 0  # Reset defend turns after taking damage
        self.hp = max(0, self.hp - damage)
        print(f"{self.name} took {damage} damage.")