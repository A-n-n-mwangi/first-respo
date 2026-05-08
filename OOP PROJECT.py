MILESTONE 1 AND 2
# Data
age_female = (18, 19, 17, 20, 25, 23, 23, 21, 25, 23, 21, 23, 19, 18)
age_male = (15, 20, 23, 21, 23, 21, 22, 24, 19, 18, 25, 22, 26, 20, 21)

anxiety_female = (7, 5, 6, 4, 9, 8, 1, 4, 3, 6, 5, 9, 7, 8)
anxiety_male = (6, 2, 6, 5, 9, 5, 2, 4, 8, 9, 5, 6, 3, 1, 6)

stress_female = (3, 9, 7, 4, 6, 2, 4, 9, 7, 8, 3, 4, 6, 7)
stress_male = (4, 5, 8, 9, 9, 10, 3, 7, 9, 6, 4, 6, 3, 9, 7)

energy_female = (2, 6, 6, 4, 9, 7, 2, 5, 7, 5, 3, 7, 9, 4)
energy_male = (6, 7, 5, 8, 4, 9, 4, 6, 4, 8, 5, 2, 5, 8, 6)
# Create objects
female_stats = MentalHealthStats(age_female, anxiety_female, stress_female, energy_female)
male_stats = MentalHealthStats(age_male, anxiety_male, stress_male, energy_male)
import statistics

class MentalHealthStats:
    def _init_(self, ages, anxiety_levels, stress_levels, energy_levels):
        # Encapsulation: keep data private
        self._ages = ages
        self._anxiety_levels = anxiety_levels
        self._stress_levels = stress_levels
        self._energy_levels = energy_levels

    # Abstraction
    def get_max_values(self):
        return {
            "anxiety": max(self._anxiety_levels),
            "stress": max(self._stress_levels),
            "energy": max(self._energy_levels)
        }

    def get_min_values(self):
        return {
            "anxiety": min(self._anxiety_levels),
            "stress": min(self._stress_levels),
            "energy": min(self._energy_levels)
        }

    def get_mean_values(self):
        return {
            "anxiety": f"{statistics.mean(self._anxiety_levels):.2f}",
            "stress": f"{statistics.mean(self._stress_levels):.2f}",
            "energy": f"{statistics.mean(self._energy_levels):.2f}"
        }
   print("Female Max Values:", female_stats.get_max_values())
print("Male Max Values:", male_stats.get_max_values())

print("Female Min Values:", female_stats.get_min_values())
print("Male Min Values:", male_stats.get_min_values())

print("Female Mean Values:", female_stats.get_mean_values())
print("Male Mean Values:", male_stats.get_mean_values()) 
Milestone 2: Processing data with Loops and Conditionals
female_dataset = {"anxiety": [], "stress": [], "energy": []}

for score in raw_female_anxiety:
    if score > 0:  # Simple conditional check
        female_dataset["anxiety"].append(score)

   MILESTONE 3 AND 4

# File Handling 
    
    def save_to_file(self, filename="survey_data.json"):
        with open(filename, "w") as f:
            json.dump(self._dataset, f)
        self._observer.update("Data saved to file")

    def load_from_file(self, filename="survey_data.json"):
        with open(filename, "r") as f:
            self._dataset = json.load(f)
        self._observer.update("Data loaded from file")
 MILESTONE 3: FUNCTIONAL PROGRAMMING & PIPELINES
# =================================================================
class DataPipeline:
    """Handles data transformation using map, filter, and lambdas."""
    @staticmethod
    def get_high_intensity_scores(data_list):
        # Using filter and lambda
        return list(filter(lambda x: x >= 7, data_list))

    @staticmethod
    def normalize_scores(data_list):
        # Using map and lambda to scale 1-10 scores to 0.0-1.0
        return list(map(lambda x: x / 10.0, data_list))

# -----------------------------
# Survey Data
# -----------------------------
female_data = {
    "anxiety": [7, 5, 6, 4, 9, 8, 1, 4, 3, 6, 5, 9, 7, 8],
    "stress": [3, 9, 7, 4, 6, 2, 4, 9, 7, 8, 3, 4, 6, 7],
    "energy": [2, 6, 6, 4, 9, 7, 2, 5, 7, 5, 3, 7, 9, 4]
}

male_data = {
    "anxiety": [6, 2, 6, 5, 9, 5, 2, 4, 8, 9, 5, 6, 3, 1, 6],
    "stress": [4, 5, 8, 9, 9, 10, 3, 7, 9, 6, 4, 6, 3, 9, 7],
    "energy": [6, 7, 5, 8, 4, 9, 4, 6, 4, 8, 5, 2, 5, 8, 6]
}


# -----------------------------
# SYSTEM EXECUTION
# -----------------------------
try:
    female_system = MentalHealthSystem(female_data)
    male_system = MentalHealthSystem(male_data)

    # Validate data
    female_system.validate()
    male_system.validate()

    # Apply Strategies
    print("Female Mean:", female_system.analyze(MeanStrategy()))
    print("Male Mean:", male_system.analyze(MeanStrategy()))

    print("Female Max:", female_system.analyze(MaxStrategy()))
    print("Male Max:", male_system.analyze(MaxStrategy()))

    print("Female Min:", female_system.analyze(MinStrategy()))
    print("Male Min:", male_system.analyze(MinStrategy()))

    # Data Pipeline Example
    pipeline = DataPipeline(female_data["anxiety"])
    filtered = pipeline.filter_data(lambda x: x > 5)
    transformed = pipeline.transform_data(lambda x: x * 2)

    print("Filtered Anxiety (>5):", filtered)
    print("Transformed Anxiety (*2):", transformed)

    # Generator usage
    print("Generator Output:", list(pipeline.generator_pipeline()))

    # File persistence
    female_system.save_to_file()
    female_system.load_from_file()

except DataValidationError as e:
    print("Validation Error:", e)

except Exception as e:
    print("System Error:", e)


import json
import statistics

# -----------------------------
MILESTONE 4: OOP, DESIGN PATTERNS & CUSTOM EXCEPTIONS
# =================================================================
class DataValidationError(Exception):
    """Custom exception for data integrity."""
    pass

class AnalysisStrategy(ABC):
    """Strategy Pattern Interface."""
    @abstractmethod
    def analyze(self, data):
        pass

class MeanStrategy(AnalysisStrategy):
    def analyze(self, data):
        return round(statistics.mean(data), 2)

class MaxStrategy(AnalysisStrategy):
    def analyze(self, data):
        return max(data)

class SystemObserver:
    """Observer Pattern for logging events."""
    def notify(self, message):
        print(f"[LOG {time.strftime('%H:%M:%S')}]: {message}")

class MentalHealthSystem:
    """Core class using Encapsulation and Composition."""
    def __init__(self, name, data):
        self.name = name
        self._data = data  # Protected attribute
        self.observer = SystemObserver()

    def validate(self):
        if not self._data:
            raise DataValidationError(f"Dataset for {self.name} is empty.")
        self.observer.notify(f"Validation passed for {self.name}")

    def apply_analysis(self, strategy):
        # Milestone 4 Strategy application
        if hasattr(strategy, 'calculate_risk'): # Checking for Milestone 6 logic
            return strategy.calculate_risk(self._data)
        
        results = {key: strategy.analyze(val) for key, val in self._data.items()}
        self.observer.notify(f"Analysis '{strategy.__class__.__name__}' completed for {self.name}")
        return results


# Custom Exceptions 
# -----------------------------
class DataValidationError(Exception):
    pass


# -----------------------------
# Strategy Pattern 
# -----------------------------
class AnalysisStrategy:
    def analyze(self, data):
        pass


class MeanStrategy(AnalysisStrategy):
    def analyze(self, data):
        return round(statistics.mean(data), 2)


class MaxStrategy(AnalysisStrategy):
    def analyze(self, data):
        return max(data)


class MinStrategy(AnalysisStrategy):
    def analyze(self, data):
        return min(data)


# Observer Pattern 
class Observer:
    def update(self, message):
        print("LOG:", message)

MILESTONE 5 AND 6

# MILESTONE 5: ASYNCHRONOUS I/O
    # =============================================================
    async def save_report_async(self):
        """Asynchronous non-blocking file operation."""
        self.observer.notify(f"Starting async export for {self.name}...")
        await asyncio.sleep(1)  # Simulating I/O delay
        filename = f"{self.name}_report.json"
        with open(filename, "w") as f:
            json.dump(self._data, f)
        self.observer.notify(f"Report saved to {filename}")
        class InnovationRiskStrategy(AnalysisStrategy):
             NOVEL RESEARCH ALGORITHM
    Provides a weighted 'Mental Health Risk Index'.
    """
    def analyze(self, data):
        pass # Required by ABC

    def calculate_risk(self, dataset):
        anx = statistics.mean(dataset.get("anxiety", [0]))
        strss = statistics.mean(dataset.get("stress", [0]))
        enrgy = statistics.mean(dataset.get("energy", [0]))
        # Research formula: (Anxiety + Stress) balanced against Energy levels
        risk_index = (anx * 0.4) + (strss * 0.4) - (enrgy * 0.2)
        return round(risk_index, 3)

def run_parallel_tasks(systems, strategy):
    """MILESTONE 5: Multi-core Parallel Processing."""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Executes analysis for all groups simultaneously
        futures = {executor.submit(s.apply_analysis, strategy): s.name for s in systems}
        return {futures[f]: f.result() for f in concurrent.futures.as_completed(futures)}

# =================================================================
# SYSTEM EXECUTION (Putting it all together)
# =================================================================
async def main():
    try:
        # Initialize Systems (M4)
        female_sys = MentalHealthSystem(group_name_f, female_dataset)
        male_sys = MentalHealthSystem(group_name_m, male_dataset)
        all_systems = [female_sys, male_sys]

        # 1. Validation (M4)
        for sys in all_systems:
            sys.validate()

        print("\n--- MILESTONE 3: Functional Pipeline Example ---")
        high_anxiety = DataPipeline.get_high_intensity_scores(female_dataset["anxiety"])
        print(f"Female High Anxiety Scores (>=7): {high_anxiety}")

        print("\n--- MILESTONE 6: Innovation Analysis (Risk Index) ---")
        risk_strat = InnovationRiskStrategy()
        for sys in all_systems:
            score = sys.apply_analysis(risk_strat)
            print(f"{sys.name} Risk Index: {score}")

        print("\n--- MILESTONE 5: Parallel & Async Performance ---")
        # Parallel Processing
        start_time = time.perf_counter()
        parallel_results = run_parallel_tasks(all_systems, MeanStrategy())
        duration = time.perf_counter() - start_time
        print(f"Parallel Mean Results: {parallel_results}")
        print(f"Parallel Execution Time: {duration:.4f}s")

        # Asynchronous I/O
        await asyncio.gather(*(sys.save_report_async() for sys in all_systems))

        print("\n[SUCCESS] System integration of all Milestones 1-6 complete.")

    except DataValidationError as e:
        print(f"Data Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")

if __name__ == "__main__":
    # Run the top-level async entry point
    asyncio.run(main())
