from time import sleep
import stray.textAdventureIO as io
from stray.textAdventureClasses import *
from getpass import getpass
from random import choice, choices, randint


# Intro scene


def introScene(game: Game, skipIntro: bool = False) -> None:
    if not skipIntro:
        io.printWithTypingAnimation('It\'s the year 2143. The war between the Allied Systems and the Empire of the Suns has been raging for two years now. The Empire has been slowly but surely gaining ground, and the Allied Systems Fleet has taken heavy losses. The Allied Systems have been forced to take defensive position, defending the remaining colonies against enemy attacks at all costs.', newLines=2)
        io.printWithTypingAnimation(
            f'For a few weeks now, you have been the captain aboard the destroyer {game.playerSpaceship.name}.', newLines=0)
        io.printWithTypingAnimation(
            'You were only a cadet when you were promoted to the rank of captain. You have never fought in a real battle, heck, you have never even been on a real spaceship before. Of course, the simulations are good, but they\'re nothing compared to commanding a real ship.', newLines=2)
        io.printWithTypingAnimation(
            'You are on a routine patrol in the Elcaro system. There haven\'t been any hostilities in the area so far, but you are nervous nonetheless.', newLines=0)
        io.printWithTypingAnimation(
            'You are currently in the bridge of your ship. The bridge is a small room with a few consoles and a chair in the middle. The chair is yours. You sit down and log into the ship\'s computer.', newLines=2)
    print('---- Ship computer ----')
    game.username = input('Username: ')
    game.password = getpass()
    print('-----------------------\n')
    io.printWithTypingAnimation(
        'You check the status of the ship.', newLines=2)
    io.printProgressBar('Checking status', speed=0.5, fill='█')
    print()
    print(game.playerSpaceship)
    print()
    io.printWithTypingAnimation(
        'The ship is in perfect condition.', newLines=2)
    nextScene = False
    while not nextScene:
        match io.prompt('What do you want to do now?', ['Look around', 'Admire the ship', 'Sip coffee']):
            case 'Look around':
                game = lookAround(game)
                nextScene = choices([True, False], weights=[1, 2], k=1)[0]
                if 'lookedAtCat' in game.plotPoints:
                    nextScene = True
            case 'Admire the ship':
                admireShip(game)
            case 'Sip coffee':
                sipCoffee()
                nextScene = True
    secondScene(game)


def lookAround(game: Game) -> Game:
    choices = []
    if 'lookedAtFamilyPicture' not in game.plotPoints:
        choices.append('picture of your family')
    if 'lookedAtPlant' not in game.plotPoints:
        choices.append('plant')
    if 'lookedAtCoffeeCup' not in game.plotPoints:
        choices.append('coffee cup')
    if 'lookedAtCat' not in game.plotPoints:
        choices.append('cat')
    item = choice(choices)
    io.printWithTypingAnimation(
        'You look around the sparsely furnished room ...', newLines=0)

    if item == 'plant':
        game.plotPoints.append('lookedAtPlant')
        io.printWithTypingAnimation(
            'You see a potted plant in the corner.', newLines=0)
        io.printWithTypingAnimation(
            'It\'s a beautiful plant, but it\'s not your favorite.', newLines=0)
        io.printWithTypingAnimation(
            'You look at it for a few seconds and then turn away.', newLines=2)
    elif item == 'coffee cup':
        game.plotPoints.append('lookedAtCoffeeCup')
        io.printWithTypingAnimation(
            'You see the coffee cup on the table.', newLines=0)
        io.printWithTypingAnimation(
            'You think about taking a sip.', newLines=2)
    elif item == 'picture of your family':
        game.plotPoints.append('lookedAtFamilyPicture')
        io.printWithTypingAnimation(
            'You see a picture of your family on the wall.')
        print(
            """
      ,--.
     //^\\\\\\  ,;;;,                        .
    ((-_-))) (-_- ;                       /_\\
     )))(((   >..'.    .:.     .--.      |SSt|
    ((_._ )  /.   .|  :-_-;   /-_-))
    _))A ((_//| S ||  ,`-'.   ))-((
    `(    )`' |___|),;, C \\_/,`I ))
      \\  /    | | |`' |___(/-'|___()  ,-.
       )(     | | |   | | |   | | |  (-_-)    _____
      /__\\    |_|_|   |_|_|   |_|_|  (\\I/\\.__|A|R|T|
      `''     `-'-'   `-'-'   `-'-'  `'-`'   `o' `o'
""")
        io.printWithTypingAnimation(
            'It makes you feel sad when you think about how much you miss them and that you might never see them again.', newLines=2)
    elif item == 'cat':
        game.plotPoints.append('lookedAtCat')
        io.printWithTypingAnimation(
            'Out of the corner of your eye, you see a small red-brownish cat entering the bridge.', newLines=0)
        io.printWithTypingAnimation(
            'It looks at you with its big blue eyes and meows.', newLines=0)
        io.printWithTypingAnimation(
            'You pet the cat and it purrs. It likes you.', newLines=2)
        game.catName = io.prompt('What do you want to name you little fellow?')
        io.printWithTypingAnimation(
            f'You could spend all day petting {game.catName}. For a short moment everything seems so peaceful ...', newLines=2)
    return game


def sipCoffee() -> None:
    io.printWithTypingAnimation(
        'You reach for the coffee cup on the table next to you.', newLines=0)
    io.printWithTypingAnimation(
        'You slowly lift the cup to your mouth and take a long sip. *slurp*', newLines=2)


def admireShip(game: Game) -> None:
    """Prints the ship."""
    print(game.playerSpaceship)
    print()
    io.printWithTypingAnimation(
        'It\'s a beautiful ship. You feel proud to be her captain. But will you be able to protect her?', newLines=2)


# Second scene


def secondScene(game: Game) -> None:
    enemyCount = choices([1, 2, 3], [5, 2, 1], k=1)[0]
    game.newEnemySpaceship(enemyCount)
    io.printWithTypingAnimation(
        f'*Sirens blare* "Enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} detected!"', newLines=0)
    io.printWithTypingAnimation(
        f'You startle in your chair. What is going on? You look at the radar.', newLines=0)
    if enemyCount == 1:
        io.printWithTypingAnimation('There is one enemy ship approaching.')
    else:
        io.printWithTypingAnimation(
            f'There are {enemyCount} enemy ships approaching.')
    print()
    io.printDialogue('First Officer', 'What do we do, captain?', 'asks')
    print()
    match io.prompt('You have to decide quickly.', [f'Scan enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}', 'Attack', 'Send a distress signal', 'Retreat', 'Surrender']):
        case 'Scan enemy ship':
            scanShips(game)
            match io.prompt('Now that you know your enemy, you can make an informed decision on what to do.', ['Attack', 'Send a distress signal', 'Retreat', 'Surrender']):
                case 'Attack':
                    attack(game)
                case 'Send a distress signal':
                    game = sendDistressSignal(game)
                    match io.prompt('Unimpressed with this desperate attempt, the enemy ships close in. What now?', ['Attack', 'Retreat', 'Surrender']):
                        case 'Attack':
                            attack(game)
                        case 'Retreat':
                            retreat(game)
                        case 'Surrender':
                            surrender(game)
                case 'Retreat':
                    retreat(game)
                case 'Surrender':
                    surrender(game)
        case 'Scan enemy ships':
            scanShips(game)
            match io.prompt('Now that you know your enemy, you can make an informed decision on what to do.', ['Attack', 'Send a distress signal', 'Retreat', 'Surrender']):
                case 'Attack':
                    attack(game)
                case 'Send a distress signal':
                    game = sendDistressSignal(game)
                    match io.prompt('Unimpressed with this desperate attempt, the enemy ships close in. What now?', ['Attack', 'Retreat', 'Surrender']):
                        case 'Attack':
                            attack(game)
                        case 'Retreat':
                            retreat(game)
                        case 'Surrender':
                            surrender(game)
                case 'Retreat':
                    retreat(game)
                case 'Surrender':
                    surrender(game)
        case 'Attack':
            game.plotPoints.append('heroic')
            io.printWithTypingAnimation(
                f'You don\'t waste any time to think about what to do and attack the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}.', newLines=2)
            attack(game)
        case 'Send a distress signal':
            game = sendDistressSignal(game)
            match io.prompt('Unimpressed with this desperate attempt, the enemy ships close in. What now?', ['Scan enemy ships', 'Attack', 'Retreat', 'Surrender']):
                case 'Scan enemy ship':
                    scanShips(game)
                    match io.prompt('Now that you know your enemy, you can make an informed decision on what to do.', ['Attack', 'Retreat', 'Surrender']):
                        case 'Attack':
                            attack(game)
                        case 'Retreat':
                            retreat(game)
                        case 'Surrender':
                            surrender(game)
                case 'Scan enemy ships':
                    scanShips(game)
                    match io.prompt('Now that you know your enemy, you can make an informed decision on what to do.', ['Attack', 'Retreat', 'Surrender']):
                        case 'Attack':
                            attack(game)
                        case 'Retreat':
                            retreat(game)
                        case 'Surrender':
                            surrender(game)
                case 'Attack':
                    attack(game)
                case 'Retreat':
                    retreat(game)
                case 'Surrender':
                    surrender(game)
        case 'Retreat':
            game.plotPoints.append('coward')
            retreat(game)
        case 'Surrender':
            surrender(game)


def scanShips(game: Game) -> None:
    io.printWithTypingAnimation(
        f'You instruct the Science Officer to scan the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}.', newLines=2)
    io.printProgressBar(
        f'Scanning enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}', fill='█')
    for enemySpaceships in game.enemySpaceships:
        print()
        print(enemySpaceships)
    print()


def sendDistressSignal(game: Game) -> Game:
    game.plotPoints.append('distressSignalSent')
    io.printWithTypingAnimation(
        'You instruct the Communications Officer to send a distress signal. Hopefully, someone will come to your aid.', newLines=2)
    return game


# Third scene


def attack(game: Game) -> None:
    while len(game.enemySpaceships) > 0:
        # Player attack
        nameOfWeapon = io.prompt(
            'What weapon do you want to use?', game.playerSpaceship.weapons)
        if len(game.enemySpaceships) == 1:
            targetShip = game.enemySpaceships[0]
        else:
            nameOfShipToAttack = io.prompt('Which ship do you want to attack?', [
                enemySpaceship.name for enemySpaceship in game.enemySpaceships])
            targetShip = next(
                enemySpaceship for enemySpaceship in game.enemySpaceships if enemySpaceship.name == nameOfShipToAttack)

        targetShip.hull -= io.printFireWeapon(
            game.playerSpaceship, targetShip, weaponDict[nameOfWeapon])

        if targetShip.hull <= 0:
            game = enemyShipDefeated(game, targetShip)

        # Enemy attack
        for enemySpaceship in game.enemySpaceships:
            damage = io.printFireWeapon(
                enemySpaceship, game.playerSpaceship, weaponDict[choice(enemySpaceship.weapons)])
            game.playerSpaceship.hull -= damage

            if damage:
                if game.playerSpaceship.hull <= 0:
                    shipExplodesEnding(game)

                if game.playerSpaceship.hull <= 0.7 * MAX_PLAYERSHIP_HEALTH and game.playerSpaceship.hull > 0.4 * MAX_PLAYERSHIP_HEALTH and 'hullIntegrityBelow70' not in game.plotPoints:
                    io.printDialogue(
                        'Second Officer', f'Our front shields are crumbling. Hull integrity at {round(game.playerSpaceship.hull / MAX_PLAYERSHIP_HEALTH * 100)}%.', 'says')
                    game.plotPoints.append('hullIntegrityBelow70')
                    print()

                if game.playerSpaceship.hull <= 0.4 * MAX_PLAYERSHIP_HEALTH and game.playerSpaceship.hull > 0.25 * MAX_PLAYERSHIP_HEALTH and 'hullIntegrityBelow40' not in game.plotPoints:
                    io.printDialogue(
                        'Second Officer', f'We\'re taking heavy fire! Hull integrity at {round(game.playerSpaceship.hull / MAX_PLAYERSHIP_HEALTH * 100)}%.', 'says')
                    game.plotPoints.append('hullIntegrityBelow40')
                    print()

                if game.playerSpaceship.hull <= 0.25 * MAX_PLAYERSHIP_HEALTH:
                    io.printDialogue('Second Officer',
                                     f'Hull integrity at {round(game.playerSpaceship.hull / MAX_PLAYERSHIP_HEALTH * 100)}%. The reactor is destabilizing!', 'shouts')
                    io.printDialogue('Tactics Commander',
                                     'We need to retreat NOW!', 'shouts')
                    io.printDialogue(
                        'First Officer', 'No! We have to fight until the end!', 'exclaims')
                    print()
                    if io.prompt('You will have to decide.', ['Retreat', 'Continue Attack']) == 'Retreat':
                        retreat(game)
                    else:
                        game.plotPoints.append('fightToTheDeath')

        if 'distressSignalSent' in game.plotPoints and choices([True, False], [0.1, 0.9], k=1)[0]:
            helpArrivesEnding(game)
    enemyDestroyedEnding(game)


def enemyShipDefeated(game: Game, targetShip: Spacecraft) -> Game:
    defeat = choice(['is obliterated as it\'s reactor overheats and violently explodes',
                    'can\'t withstand the structural damage and breaks apart', 'is rendered inoperable as the command bridge is destroyed'])
    io.printWithTypingAnimation(f'The enemy ship {defeat}.', newLines=2)
    game.enemySpaceships.remove(targetShip)
    return game


def retreat(game: Game) -> None:
    io.printWithTypingAnimation(
        'Knowing that you cannot win and fearing for your life, you decide to retreat.', newLines=2)
    io.printDialogue(
        'First Officer', 'What are you doing, captain? We can\'t just run away!', 'asks')
    print()
    match io.prompt('What do you answer?', ['I\'m sorry, but I have to do this.', 'You\'re right. We can\'t run away.']):
        case 'I\'m sorry, but I have to do this.':
            io.printDialogue(
                'You', 'I\'m sorry, but I have to do this.', 'say')
            io.printDialogue(
                'You', 'All power to the engines and rear shields. We\'re retreating. That is an order!', 'command')
            io.printDialogue(
                'First Officer', 'But captain, that will leave the colonies defenseless!', 'exclaims')
            io.printDialogue(
                'You', 'Then so be it. I won\'t risk the lives of my crew to fight a losing battle.', 'answer')
            print()
            io.printWithTypingAnimation(
                f'The engines roar to life and the ship starts to move away from the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}.', newLines=2)

            fastestEnemySpacecraft = max(
                game.enemySpaceships, key=lambda enemySpaceship: enemySpaceship.speed)

            canCatchUp = choices([True, False], [
                                 fastestEnemySpacecraft.speed, game.playerSpaceship.speed * 1.3], k=1)[0]

            if canCatchUp:
                io.printWithTypingAnimation(
                    f'But what is this? The radar shows the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} firing their engines and closing in on you.', newLines=0)
                io.printWithTypingAnimation(
                    'A feeling of dread fills your stomach.', newLines=0)
                io.printWithTypingAnimation(
                    f'The enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} {"catches" if len(game.enemySpaceships) == 1 else "catch"} up to you and {"starts" if len(game.enemySpaceships) == 1 else "start"} attacking.', newLines=2)
                attackingShip = choice(game.enemySpaceships)
                game.playerSpaceship.hull -= io.printFireWeapon(
                    attackingShip, game.playerSpaceship, weaponDict[choice(attackingShip.weapons)])
                if game.playerSpaceship.hull <= 0:
                    shipExplodesEnding(game)
                if 'distressSignalSent' in game.plotPoints and choices([True, False], [0.4, 0.6], k=1)[0]:
                    helpArrivesEnding(game)
                io.printWithTypingAnimation(
                    'You don\'t have a choice. You are forced to surrender.', newLines=2)
                finalSurrender(game)
            else:
                retreatEnding(game)
        case 'You\'re right. We can\'t run away.':
            if 'coward' in game.plotPoints:
                game.plotPoints.remove('coward')
            io.printDialogue(
                'You', 'You\'re right. We can\'t run away.', 'agree')
            io.printDialogue(
                'You', 'Everybody on your stations! We\'re fighting!', 'command')
            print()
            io.printWithTypingAnimation(
                'You bring your ship into position and give the order to fire', newLines=2)
            attack(game)


def surrender(game: Game) -> None:
    io.printWithTypingAnimation(
        'This is too much for you. You know you don\'t stand a chance against the enemy, so you decide to surrender.', newLines=2)
    surrenderInTime = choice([True, False])
    if surrenderInTime:
        prisonerEnding(game)
    else:
        io.printWithTypingAnimation(
            f'You\'r about to hail the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} but they have already opened fire.')
        print()
        attackingShip = choice(game.enemySpaceships)
        game.playerSpaceship.hull -= io.printFireWeapon(
            attackingShip, game.playerSpaceship, weaponDict[choice(attackingShip.weapons)])
        if game.playerSpaceship.hull <= 0:
            shipExplodesEnding(game)
        io.printWithTypingAnimation(
            'The whole ship shakes violently. You are thrown out of your chair.', newLines=0)
        io.printWithTypingAnimation(
            'You lie on the floor dazed and bleeding.', newLines=2)
        options = ['Attack', 'Retreat']
        if 'distressSignalSent' not in game.plotPoints:
            options += ['Send a distress signal']
        match io.prompt('You are desperate. You have to do something.', options):
            case 'Attack':
                io.printWithTypingAnimation(
                    'You didn\'t want to do this, but you have no choice.')
                attack(game)
            case 'Retreat':
                retreat(game)
            case 'Send a distress signal':
                sendDistressSignal(game)
                match io.prompt('You doubt that anyone will come to help you. You will have to do something anyway.', ['Attack', 'Retreat']):
                    case 'Attack':
                        attack(game)
                    case 'Retreat':
                        retreat(game)


def finalSurrender(game: Game) -> None:
    surrenderInTime = choice([True, False])
    if surrenderInTime:
        prisonerEnding(game)
    else:
        io.printWithTypingAnimation(
            f'You\'r about to hail the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} but then ...', newLines=2)
        while game.playerSpaceship.hull > 0:
            attackingShip = choice(game.enemySpaceships)
            game.playerSpaceship.hull -= io.printFireWeapon(
                attackingShip, game.playerSpaceship, weaponDict[choice(attackingShip.weapons)])
        shipExplodesEnding(game)


# Endings


def helpArrivesEnding(game: Game) -> None:
    io.printWithTypingAnimation(
        'Suddenly your ship sensors show two unknown signals leaving warp right behind you.', newLines=2)
    print(friendlyHeavyCruiser1)
    print()
    print(friendlyHeavyCruiser2)
    print()
    io.printWithTypingAnimation(
        'You look out of the window ... It\'s two allied heavy cruisers. You are saved!', newLines=0)
    io.printWithTypingAnimation(
        'The two massive warships make short work of the remaining enemy forces.', newLines=2)
    io.printWithTypingAnimation(
        'You are hailed by the captain of one of the cruisers.', newLines=2)
    io.printDialogue(
        'Captain', f'Well done, captain {game.username}. Today you saved countless lives.')
    io.printDialogue('You', 'We wouldn\'t have made it without you', 'reply')
    io.printDialogue(
        'Captain', 'You\'re welcome. Now let\'s get your ship to the nearest station, you look like you could need some repairs', 'says')
    io.printDialogue(
        'You', f'I suppose you\'ve got a point there ... {game.playerSpaceship.name} out.', 'reply')
    print()
    io.printWithTypingAnimation('The end.')
    exit()


def enemyDestroyedEnding(game: Game) -> None:
    io.printWithTypingAnimation(
        'It\'s finally over. You successfully fought off the enemy intruders.', newLines=2)

    if 'distressSignalSent' in game.plotPoints:
        io.printWithTypingAnimation(
            'The distress signal you sent earlier has been received by the fleet.', newLines=0)
        io.printWithTypingAnimation(
            'They are on their way to help you.', newLines=2)

    if 'lookedAtFamilyPicture' in game.plotPoints:
        io.printWithTypingAnimation(
            'As you let your gaze wander you notice the picture of your family is missing.', newLines=0)
        io.printWithTypingAnimation(
            'You look around and find it shattered on the floor.', newLines=0)
        io.printWithTypingAnimation(
            'You take the photo from the broken frame and put it in your pocket.', newLines=2)
    elif 'lookedAtCat' in game.plotPoints:
        io.printWithTypingAnimation(
            'Just as peace returns to the ship, you hear a meow. It\'s {game.catName}. He jumps into your lap and purrs as you gently pet him.', newLines=2)
    elif 'lookedAtPlant' in game.plotPoints:
        io.printWithTypingAnimation(
            'Relieved you look around the bridge, in the corner you see the remains of a plant pot and next to it the uprooted plant. The heavy shaking of the ship has caused it to fall over. You pick up the small plant, maybe it is your favorite plant after all.', newLines=2)

    if 'distressSignalSent' in game.plotPoints:
        io.printWithTypingAnimation(
            'Finally the fleet arrives. You can now return home.', newLines=2)

    if 'fightToTheDeath' in game.plotPoints or 'heroic' in game.plotPoints:
        io.printWithTypingAnimation(
            'When you reach your home planet you are greeted by a hero\'s welcome.', newLines=0)
        io.printWithTypingAnimation(
            'You are awarded the highest honors for your actions. Your bravery and courage will be remembered for generations to come.', newLines=2)

    io.printWithTypingAnimation('The end.')
    exit()


def prisonerEnding(game: Game) -> None:
    io.printDialogue(
        'You', f'Hail the enemy ship {"ship" if len(game.enemySpaceships) == 1 else "ships"}. We surrender.', 'instruct')
    print()
    io.printWithTypingAnimation(
        f'Your first officer looks at you in disbelief, but he does as you say. He sends a message to the enemy ship {"ship" if len(game.enemySpaceships) == 1 else "ships"}.', newLines=0)
    io.printWithTypingAnimation(
        'The enemies board your ship and take you and your crew prisoner.', newLines=0)
    io.printWithTypingAnimation(
        'It\'s not the end you had hoped for, but at least you\'re alive.', newLines=2)
    io.printWithTypingAnimation('The end.')
    exit()


def retreatEnding(game: Game) -> None:
    io.printWithTypingAnimation(
        f'It\'s close but you are able to outrun the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}.', newLines=0)
    io.printWithTypingAnimation(
        'As soon as you are out of range, you jump to the nearest allied system to report the attack but until then the colonies are defenseless prey.', newLines=0)
    io.printWithTypingAnimation(
        'Many civilians will die onslaught that follows your retreat.', newLines=2)
    if 'coward' in game.plotPoints:
        io.printWithTypingAnimation(
            'you managed to escape, you will pay for this cowardice.', newLines=0)
        io.printWithTypingAnimation(
            'Upon arriving at the allied system, you are dishonorably discharged from the military and stripped of your rank.', newLines=0)
        io.printWithTypingAnimation(
            'You might have saved your own life, but the guilt of letting so many people die will haunt you for the rest of your life.', newLines=2)
    io.printWithTypingAnimation('The end.')
    exit()


def shipExplodesEnding(game: Game) -> None:
    io.printWithTypingAnimation(
        'It\'s over. The damage inflicted on your ship is too severe. You take a last breath, then the ship\'s reactor explodes ...', newLines=0)
    sleep(3)
    io.printWithTypingAnimation(
        'The deafening shockwave is followed by a fireball obliterating everything in it\'s way. You and your crew are already dead when the shockwave breaches the inner hull, shattering the ship into pieces. The pitiful remains of your beloved ship float through space as the enemy sets course for the now unprotected colonies.', newLines=2)

    if 'heroic' in game.plotPoints:
        io.printWithTypingAnimation(
            'You might have died, but your fearless actions will be remembered for generations to come. You were the sort of brave captain that will lead the Allied Systems Fleet to victory.', newLines=2)
    elif 'lookedAtFamilyPicture' in game.plotPoints:
        io.printWithTypingAnimation(
            'When you family hears about your death a few days later, they are devastated. Your wife can\'t stop crying and your children are inconsolable. You will be missed.', newLines=2)

    io.printWithTypingAnimation('The end.')
    exit()
