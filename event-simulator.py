#!/usr/bin/env python3

import random
import time

# prints a random value from the list
messages = [
    "Debug: KukuLala Tumamba",
    "Debug: Graceful exit",
    "Debug: Connecting to db",
    "Debug: Starting authentication",
    # "Debug:",
    # "Debug:",
    # "Debug:",
    # "Debug:",
    # "Debug:",
    # "Debug:",
    "Info: Starting application",
    "Info: Restarting application",
    "Info: Stopping application",
    "Info: Cleaning the cache",
    "Info: Connecting to payment provider",
    "Info: Payment successful",
    # "Info:",
    # "Info:",
    # "Info:",
    # "Info:",
    "Warn: Running low on memory",
    "Warn: Running low on CPU",
    "Warn: Running low on disk space",
    "Warn: Too many connections",
    # "Warn:",
    # "Warn:",
    # "Warn:",
    # "Warn:",
    # "Warn:",
    # "Warn:",
    "Err: User does not exist",
    "Err: Wrong credentials",
    "Err: User is blocked",
    "Err: Not enough funds",
    "Err: Credit card is not compatible",
    "Err: Browser is not compatible",
    "Err: Process died unexpectedly",
    "Err: Age verification failed",
    "Err: No disk space left",
    "Err: Memory full",
]

while True:
    print(random.choice(messages))
    time.sleep(2)
