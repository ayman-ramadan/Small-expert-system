def main():
     
    Questions = {
        # For High CPU Usage
        "Ruunning_resource_intensive_applications": False,
        "Noticed_background_processes_consuming_CPU": False,
        "Checked_task_manager_for_CPU_usage": False,
        #For High Memory Usage
        "Noticed_applications_consuming_a_lot_of_memory": False,
        "Opened_multiple_large_files": False,
        "Checked_task_manager_for_memory_usage": False,
        #For Low Disk Space
        "Downloaded_large_files": False,
        "Checked_for_unnecessary_files_taking_up_space": False,
        "Ran_disk_cleanup_to_free_up_space": False,
        #For High Network Latency
        "Experienced_slow_internet_speeds": False,
        "Checked_network_connection_for_stability": False,
        "Tried_restarting_router": False,
        #For Database Connection Failure
        "Having_trouble_accessing_the_database": False,
        "Checked_database_server_status": False,
        "Verified_database_connection_settings": False
        
        
    }

    # Ask questions return yes or no
    for Question in Questions.keys():
        Questions[Question] = For_Q(Question) 

    # Define inference rules for potintial issues
    Issues = {
        "High CPU Usage": "(Ruunning_resource_intensive_applications AND Noticed_background_processes_consuming_CPU) or (Checked_task_manager_for_CPU_usage)", 
        "High Memory Usage": "Noticed_applications_consuming_a_lot_of_memory AND (Opened_multiple_large_files OR Checked_task_manager_for_memory_usage)", 
        "Low Disk Space": "Downloaded_large_files AND Checked_for_unnecessary_files_taking_up_space AND Ran_disk_cleanup_to_free_up_space", 
        "High Network Latency": "Experienced_slow_internet_speeds AND (NOT Checked_network_connection_for_stability ) OR Tried_restarting_router " ,
        "Database Connection Failure" : "(Having_trouble_accessing_the_database OR Checked_database_server_status) AND Verified_database_connection_settings "
    }

    # Evaluate inference rules and determine potential_issues
    potential_issues = []
    for Issue, expression in Issues.items():
        if Eval_Expression(expression, Questions):
            potential_issues.append(Issue)

    # Print potential_issues
    if potential_issues:
        print("Issues that may apply based on your responses:")
        for Issue in potential_issues:
            print(Issue)
            
        # Suggest solutions based on identified issues
        suggest_solutions(potential_issues)
    else:
        print("No Issues based on your response")


def For_Q(Question):
    response = input(f"Have You {Question}?").lower()
    return response == "yes" #to handle if the user answer anything not(yes) return False

def Eval_Expression(expression, responses):
    expression = expression.replace("AND", "and").replace("OR", "or").replace("NOT","not")  
    return eval(expression, responses) 

def suggest_solutions(issues):
    solutions = {
        "High CPU Usage": [
            "Close unnecessary applications consuming CPU resources",
            "Check for malware or background processes"
        ],
        "High Memory Usage": [
            "Close memory-intensive applications",
            "Check for memory leaks in applications"
        ],
        "Low Disk Space": [
            "Delete unnecessary files or move them to an external storage device",
            "Use disk cleanup tools to remove temporary files"
        ],
        "High Network Latency": [
            "Restart router or modem",
            "Check for interference with other devices on the network"
        ],
        "Database Connection Failure": [
            "Check database server status and restart if necessary",
            "Verify database connection settings and credentials"
        ]
    }
    
    print("\nSuggested solutions based on identified issues:")
    for issue in issues:
        print(f"Issue: {issue}")
        print("Possible solutions:")
        for solution in solutions.get(issue, []):
            print(f"- {solution}")

if __name__ == "__main__":
    main()
