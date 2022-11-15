from stray.textAdventureClasses import *
import stray.textAdventureGameLogic as gameLogic
import stray.textAdventureIO as io


game = Game()


print('')
io.tprint(game.playerSpaceship.name, font='small')
io.speak(game.playerSpaceship.name, printError=True)
skipIntro = io.prompt('Skip intro?: ', ['Yes', 'No']) == 'Yes'
gameLogic.introScene(game, skipIntro)
