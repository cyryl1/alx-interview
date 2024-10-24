#!/usr/bin/env python3
import sys
import signal
import re
from typing import Dict, Match, Optional
from collections import defaultdict

class LogAnalyzer:
    def __init__(self):
        # Regular expression for parsing log lines
        self.line_pattern = r'(\d+\. \d+\. \d+\. \d+) - \[(.*?)\] 
        "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
        self.total_size = 0
        self.status_counts: Dict[int, int] = default(int)
        self.line_count = 0

        #list of valid status codes
        self.valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}

        # Set up signal handler for CTRL+C
        signal.signal(signal.SIGINT, self.signal_handler)

    def parse_line(self, line: str) -> Optional[Match]:
        """Parse a single log line and return the match object if valid."""
        return re.match(self.line_pattern, line.strip())

    def process_line(self, line: str) -> None:
        """Process a single log line and update statistics."""
        match = self.parse_line(line)
        if match:
            try:
                status_code = int(match.group(3))
                file_size = int(match.group(4))

                if status_code in self.valid_codes:
                    self.status_counts[status_code] += 1
                self.total_size += file_size
                self.line_count += 1

                if self.line_count % 10 == 0:
                    self.print_statistics()
                except ValueError:
                    pass

    def print_statistics(self) -> None:
        """Print the current statistics. """
        print("File size:", self.total_size)
        for code in sorted(self.status_counts.keys()):
            if self.status_counts[code] > 0:
                print(f"{code}: {self.status_counts[code]}")
        print()

    def signal_handler(self, sig, frame) -> None:
        """Handle CTRL+C by printing statisics and exiting."""
        print("\nKeyboard interruption detected")
        self.print_statistics()
        sys.exit(0)

    def process_stdin(self) -> None:
        """Processs input from stdin line by line."""
        try:
            for line in sys.stdin:
                self.process_line(line)
        except KeyboardInterrupt:
            self.signal_handler(None, None)

def main():
    analyzer = LogAnalyzer()
    analyzer.process_stdin()

if __name__ == "__main__":
    main()
