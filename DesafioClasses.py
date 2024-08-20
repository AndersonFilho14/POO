from random import randint

#Class Emplyee will be abstract
class Emplyee:
    '''abstract class'''
    number_emplyee = 0

    def __init__(self,full_name,email,registration,wage):
        self.full_name =  full_name
        self.email = email
        self.registration = registration
        self.wage = float(wage)
        Emplyee.number_emplyee += 1

    def start_journey(self):
        '''a'''
        pass

    def finish_journey(self):
        '''a'''
        print('Ligo')
        pass 

    def receive_a_raise(self,a):
        raise NotImplementedError
    
class Dev(Emplyee):
    '''dev'''
    percente_wait = randint(1,15)
    def __init__(self, full_name, email, registration, wage,efficiency):
        super().__init__(full_name, email, registration, wage)
        self.efficiency = efficiency

    def coffe(self):
        a = randint(0,1)
        if a == 0:
            self.efficiency = 'Sua eficiencia aumentou, parabéns'
            
        else:
            self.efficiency == 'Deu problema, sua eficiencia esta baixa'
        

    def receive_a_raise(self):
        '''increase'''
        print(self.wage)
        self.wage = self.percente_wait / 100 * self.wage + self.wage
        print(self.wage)

class ProjectManager(Emplyee):
    '''Manager developer'''
    def __init__(self, full_name, email, registration, wage,programmingLinguage,coffe):
        super().__init__(full_name, email, registration, wage)
        self.programmingLinguage = programmingLinguage
        self.coffe = float(coffe)
        self.bornout = False

#o1 = Emplyee('bizonho','lari@','wheyProten',1550)
