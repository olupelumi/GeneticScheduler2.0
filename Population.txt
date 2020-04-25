import java.util.ArrayList;

/** population */
public class Population {

  private ArrayList<DNA> populationArray;

  private Population(ArrayList<DNA> populationArray) {
    this.populationArray = populationArray;
  }

  public static Population generateRandomPopulation() {
    // creates a random first population
    throw new UnsupportedOperationException("not implemented yet");
  }

  public Population createNextGen() {
    // creates the next generation
    throw new UnsupportedOperationException("not implemented yet");
  }

  public ArrayList<DNA> createMatingPool() {
    // will create a mating pool
    throw new UnsupportedOperationException("not implemented yet");
  }
}
