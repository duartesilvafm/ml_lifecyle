
# Clean shangai dataset function

def shangai_clean(x):
    # Read excel file and sort by total score
    shangai = pd.read_excel("shanghaiData.xlsx").sort_values(by = "total_score", ascending = False)
    
    # Drop null values
    shangai.dropna(inplace = True)
    
    # Filter by the latest year
    shangai = shangai[shangai["year"] == shangai["year"].max()]
    
    # Simplify dataframe with only explanatory variables and drop null values
    shangai.drop(["world_rank", "university_name", "national_rank", "year", "total_score"], axis = 1, inplace = True)
    
    # Code the top 50 universities
    array_ref = (np.arange(len(shangai)) < x)
    shangai["top_50"] = array_ref
    code = {True:1.0, False:0.0}
    shangai["top_50"] = shangai["top_50"].map(code)
    
    # Return the array
    return shangai
def times_clean(a):
    
    # Read the csv file and sort by total score ind descending order
    times = pd.read_csv("timesData.csv").sort_values(by = "total_score", ascending = False)
    
    # Drop null values from total score
    times["total_score"] = pd.to_numeric(times["total_score"], errors = "coerce")
    times.dropna(inplace = True)
    
    # Filter by the latest year
    times = times[times["year"] == 2016] 
            
    # Simplify the table by dropping non explanatory variables
    times.drop(["world_rank", "university_name", "country", "year", "total_score"], axis = 1, inplace = True)
        
    # Convert all other columns to float type
    times["international"] = pd.to_numeric(times["international"], errors = "coerce")
    times["income"] = pd.to_numeric(times["income"], errors = "coerce") 
    times["female_male_ratio"] = pd.to_numeric(times["female_male_ratio"].apply(lambda d: d.split(" : ")[0]), errors = "coerce")
    times["international_students"] = pd.to_numeric(times["international_students"].apply(lambda d: d.split("%")[0]), errors = "coerce")
    
    student_list = []
    
    for x in range(len(times)):
        student_value = times["num_students"].iloc[x].replace(",",".")
        student_list.append(student_value)
        
    times["num_students"] = pd.to_numeric(student_list, errors = "coerce")
    
    # Drop null values once again after converting all other columns to float 
    times.dropna(inplace = True)
    
    # Add a new column with the actual ranking
    array_ref = (np.arange(len(times)) < a)
    times["top_50"] = array_ref
    code = {True:1.0, False:0.0}
    times["top_50"] = times["top_50"].map(code)
    
    return times