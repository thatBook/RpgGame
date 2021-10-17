import json

def inventory():
	f = open('inv.json', 'w')
	print(f)

def game():
	answer= input('		Welcome to *GAME*, do you want to start?(y/n)')

	if answer.lower()=='y':
		print('')
		print('		Welcome.')
		print('')
		start=True
		inventory()
	else:
		print('		Ok then.')
	
	if start==True:
		print('		I feel a flash of light and have the sense of being transported somewhere...')
		print('		...')
		print('		...')
		print("		As I open my eyes and take in my surroundings, I realise I'm not tucked up in bed anymore.")
		choice=input('		There is a large victorian manor to my right, and a lond winding path to my left.(l/r)')

		if choice.lower()=='l':
			choiceY1=True
			print('		I start walking along the path, and after about 30 minutes I see a large spider running towards me. I beat at the monster until it is dead an-')
			print('		§§§-- Would you like to loot *Large Lesser Spider*. --§§§ ')
			print('		What? Uhh.. Yes?')
			print('		§§§-- You have received *Spiders Cloak* --§§§')
			inventory.append('Spiders Cloak')
		else:
			choiceY1=False
			print("		As I enter the manor, a strange creeping feeling overcomes me, but, I push forward, as it's the only thing I can do. I turn a corner and feel a sharp pain in my head before blacking out...")
			print('		I blearily come to, and notice three other people in the room with me.')
			print("		'Hey' one man says 'You're finally awake.'")


game()

