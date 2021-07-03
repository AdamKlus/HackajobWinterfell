class Solution:

	def SevenKingdomAttack(self, no_of_infantry, no_of_dragons, no_of_walkers, no_of_white_lords):

		ww_defence = (no_of_walkers * 3) + (no_of_white_lords * 100)
		sk_attack = (no_of_infantry * 2) + (no_of_dragons * 600)

		if ww_defence - sk_attack <= 0: #all killed
			no_of_walkers = 0
			no_of_white_lords = 0

		else: #we kill white lords first
			if sk_attack > no_of_white_lords*100:
				no_of_walkers = no_of_walkers - int((sk_attack-no_of_white_lords*100)/3)
				no_of_white_lords = 0
			else:
				no_of_white_lords = no_of_white_lords - int((sk_attack)/100)
			
		return no_of_white_lords, no_of_walkers

	def WhiteWalkersAttack(self, no_of_infantry, no_of_dragons, no_of_walkers, no_of_white_lords):

		sk_defence = (no_of_infantry * 2) + (no_of_dragons * 600)
		ww_attack = (no_of_walkers * 1) + (no_of_white_lords * 50)

		if sk_defence - ww_attack <= 0: #all killed
			no_of_infantry = 0
			no_of_dragons = 0

		else:
			if no_of_infantry > 0: #we kill infantry first
				if ww_attack > no_of_infantry*2:
					no_of_dragons = no_of_dragons - int((ww_attack-no_of_infantry*2)/600) 
					no_of_infantry = 0
				else:
					no_of_infantry = no_of_infantry - int((ww_attack)/2)

			else:
				no_of_dragons = no_of_dragons - int((ww_attack)/600)
			
		return no_of_dragons, no_of_infantry

	def run(self, first_strike_army_name, no_of_dragons, no_of_white_lords):

		result = None

		no_of_infantry = 5000
		no_of_walkers = 10000

		if type(no_of_dragons) == int and no_of_dragons > 0 and type(no_of_white_lords) == int and no_of_white_lords > 0:

			if first_strike_army_name == "Seven Kingdom Army":

				turn = 1

				while True:

					no_of_white_lords, no_of_walkers = self.SevenKingdomAttack(no_of_infantry, no_of_dragons, no_of_walkers, no_of_white_lords)

					if no_of_walkers < 1 and no_of_white_lords < 1:
						result = "Seven Kingdom Army|" + str(turn)
						break

					turn = turn + 1
					
					no_of_dragons, no_of_infantry = self.WhiteWalkersAttack(no_of_infantry, no_of_dragons, no_of_walkers, no_of_white_lords)
					
					if no_of_dragons < 1 and no_of_infantry < 1:
						result = "White Walker Army|" + str(turn)
						break
					
					turn = turn + 1					
					
			elif first_strike_army_name == "White Walker Army":

				turn = 1

				while True:

					no_of_dragons, no_of_infantry = self.WhiteWalkersAttack(no_of_infantry, no_of_dragons, no_of_walkers, no_of_white_lords)
					
					if no_of_dragons < 1 and no_of_infantry < 1:
						result = "White Walker Army|" + str(turn)
						break

					turn = turn + 1

					no_of_white_lords, no_of_walkers = self.SevenKingdomAttack(no_of_infantry, no_of_dragons, no_of_walkers, no_of_white_lords)

					if no_of_walkers < 1 and no_of_white_lords < 1:
						result = "Seven Kingdom Army|" + str(turn)
						break

					turn = turn + 1
				
			else:
				result = "Invalid parameter provided"
		else:
			result = "Invalid parameter provided"
					
		return result

a = Solution()
print(a.run("Seven Kingdom Army",2,1))