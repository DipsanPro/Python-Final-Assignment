import sys
from statistics import mean
from pathlib import Path
from typing import Dict, List, Tuple

def read_driver_info(filename: str = "files-f1/drivers.txt") -> Dict[str, dict]:
    """Read driver information from drivers.txt file"""
    drivers = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                code, number, name, team = line.strip().split(',')
                drivers[code] = {
                    'number': number,
                    'name': name,
                    'team': team
                }
    except FileNotFoundError:
        print(f"Warning: Driver info file {filename} not found")
    return drivers

def process_timing_file(filename: str) -> Tuple[str, Dict[str, List[float]]]:
    """Process the timing file and return location and lap times"""
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

# Modify calculate_stats function to include lap count
def calculate_stats(driver_times: Dict[str, List[float]]) -> Dict[str, dict]:
    """Calculate statistics for each driver"""
    stats = {}
    for driver, times in driver_times.items():
        stats[driver] = {
            'fastest': min(times),
            'average': mean(times),
            'laps': len(times)  # Add lap count
        }
    return stats

def display_results(location: str, stats: Dict[str, dict], driver_info: Dict[str, dict]):
    """Display formatted results"""
    print(f"\nFormula 1 Timing Board - {location}")
    print("-" * 80)
    
    # Find fastest overall time
    fastest_driver = min(stats.items(), key=lambda x: x[1]['fastest'])
    print(f"\nFastest Lap: {fastest_driver[0]} - {fastest_driver[1]['fastest']:.3f}")
    
    # Calculate overall average
    all_times = [time for driver_stats in stats.values() for time in [driver_stats['fastest']]]
    overall_average = mean(all_times)
    print(f"Overall Average: {overall_average:.3f}")
    
    # Display detailed results
    print("\nDetailed Results:")
    print("-" * 80)
    print(f"{'Driver Code':<12}{'Name':<20}{'Team':<20}{'Fastest':<12}{'Average':<12}")
    print("-" * 80)
    
    # Sort by fastest lap time
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['fastest'])
    
    for driver_code, driver_stats in sorted_stats:
        driver = driver_info.get(driver_code, {})
        name = driver.get('name', 'Unknown')
        team = driver.get('team', 'Unknown')
        
        print(f"{driver_code:<12}{name[:19]:<20}{team[:19]:<20}"
              f"{driver_stats['fastest']:<12.3f}{driver_stats['average']:<12.3f}")

# Add new menu option
def display_menu():
    """Display the menu options"""
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
    fastest_driver = min(stats.items(), key=lambda x: x[1]['fastest'])
    driver_code = fastest_driver[0]
    fastest_time = fastest_driver[1]['fastest']
    driver_name = driver_info.get(driver_code, {}).get('name', 'Unknown')
    print(f"\nFastest Overall Lap: {driver_name} ({driver_code}) - {fastest_time:.3f}")

def display_all_fastest(stats: Dict[str, dict], driver_info: Dict[str, dict]):
    print("\nAll Drivers' Fastest Laps:")
    print("-" * 50)
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['fastest'])
    for driver_code, driver_stats in sorted_stats:
        name = driver_info.get(driver_code, {}).get('name', 'Unknown')
        print(f"{name:<20} ({driver_code}): {driver_stats['fastest']:.3f}")

def display_overall_average(stats: Dict[str, dict]):
    all_times = [time for driver_stats in stats.values() for time in [driver_stats['fastest']]]
    overall_avg = mean(all_times)
    print(f"\nOverall Average Time: {overall_avg:.3f}")

def display_driver_averages(stats: Dict[str, dict], driver_info: Dict[str, dict]):
    print("\nDriver Average Times:")
    print("-" * 50)
    for driver_code, driver_stats in stats.items():
        name = driver_info.get(driver_code, {}).get('name', 'Unknown')
        print(f"{name:<20} ({driver_code}): {driver_stats['average']:.3f}")

# Add new display function
def display_lap_counts(stats: Dict[str, dict], driver_info: Dict[str, dict]):
    print("\nNumber of Laps per Driver:")
    print("-" * 50)
    for driver_code, driver_stats in stats.items():
        name = driver_info.get(driver_code, {}).get('name', 'Unknown')
        print(f"{name:<20} ({driver_code}): {driver_stats['laps']} laps")

# Modify main loop to include new option
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <timing_file>")
        sys.exit(1)
    
    timing_file = sys.argv[1]
    driver_info = read_driver_info()
    location, driver_times = process_timing_file(timing_file)
    stats = calculate_stats(driver_times)
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            print(f"\nRace Location: {location}")
        elif choice == '2':
            display_fastest_overall(stats, driver_info)
        elif choice == '3':
            display_all_fastest(stats, driver_info)
        elif choice == '4':
            display_overall_average(stats)
        elif choice == '5':
            display_driver_averages(stats, driver_info)
        elif choice == '6':
            display_results(location, stats, driver_info)
        elif choice == '7':
            display_lap_counts(stats, driver_info)
        elif choice == '8':
            print("\nThank you for using F1 Timing Board!")
            break
        else:
            print("\nInvalid option, please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()