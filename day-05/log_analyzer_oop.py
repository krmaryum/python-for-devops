"""
Day 05 – Object-Oriented Python for DevOps (Basics)

Refactor of Day 04 Log Analyzer using a class-based approach.
Keeps it simple and practical (no inheritance, no advanced patterns).
"""

# Bis mil Allah heer Rhaman nir Raheem


class LogAnalyzer:
    """A simple log analyzer that counts INFO/WARNING/ERROR lines."""

    def __init__(self, log_file, output_file="log_summary.txt"):
        self.log_file = log_file
        self.output_file = output_file
        self.lines = []
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        print("Constructor ran: object initialized")

    def read_logs(self):
        """Read the log file into memory, handling missing/empty files."""
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                self.lines = f.readlines()
        except FileNotFoundError:
            print(f"ERROR: {self.log_file} not found.")
            raise SystemExit("Please place a file in the folder or check the file name.")

        if not self.lines:
            print(f"ERROR: {self.log_file} is empty.")
            raise SystemExit("Without Data I am not able to do it.")

    def analyze_count_lines(self):
        """Count INFO/WARNING/ERROR occurrences using the same Day 04 rules."""
        for line in self.lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1

    def log_summary(self):
        """Build the summary report text."""
        return (
            "Log Analysis Summary\n"
            "--------------------\n"
            f"Total lines: {len(self.lines)}\n"
            f"INFO: {self.counts['INFO']}\n"
            f"WARNING: {self.counts['WARNING']}\n"
            f"ERROR: {self.counts['ERROR']}\n"
        )

    def write_summary(self, summary):
        """Write the summary to the output file."""
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write(summary)

    def run(self):
        """Run the full analysis workflow."""
        self.read_logs()
        self.analyze_count_lines()
        summary = self.log_summary()
        print(summary)
        self.write_summary(summary)
        print(f"Saved summary to {self.output_file}")
        raise SystemExit("Happy Learning!!!")


def main():
    log_file = input("Enter The File Name: ")
    analyzer = LogAnalyzer(log_file=log_file, output_file="log_summary.txt")
    analyzer.run()


if __name__ == "__main__":
    main()
