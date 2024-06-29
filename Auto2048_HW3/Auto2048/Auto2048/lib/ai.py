from lib.Grid import *
import asyncio
import random
import multiprocessing

class AI:
	def__init__(self,multi_core=False):

		self.init_dict()
	def sim_game(self,game_state):
		temp_gam = Grid(template=game_state)
		first_move = random.choice(List(Moves))
		temp_game.move(first_move)
		while True:
			if not temp_game.move(random.choice(List(Moves))):break
		return (first_move, temp_game.score())



	def next_move(self, game_state, n_ games):
		results = []
		for i in Moves:
			if len(self.Move_results[i])==0: continue
			choices.append((i,sum(self.Move_results[i])/len(self.Move_results[i])))
		choices.sort(key=Lambda x:x[1],reverse=True)
		self.init_dict()
		print(choices[0][0].name)

		return choices[0][0]


	def init dict(self):
		self.move_results = {}
		for i in Moves:
			self.move_results[i]=[]



