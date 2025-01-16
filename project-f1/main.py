import sys
from statistics import mean
from pathlib import Path
from typing import Dict, List, Tuple

def read_driver_info() -> Dict[str, dict]:
    """Read driver information from the file and return a dictionary."""
    driver_info = {}
    with open('./files-f1/f1_drivers.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                _, driver_code, name, team = parts
                driver_info[driver_code] = {'name': name, 'team': team}
    return driver_info

def process_timing_file(filename: str) -> Tuple[str, Dict[str, List[float]]]:
    """Process the timing file and return location and lap times."""
    driver_times = {}
    location = ""
    
    try:
        with open(filename, 'r') as file:
            # First line is the location
            location = file.readline().strip()
            
            # Process remaining lines
            for line in file:
                if len(line.strip()) >= 4:  # Ensure line has minimum length
                    driver_code = line[:3]
                    time = float(line[3:].strip())
                    
                    if driver_code not in driver_times:
                        driver_times[driver_code] = []
                    driver_times[driver_code].append(time)
                    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid data format in file - {e}")
        sys.exit(1)
        
    return location, driver_times

def calculate_stats(driver_times: Dict[str, List[float]]) -> Dict[str, dict]:
    """Calculate statistics for each driver."""
    stats = {}
    for driver, times in driver_times.items():
        stats[driver] = {
            'fastest': min(times),
            'average': mean(times),
            'laps': len(times)  # Add lap count
        }
    return stats

def display_results(location, stats, driver_info):
    """Display the results including driver names, teams, fastest lap, and average lap time."""
    print(f"\nLocation: {location}")
    print("Driver Code Name                Team                Fastest     Average")
    print("-" * 80)
    for driver_code, driver_stats in stats.items():
        name = driver_info.get(driver_code, {}).get('name', 'Unknown')
        team = driver_info.get(driver_code, {}).get('team', 'Unknown')
        fastest = driver_stats.get('fastest', 'N/A')
        average = driver_stats.get('average', 'N/A')
        print(f"{driver_code:<10} {name:<20} {team:<20} {fastest:<10} {average:<10}")

def display_menu():
    """Display the menu options."""
    print("\nF1 Timing Board - Menu")
    print("1. Show Race Location")
    print("2. Show Fastest Overall Lap")
    print("3. Show All Drivers' Fastest Laps")
    print("4. Show Overall Average Time")
    print("5. Show Each Driver's Average Time")
    print("6. Show Full Statistics")
    print("7. Show Lap Counts")  # New option
    print("8. Exit")
    return input("Select an option (1-8): ")

def display_fastest_overall(stats: Dict[str, dict], driver_info: Dict[str, dict]):
    """Display the fastest overall lap."""
    fastest_driver = min(stats.items(), key=lambda x: x[1]['fastest'])
    driver_code = fastest_driver[0]
    fastest_time = fastest_driver[1]['fastest']
    driver_name = driver_info.get(driver_code, {}).get('name', 'Unknown')
    print(f"\nFastest Overall Lap: {driver_name} ({driver_code}) - {fastest_time:.3f}")

def display_all_fastest(stats: Dict[str, dict], driver_info: Dict[str, dict]):
    """Display all drivers' fastest laps."""
    print("\nAll Drivers' Fastest Laps:")
    print("-" * 50)
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['fastest'])
    for driver_code, driver_stats in sorted_stats:
        name = driver_info.get(driver_code, {}).get('name', 'Unknown')
        print(f"{name:<20} ({driver_code}): {driver_stats['fastest']:.3f}")

def display_overall_average(stats: Dict[str, dict]):
    """Display the overall average lap time."""
    all_times = [time for driver_stats in stats.values() for time in [driver_stats['fastest']]]
    overall_avg = mean(all_times)
    print(f"\nOverall Average Time: {overall_avg:.3f}")

def display_driver_averages(stats: Dict[str, dict], driver_info: Dict[str, dict]):
    """Display each driver's average lap time."""
    print("\nDriver Average Times:")
    print("-" * 50)
    for driver_code, driver_stats in stats.items():
        name = driver_info.get(driver_code, {}).get('name', 'Unknown')
        print(f"{name:<20} ({driver_code}): {driver_stats['average']:.3f}")

def display_lap_counts(stats: Dict[str, dict], driver_info: Dict[str, dict]):
    """Display the number of laps per driver."""
    print("\nNumber of Laps per Driver:")
    print("-" * 50)
    for driver_code, driver_stats in stats.items():
        name = driver_info.get(driver_code, {}).get('name', 'Unknown')
        print(f"{name:<20} ({driver_code}): {driver_stats['laps']} laps")

def main():
    """Main function to run the F1 Timing Board application."""
    if len(sys.argv) != 2:
        print("Usage: python main.py <timing_file>")
        sys.exit(1)
    
    timing_file = sys.argv[1]
    driver_info = read_driver_info()
    location, driver_times = process_timing_file(timing_file)
    stats = calculate_stats(driver_times)
    
    while True:
        print("\nMenu:")
        print("1. Display all fastest laps")
        print("2. Display overall average lap time")
        print("3. Display driver averages")
        print("4. Display results")
        print("5. Display lap counts")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_all_fastest(stats, driver_info)
        elif choice == '2':
            display_overall_average(stats)
        elif choice == '3':
            display_driver_averages(stats, driver_info)
        elif choice == '4':
            display_results(location, stats, driver_info)
        elif choice == '5':
            display_lap_counts(stats, driver_info)
        elif choice == '6':
            print("\nThank you for using F1 Timing Board!")
            break
        else:
            print("\nInvalid option, please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()