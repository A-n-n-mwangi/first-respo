"""
MENTAL HEALTH ANALYTICS SYSTEM: MILESTONES 1-6
Organized Systematically
"""

import statistics
import json
import time
import asyncio
import concurrent.futures
from abc import ABC, abstractmethod

# =================================================================
# MILESTONE 1 & 2: FOUNDATIONS (Variables, Data Types & Control Flow)
# =================================================================
# Variables and basic data structures (Lists and Dictionaries)
group_name_f = "Female_Group"
group_name_m = "Male_Group"

# Raw Data (Milestone 1: Basic Types)
# Scores represent Anxiety, Stress, and Energy on a scale of 1-10
raw_female_anxiety = [7, 5, 6, 4, 9, 8, 1, 4, 3, 6, 5, 9, 7, 8]
raw_female_stress = [3, 9, 7, 4, 6, 2, 4, 9, 7, 8, 3, 4, 6, 7]
raw_female_energy = [2, 6, 6, 4, 9, 7, 2, 5, 7, 5, 3, 7, 9, 4]

# Milestone 2: Processing data with Loops and Conditionals
female_dataset = {"anxiety": [], "stress": [], "energy": []}

for score in raw_female_anxiety:
    if score > 0:  # Simple conditional check
        female_dataset["anxiety"].append(score)

# Finalizing the structured data for Male group
male_dataset = {
    "anxiety": [6, 2, 6, 5, 9, 5, 2, 4, 8, 9, 5, 6, 3, 1, 6],
    "stress": [4, 5, 8, 9, 9, 10, 3, 7, 9, 6, 4, 6, 3, 9, 7],
    "energy": [6, 7, 5, 8, 4, 9, 4, 6, 4, 8, 5, 2, 5, 8, 6]
}

# =================================================================
# MILESTONE 3: FUNCTIONAL PROGRAMMING & PIPELINES
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

# =================================================================
# MILESTONE 4: OOP, DESIGN PATTERNS & CUSTOM EXCEPTIONS
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

    # =============================================================
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

# =================================================================
# MILESTONE 5 & 6: CONCURRENCY & RESEARCH INNOVATION
# =================================================================
class InnovationRiskStrategy(AnalysisStrategy):
    """
    MILESTONE 6: NOVEL RESEARCH ALGORITHM
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