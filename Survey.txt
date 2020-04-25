import com.google.gson.Gson;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Optional;

/**
 * Survey Data structure to represent the information coming from the inputted survey need the list
 * of names preference information as a mapping of a mapping(name to day/time to the number they
 * ranked that shift).
 *
 * <p>The way the surbey json is structured is that it is a an array of json objects
 *
 * <p>To be honest I'm thinking about this now and perhaps I want to also create a name class with
 * the person's specific preference but that also may be unneccessarry. I think I need to do more
 * thinking about my overall design of the project, starting at a high level at the main code
 * functionality
 *
 * <p>Also I think I should change how the "schedulePreference" data structure looks like. I'm
 * thinking it should be a Hashmap<String,Hashmap<String, Integer>> where the outer key is the name
 * of an employee and the inner value is a dictionary of a bunch of information about the
 * preferences and such of the employee.
 */
public class Survey {
  private List<String> names;
  private List<HashMap<String, Object>> schedulePreference =
      new ArrayList<>(); // The value of the information are of different types

  private Survey(List<String> names, List<HashMap<String, Object>> schedulePreference) {
    this.names = names;
    this.schedulePreference = schedulePreference;
  }
  // Will need to make some getters and setters as well as more constructors
  // one constructor will be taking in the json and making it into an instance of the survey class

  // making a public constructor here
  // reading a json file and instantiating it as an instance of a survey class
  // I need to read the gson documentation
  public static Survey fromJson(String filName) throws FileNotFoundException {
    Survey surveyObject;

    FileReader reader =
        new FileReader("C:\\Users\\Pelumi\\IdeaProjects\\GeneticScheduler\\survey_data.json");

    // Using options to take care of error handling
    Optional<FileReader> optFile = Optional.of(reader);
    // Throws an exception if file not found and then I can fix it from there
    FileReader newReader = optFile.orElseThrow(() -> new FileNotFoundException());
    // Initializing Gson object
    Gson gson = new Gson();
    Object preferenceList = gson.fromJson(reader, Object.class);
    List<HashMap<String, Integer>> testMap = (List<HashMap<String, Integer>>) preferenceList;
    // String[] nameList = (String[]) testMap.keySet().toArray();
    // return new Survey(nameList, testMap);

    throw new UnsupportedOperationException("Not fully implemented yet");

    //    try {
    //      FileReader reader =
    //          new
    // FileReader("C:\\Users\\Pelumi\\IdeaProjects\\GeneticScheduler\\survey_data.json");
    //      //Initializing Gson object
    //      Gson gson = new Gson();
    //      Object object = gson.fromJson(reader,Object.class);
    //      HashMap<String, HashMap<String, Integer>> testMap = (HashMap<String, HashMap<String,
    // Integer>>) object;
    //      String[] nameList = (String[]) testMap.keySet().toArray();
    //      surveyObject = new Survey(nameList,testMap);
    //
    //      //return new Survey(names,testMap);
    //      //return reader;
    //      //System.out.println(reader);
    //    } catch (FileNotFoundException e) {
    //      e.printStackTrace();
    //    } finally{
    //      System.out.println("put this so I know that my code actually ran");
    //    }
    // return surveyObject;
  }

  /**
   * Create schedule preference structure from a list of mappings to a mapping of mappings e.g
   * {Name:{Monday, 9AM:2}}
   */
  private HashMap<String, HashMap<String, Object>> createSchedulePreferenceStructure(
      List<HashMap<String, Object>> PreferenceListInfo) {
    // Initializing a map data structure
    HashMap<String, HashMap<String, Object>> EmployeePreferenceMap =
        new HashMap<String, HashMap<String, Object>>();

    // Iterating through the list preference information, extracting the name and then making that a
    // key and the rest of the information to be its value
    for (HashMap<String, Object> preferenceMapping : PreferenceListInfo) {
      String employeeName = (String) preferenceMapping.get("name");
      preferenceMapping.remove("name");
      EmployeePreferenceMap.put(employeeName, preferenceMapping);
    }
    return EmployeePreferenceMap;
  }
}
