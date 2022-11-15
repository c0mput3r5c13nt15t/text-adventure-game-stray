import os
from random import choice
from stray.textAdventureClasses import Spacecraft, Weapon
from gtts import gTTS
from progress.bar import Bar
import time
from art import tprint
from threading import Thread
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


colorsForRegex: list[tuple[str, str]] = [
    ("Stray", bcolors.WARNING),
    # ("you'[a-z]\b", bcolors.WARNING),
    # ("you(r(s)?)?", bcolors.WARNING),
    ("Allied Systems", bcolors.OKGREEN),
    ("Empire( of the Suns)?", bcolors.FAIL),
    ("\\*Sirens blare\\*", bcolors.FAIL),
    ("enemy( ship(s)?)?( intruders)?", bcolors.FAIL),
    ("Elcaro system", bcolors.HEADER),
    ("\\d* damage", bcolors.FAIL),
    ("Aqua|Cobra|Stinger|Spike|Nimbus|Tsar|Shockwave|Vortex|Phazek|Tilde|Pling|Hyperion|Nexus", bcolors.FAIL),
    ("Aurora|Muinnellim", bcolors.OKGREEN),
    ("Small Laser Turret|Missile Launcher|Railgun|Torpedo Launcher|Artillery Cannon|Plasma Beam|Gatling Gun|missile bays|torpedo bays", bcolors.OKBLUE),
    ("Invalid choice", bcolors.FAIL),
    ("First Officer|Second Officer|Science Officer|Tactics Commander", bcolors.OKCYAN),
    ("plant", bcolors.OKGREEN),
    ("The end.", bcolors.BOLD),
    ("Hull integrity at \\d*%", bcolors.FAIL),
]


def colorText(text: str) -> str:
    # Prefix "You" with color
    for string in colorsForRegex:
        text = re.sub(string[0], string[1] + r'\g<0>' +
                      bcolors.ENDC, text, flags=re.IGNORECASE)
    return text


def speak(text, printError=False):
    try:
        currentPath = os.path.dirname(os.path.abspath(__file__))
        tts = gTTS(text=text, lang='en')

        filename = f"{currentPath}/tmp-audio-{str(time.time())}.mp3"
        tts.save(filename)
        value = os.system("play \"" + filename + "\" -q -t alsa 2>/dev/null")
        if value != 0 and printError:
            print(
                f"Error: Could not play audio. Probably missing the 'play' command. The game will continue without audio.", end='\n\n')
        os.remove(filename)
    except Exception as e:
        if printError:
            print(
                f"Error: {e}", end='\n\n')


def makeStringSpecificLength(string: str, length: int, fill: str = ' ') -> str:
    return string + fill * (length - len(string))


def printWithTypingAnimation(text: str, speed: float = 0.05, newLines=1) -> None:
    thread = Thread(target=speak, args=(text,))
    thread.start()
    text = colorText(text)
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed)
    thread.join()
    print(' ', end='')
    print('\n' * newLines, end='')


def printDialogue(character: str, text: str, verb: str = "says") -> None:
    printWithTypingAnimation(f'{character} {verb}:', newLines=0)
    printWithTypingAnimation('"' + text + '"')


def printFireWeapon(attackingShip: Spacecraft, targetShip: Spacecraft, weapon: Weapon) -> int:
    damage, projectilesHitting = weapon.fire()
    match weapon.name:
        case "Small Laser Turret":
            printWithTypingAnimation(
                f'{attackingShip.name} uses it\'s {weapon.name} to fire {weapon.projectilesPerShot} lasers at {targetShip.name}!', newLines=0)
            if damage:
                printWithTypingAnimation(
                    f'{projectilesHitting} {"laser hits" if projectilesHitting == 1 else "lasers hit"}, penetrating the hull and dealing {damage} damage!')
            else:
                printWithTypingAnimation(f'All lasers miss!')
        case "Missile Launcher":
            printWithTypingAnimation(
                f'{attackingShip.name} opens it\'s missile bays, firing {weapon.projectilesPerShot} missiles at {targetShip.name}!', newLines=0)
            if damage:
                printWithTypingAnimation(
                    f'The missiles swirl towards the ship, {weapon.projectilesPerShot - projectilesHitting} {"missile is picked up" if weapon.projectilesPerShot - projectilesHitting == 1 else "missiles are picked up"} by the point defense system. The remaining {"missile gets" if projectilesHitting == 1 else "missiles get"} through and explode dealing {damage} damage.')
            else:
                printWithTypingAnimation(
                    'Just as the missiles are about to hit, the point defense system kicks in and destroys all of them!')
        case "Railgun":
            # Railgun can only have one projectile per shot
            printWithTypingAnimation(
                f'{attackingShip.name} fires it\'s {weapon.name} at {targetShip.name}!', newLines=0)
            if damage:
                printWithTypingAnimation(
                    f'The projectile flies through space and hits, penetrating deep into the ships hull and dealing {damage} damage!')
            else:
                printWithTypingAnimation(
                    f'Just as the railgun is about to fire, the gun jams failing to fire!')
        case "Torpedo Launcher":
            printWithTypingAnimation(
                f'{attackingShip.name} opens it\'s torpedo bays, firing {weapon.projectilesPerShot} torpedoes at {targetShip.name}!', newLines=0)
            if damage:
                printWithTypingAnimation(
                    f'The torpedoes rumble towards the ship, {weapon.projectilesPerShot - projectilesHitting} {"torpedo is picked up" if weapon.projectilesPerShot - projectilesHitting == 1 else "torpedoes are picked up"} by the point defense system. The remaining {"torpedo bursts" if projectilesHitting == 1 else "torpedoes burst"} into the hull of the target dealing {damage} damage.')
            else:
                printWithTypingAnimation(
                    'Just as the torpedoes are about to hit, the point defense system springs into action and destroys all of them!')
        case "Artillery Cannon":
            printWithTypingAnimation(
                f'{attackingShip.name} fires it\'s {weapon.name} at {targetShip.name}!', newLines=0)
            if damage:
                printWithTypingAnimation(
                    f'The {weapon.projectilesPerShot} projectiles fly through space, {projectilesHitting} {"shot hits" if projectilesHitting == 1 else "shots hit"}, exploding on impact and dealing {damage} damage to the hull!')
            else:
                printWithTypingAnimation(
                    f'The {weapon.projectilesPerShot} projectiles fly through space, but somehow all of them miss!')
        case "Plasma Cannon":
            # Railgun can only have one projectile per shot
            printWithTypingAnimation(
                f'{attackingShip.name} starts prepping it\'s {weapon.name}!', newLines=0)
            if damage:
                printWithTypingAnimation(
                    'The plasma beam illuminates the darkness of space. The beam hits the ship melting the hull and dealing {damage} damage!')
            else:
                printWithTypingAnimation(
                    f'The plasma beam starts to form, but then it suddenly stops. A leak in the plasma chamber has caused the beam to stop!')
        case "Gatling Gun":
            printWithTypingAnimation(
                f'{attackingShip.name} points it\'s {weapon.name} at {targetShip.name}!', newLines=0)
            if damage:
                printWithTypingAnimation(
                    f'It rattles off {weapon.projectilesPerShot} shots, {projectilesHitting} {"shot impacts" if projectilesHitting == 1 else "shots impact"}, the hull dealing {damage} damage!')
            else:
                printWithTypingAnimation(
                    'Just as the gun is about to unleash it\'s fury, the barrel jams!')
    print()
    return damage


def printProgressBar(title: str, fill: str = '#', speed: float = 0.1) -> None:
    thread = Thread(target=speak, args=(title,))
    thread.start()
    bar = Bar(title, max=20, fill=fill, suffix='%(percent)d%%', )
    for i in range(20):
        time.sleep(speed)
        bar.next()
    thread.join()
    bar.finish()


def prompt(question: str, options: list[str] | None = [], hiddenOptions: list[str] = []) -> str:
    printWithTypingAnimation(question)
    if options:
        thread = Thread(target=speak, args=(
            f"{', '.join([options[i] for i in range(len(options)-1)] + ['or ' + options[-1]])}",))
        thread.start()
        print(
            '[', f"{' / '.join([options[i] for i in range(len(options))])}", ']', sep='')
        thread.join()
        while True:
            try:
                choice = input("> ")
                if choice in options or choice in hiddenOptions:
                    print()
                    return choice
                else:
                    printWithTypingAnimation("Invalid choice")
            except ValueError:
                printWithTypingAnimation("Invalid choice")
    else:
        returnInput = input("> ")
        print()
        return returnInput
