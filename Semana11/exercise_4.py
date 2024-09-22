class Head:
    def __init__(self, eyes, ears, nose, mouth, hair, forehead, cheeks):
        self.eyes=eyes
        self.ears=ears
        self.nose=nose
        self.mouth=mouth
        self.hair=hair
        self.forehead=forehead
        self.cheeks=cheeks

    def print_head(self):
        print(f"The parts of the head are: {self.eyes, self.ears, self.nose, self.mouth, self.hair, self.forehead, self.cheeks}")

class Torso:
    def __init__(self, head, right_arm, left_arm, chest, abdomen, hip):
        self.head=head
        self.right_arm=right_arm
        self.left_arm=left_arm
        self.chest=chest
        self.abdomen=abdomen
        self.hip=hip

    def print_torso(self):
        print(f"The parts of the torso are: head, right_arm, left_arm, {self.chest, self.abdomen, self.hip}")

class Arm:
    def __init__(self, hand, elbow, wrist, shoulder):
        self.hand=hand
        self.elbow=elbow
        self.wrist=wrist
        self.shoulder=shoulder

    def print_arm(self):
        print(f"The parts of the arm are: {self.hand, self.elbow, self.wrist, self.shoulder}")

class Hand:
    def __init__(self, nails, fingers, palm):
        self.nails=nails
        self.fingers=fingers
        self.palm=palm

    def print_hand(self):
        print(f"The parts of the hand are: {self.nails, self.fingers, self.palm}")

class Leg:
    def __init__(self, foot, knee, thigh, shin, calf, ankle):
        self.knee=knee
        self.thigh=thigh
        self.shin=shin
        self.calf=calf
        self.ankle=ankle
        self.foot=foot

    def print_leg(self):
        print(f"The parts of the leg are: {self.knee, self.thigh, self.shin, self.calf, self.ankle, self.foot}")

class Feet:
    def __init__(self, instep, heel, sole, toes, nails):
        self.instep=instep
        self.heel=heel
        self.sole=sole
        self.toes=toes
        self.nails=nails

    def print_feet(self):
        print(f"The parts of the foot are: {self.instep, self.heel, self.sole, self.toes, self.nails}")

class Human:
    def __init__(self, head, torso, left_arm, right_arm, left_leg, right_leg):
        self.head=head
        self.torso=torso
        self.left_arm=left_arm
        self.right_arm=right_arm
        self.left_leg=left_leg
        self.right_leg=right_leg

    def print_body(self):
        print(f"The human body has: {self.head, self.torso, self.left_arm, self.right_arm, self.left_leg, self.right_leg}")


right_hand=Hand("nails", "fingers", "palm")
left_hand=Hand("nails", "fingers", "palm")
#-----------------------------------------------
right_arm=Arm(right_hand, "elbow", "wrist", "shoulder")
left_arm=Arm(left_hand, "elbow", "wrist", "shoulder")
#-----------------------------------------------
right_foot=Feet("instep", "heel", "sole", "toes", "nails")
left_foot=Feet("instep", "heel", "sole", "toes", "nails")
#-----------------------------------------------
right_leg=Leg(right_foot, "knee", "thigh", "shin", "calf", "ankle")
left_leg=Leg(left_foot, "knee", "thigh", "shin", "calf", "ankle")
#-----------------------------------------------
head=Head("eyes", "ears", "nose", "mouth", "hair", "forehead", "cheeks")
torso=Torso(head, right_arm, left_arm, "chest", "abdomen", "hip")
human_body=Human(head, torso, left_arm, right_arm, left_leg, right_leg )


head.print_head()

right_hand.print_hand()

left_arm.print_arm()

right_leg.print_leg()

left_foot.print_feet()

human_body.print_body()
