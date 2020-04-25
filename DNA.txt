import java.util.ArrayList;
import java.util.HashMap;

/** DNA This DNA class will represent a possible schedule. */
public class DNA {
  private String name;
  // initializing new hashmap
  // {'Monday':{'10AM':["Brendan","Magdah"],'11AM':[Brendan,Areli]}}
  private HashMap<String, HashMap<String, ArrayList<String>>> schedule = new HashMap<>();

  private DNA(
      final String name,
      HashMap<String, HashMap<String, ArrayList<String>>>
          schedule) { // writing my first constructor. This is cool
    this.name = name;
    this.schedule = schedule;
  }

  public static DNA createRandomSchedule() {
    // returns a random schedule
    // here in this will be getting the names of people who took the survey and the dates and such
    throw new UnsupportedOperationException("Not implemented yet");
  }
  // TODO
  public DNA mutate() {
    // mutating schedules, making this an instance method
    throw new UnsupportedOperationException("Not implemented yet");
  }

  public DNA crossbreed(final DNA parent2) {
    // crossbreeding two schedules
    final DNA parent1 = this;
    // do some logic and then return a random crossbreed
    throw new UnsupportedOperationException("Not implemented yet");
  }
}
