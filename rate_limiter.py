from __future__ import annotations

import time
from collections import deque
from dataclasses import dataclass, field


@dataclass
class RateLimiter:
    max_requests: int
    per_seconds: float
    _timestamps: deque[float] = field(default_factory=deque)

    def acquire(self) -> None:
        now = time.monotonic()
        while self._timestamps and now - self._timestamps[0] >= self.per_seconds:
            self._timestamps.popleft()

        if len(self._timestamps) >= self.max_requests:
            sleep_for = self.per_seconds - (now - self._timestamps[0])
            if sleep_for > 0:
                time.sleep(sleep_for)
            now = time.monotonic()
            while self._timestamps and now - self._timestamps[0] >= self.per_seconds:
                self._timestamps.popleft()

        self._timestamps.append(time.monotonic())
