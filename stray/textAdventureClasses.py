from random import choice, randint, choices

MAX_PLAYERSHIP_HEALTH = 189


class Weapon:
    def __init__(self, name: str, damageRange: tuple[int, int], projectilesPerShot: int) -> None:
        self.name = name
        self.damageRange = damageRange
        self.projectilesPerShot = projectilesPerShot

    def __str__(self) -> str:
        return self.name

    def fire(self) -> tuple[int, int]:
        totalMiss = choices([True, False], [0.1, 0.9], k=1)[0]
        if totalMiss:
            return 0, 0
        projectilesHit = randint(1, self.projectilesPerShot)
        return (randint(self.damageRange[0], self.damageRange[1]) * projectilesHit, projectilesHit)


smallLaserTurret = Weapon("Small Laser Turret",
                          (15, 20), 2)  # 30-40, 15-20
missileLauncher = Weapon("Missile Launcher", (10, 15),
                         6)  # 60-90, 10-15
railgun = Weapon("Railgun", (50, 60), 1)  # 50-60, 50-60
torpedoLauncher = Weapon("Torpedo Launcher", (25, 35),
                         2)  # 50-70, 25-35
artilleryCannon = Weapon("Artillery Cannon", (14, 20),
                         4)  # 56-80, 14-20
plasmaBeam = Weapon("Plasma Beam", (60, 70), 1)  # 60-70, 60-70
gatlingGun = Weapon("Gatling Gun", (5, 8), 25)  # 125-200, 5-8

weaponDict = {
    "Small Laser Turret": smallLaserTurret,
    "Missile Launcher": missileLauncher,
    "Railgun": railgun,
    "Torpedo Launcher": torpedoLauncher,
    "Artillery Cannon": artilleryCannon,
    "Plasma Beam": plasmaBeam,
    "Gatling Gun": gatlingGun
}


class Spacecraft:
    def __init__(self, name: str, graphic: str, crew: int, speed: int, hull: int, weapons: list[str]) -> None:
        self.name = name
        self.graphic = graphic
        self.crew = crew
        self.speed = speed
        self.hull = hull
        self.weapons = weapons

    def __str__(self) -> str:
        return f"{self.graphic}\n{self.name} - Crew: {self.crew} - Speed: {self.speed} - Hull: {self.hull} - Weapons: {', '.join(self.weapons)}"


Aqua = Spacecraft("Aqua", """
   :::-
    ] [] [=] [-*@
   [  []}{
    ] [] [=] [-*@
   :::-
""", 10, 36, 81, [railgun.name, railgun.name, smallLaserTurret.name])
Cobra = Spacecraft("Cobra", """
   }{=
     D-) (0()8<)]X(
   +[] X=0} {|X()*<>**
     D-) (0()8<)]X(
   }{=
""", 34, 26, 165, [railgun.name, missileLauncher.name, missileLauncher.name])
Stinger = Spacecraft("Stinger", """
    888))=
    -)-)-))-))-))-))-))
   (X==<>==X)>
    -)-)-))-))-))-))-))
    888))=
""", 20, 40, 102, [railgun.name, railgun.name, smallLaserTurret.name, smallLaserTurret.name])
Spike = Spacecraft("Spike", """
   8-8)=
   ) ((@)[
   -<  *) (> <] [
   ) ((@)[
   8-8)=
""", 12, 49, 88, [smallLaserTurret.name, gatlingGun.name])
Nimbus = Spacecraft("Nimbus", """
   ---x---
     -)8-8(=
   {}(&)
     -)8-8(=
     -x-
""", 8, 53, 76, [smallLaserTurret.name, smallLaserTurret.name])
Tsar = Spacecraft("Tsar", """
    88((=
   -)-)-)-)-)-)
   [~] (x-x-x)><(x-x-x)
   -)-)-)-)-)-)
    88((=
""", 43, 20, 160, [torpedoLauncher.name, artilleryCannon.name])
Shockwave = Spacecraft("Shockwave", """
    88((+
   8-8((+
   -][  O] [<)] [O(!)
   8-8((+
    88((+
""", 17, 17, 69, [missileLauncher.name, railgun.name])
Vortex = Spacecraft("Vortex", """
   <---x x--->
    {}8<>[=<><><() (D8
   +[]  X|)}8|] [8()) ((-
    {}8<>[=<><><() (D8
     <-x x->
""", 40, 10, 250, [torpedoLauncher.name, smallLaserTurret.name, smallLaserTurret.name])
Phazek = Spacecraft("Phazek", """
   8-8((=
     =+))|o|((+=
   :x:  (X==<>==X)>
     =+))|o|((+=
   8-8((=
""", 13, 73, 254, [railgun.name, smallLaserTurret.name, smallLaserTurret.name, smallLaserTurret.name])
Tilde = Spacecraft("Tilde", """
   \\~\\
    ){<>] [> <:=>
   {@(!)<>-:=}-) (8()
    ){<>] [> <:=>
   /~/
""", 11, 78, 112, [missileLauncher.name, missileLauncher.name, smallLaserTurret.name])
Pling = Spacecraft("Pling", """
   \\.
     (+)===\\
   O=|-|OOOOO
     (+)===/
   /.
""", 30, 50, 100, [plasmaBeam.name, smallLaserTurret.name])
Hyperion = Spacecraft("Hyperion", """
     -)8&8((+
    >>===-
   <[]  O
    >>===-
     -)8&8((+
""", 32, 30, 94, [plasmaBeam.name, artilleryCannon.name])
Nexus = Spacecraft("Nexus", """
     //\\
     -<<::0:>-=
    *=<@O(*)
     -<<::0:>-=
     \\/
""", 21, 35, 60, [gatlingGun.name, gatlingGun.name])
Stray = Spacecraft("Stray", """
     \\+\\
    ]D-)@=<>) (]()<>
   (=+(-)+=)
    ]D-)@=<>) (]()<>
     /+/
""", 25, 39, MAX_PLAYERSHIP_HEALTH, [railgun.name, missileLauncher.name, smallLaserTurret.name])
friendlyHeavyCruiser1 = Spacecraft("Aurora", """
    888(+
  #} {(@}{o}>@> <[-|-|-|-]] [}
   [-  [X<{o}[>X]) ((*)>
  #} {(@}{o}>@> <[-|-|-|-]] [}
    888(+
""", 50, 38, 321, [railgun.name, missileLauncher.name, missileLauncher.name, gatlingGun.name, smallLaserTurret.name, smallLaserTurret.name, smallLaserTurret.name])
friendlyHeavyCruiser2 = Spacecraft("Muinnellim", """
    888(+
  #} {(@}{o}>@> <[-|-|-|-]] [}
   [-  [X<{o}[>X]) ((*)>
  #} {(@}{o}>@> <[-|-|-|-]] [}
    888(+
""", 50, 38, 321, [railgun.name, missileLauncher.name, missileLauncher.name, gatlingGun.name, smallLaserTurret.name, smallLaserTurret.name, smallLaserTurret.name])


class Game:
    def __init__(self) -> None:
        self.username: str = ""
        self.password: str = ""
        self.catName: str = ""
        self.playerSpaceship: Spacecraft = Stray
        self.plotPoints: list[str] = []
        self.enemySpaceships: list[Spacecraft] = []

    def newEnemySpaceship(self, count: int) -> None:
        while True:
            enemySpaceship = choice([Cobra, Stinger, Spike, Nimbus, Tsar,
                                    Shockwave, Vortex, Phazek, Tilde, Pling, Hyperion, Nexus])
            if enemySpaceship not in self.enemySpaceships:
                self.enemySpaceships.append(enemySpaceship)
                break
        self.enemySpaceships = choices(
            [Cobra, Stinger, Spike, Nimbus, Tsar, Shockwave, Vortex, Phazek, Tilde, Pling, Hyperion, Nexus], k=count)
