from mycroft import MycroftSkill, intent_file_handler, intent_handler, \
                    AdaptIntent
from mycroft.util.log import LOG
from datetime import datetime
from sportsreference.mlb.boxscore import Boxscores

games_today = Boxscores(datetime.today())
items = games_today.games.values()

class SportsSkill(MycroftSkill):

	# The constructor of the skill, which calls MycroftSkill's constructor
	def __init__(self):
		super(SportsSkill, self).__init__(name="SportsSkill")
			

	@intent_file_handler('TellMe.intent')
	def tell_todays_games(self, message):
		if items:
			for item in items:
				# numberOfGamesText = 'There are %s games today.'%(len(item))
				numberOfGames = len(item)
				games = item
				self.speak_dialog('NumberOfGames', {numberOfGames: numberOfGames})

			for game in games:
				# matchesText = 'The %s play against the %s' %(game["home_name"], game["away_name"])
				self.speak_dialog('', {
					'homeTeam': game['home_name'], 
					'awayTeam': game['away_name']
					}
				)
		else:
			self.speak_dialog('NoGames')
			self.log.info('no games where found or the items was undefined for the games')

	# The "stop" method defines what Mycroft does when told to stop during
	# the skill's execution. In this case, since the skill's functionality
	# is extremely simple, there is no need to override it.  If you DO
	# need to implement stop, you should return True to indicate you handled
	# it.
	#
	def stop(self):
		self.log.info('stop has been called')
		return True

def create_skill():
	return SportsSkill()
