class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

    def check_equipment(self, taskL, state):
        missing_item=[]
        for item in range(len(taskL)):
            if taskL[item] not in self.weapons:
                missing_item.append(taskL[item])
                print('{}is not ready'.format(taskL[item]))
            if len(missing_item) == 0:
                print("Players status is {}, which is not allowed condition".format(state))

            if state == self.weaknesses[0]:
                print("player's status is {}, which is not allowed condition".format(state))
            else:
                print("Player is in good condition.")


player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

# Player option menu
print('There are three task you can choose.')
print('1. Task 1- climb a mountain.')
print('2. Task 2- Cook a meal.')
print('3. Task 3- Write a book.')
print('Please choose one of the following options(1-3)')

# option 1
option = input('Enter your choice (1-3)')
if option == '1':
    task =['rope', 'coat', 'first aid kit']
    not_allowed_state = 'slow'
# option 2
if option == '2':
    task = ['pan', 'groceries']
    not_allowed_state = 'small'

# option 3
if option == '3':
    task= ['pen', 'paper']
    not_allowed_state = 'confusion'


player1.check_equipment(task, not_allowed_state)
