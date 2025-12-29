"""
Day 06 – Building a CLI Tool for DevOps (argparse)

Reuses Day 05 OOP LogAnalyzer and adds:
  --file  (required) log file path
  --out   (optional) output file path
  --level (optional) filter: INFO | WARNING | ERROR

Run examples:
  python log_analyzer_cli.py --file app.log --out summary.txt
  python log_analyzer_cli.py --file app.log --level ERROR
"""

import argparse
import sys


class LogAnalyzer:
    """A simple log analyzer that counts INFO/WARNING/ERROR lines."""

    def __init__(self, log_file, output_file="log_summary.txt", level_filter=None):
        self.log_file = log_file
        self.output_file = output_file
        self.level_filter = level_filter.upper() if level_filter else None
        self.lines = []
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    def read_logs(self):
        """Read the log file into memory, handling missing/empty files."""
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                self.lines = f.readlines()
        except FileNotFoundError:
            print(f"ERROR: {self.log_file} not found.", file=sys.stderr)
            raise SystemExit("Tip: Check the file name/path and try again.")

        if not self.lines:
            print(f"ERROR: {self.log_file} is empty.", file=sys.stderr)
            raise SystemExit("Tip: Provide a log file with content.")

    def analyze_count_lines(self):
        """Count INFO/WARNING/ERROR occurrences (optionally filter by one level)."""
        for line in self.lines:
            if self.level_filter:
                # Filter mode: only count one level
                if self.level_filter in line:
                    self.counts[self.level_filter] += 1
                continue

            # Normal mode (same rules as Day 05)
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1

    def log_summary(self):
        """Build the summary report text."""
        filter_text = self.level_filter if self.level_filter else "None"
        return (
            "Log Analysis Summary\n"
            "--------------------\n"
            f"File: {self.log_file}\n"
            f"Filter Level: {filter_text}\n"
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

        # Print to terminal
        print(summary)

        # Write to output file
        self.write_summary(summary)
        print(f"Saved summary to {self.output_file}")


def build_parser():
    parser = argparse.ArgumentParser(description="Day 06 - CLI Log Analyzer")
    parser.add_argument("--file", required=True, help="Log file path (required)")
    parser.add_argument("--out", default="log_summary.txt", help="Output file path (optional)")
    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR"],
        help="Filter only one level (optional)",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    analyzer = LogAnalyzer(
        log_file=args.file,
        output_file=args.out,
        level_filter=args.level,
    )
    analyzer.run()


if __name__ == "__main__":
    main()
