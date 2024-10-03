# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class Employee:
    def __init__(self, name):
        self.name=name

    def work(self):
        print(f"The employee {self.name} is working.")

class Manager(Employee):
    def manage(self):
        print(f"{self.name} is making reports.")

class ContentCreators(Employee):
    def creating(self):
        print(f"{self.name} is working on policy articles.")

class QualityAnalyst(Employee):
    def auditing(self):
        print(f"{self.name} is auditing the tasks and contacts of the advisors.")

class SrAdvisor(Employee) :
    def working(self):
        print(f"{self.name} is taking escalation from the Advisors.")

class Trainer(Manager, ContentCreators, QualityAnalyst, SrAdvisor):  #multiple inheritance
    def training(self):
        print(f"{self.name} is training new hires and tenure employees")


Manager=Manager("Peter")
Content_Creator=ContentCreators("Alissa")
QA=QualityAnalyst("Tony")
SrAdvisor=SrAdvisor("LaRhonda")
Trainer=Trainer("Thomas")

Manager.manage()
Content_Creator.creating()
QA.auditing()
SrAdvisor.working()

#multiple inheritance
Trainer.training()
Trainer.manage()
Trainer.creating()
Trainer.auditing()
Trainer.working()