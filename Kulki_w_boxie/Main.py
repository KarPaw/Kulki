from Coords import Coords as Coordinates
from Total_Energy import Total_Energy
from MonteCarlo import MonteCarlo

if __name__ == "__main__":
    crds = Coordinates("testy\sim2d-system.txt")
    factory = Total_Energy(crds)

    # factory.register_energy_type("HARMONIC",HarmonicMaker())
    # factory.register_energy_type("COULOMB",CoulombMaker())
    # factory.register_energy_type("REPULSION", RepulsionMaker())
    en = factory.from_file("testy\sim2d-energy.txt")
    print(en)
    factory.energy()
    simulation = MonteCarlo(crds, factory, 1.0)

    simulation.sample(10)
    print("Koniec testów")
