# Gold Bar Finding Challenge

## Description

This program is designed to find a fake gold bar among a set of identical gold bars. The gold bars have the same size and appearance, with the only difference being that the fake bar weighs less than the others. The challenge is to determine the fake gold bar using a balance scale and a website simulation.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/smylaram/fetch_coding_exercise.git
   cd fetch_coding_exercise

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

1. **Running the Test:**

   ```bash
   pytest test_gold_bar.py

This test automates the process of finding the fake gold bar on the Fetch Challenge website. The test includes the algorithm for finding the fake gold bar, as well as actions such as clicking on buttons, getting measurement results, filling out bowl grids, and checking for an alert message.

The algorithm is implemented in the find_fake_bar function in test_gold_bar.py. It uses a divide-and-conquer approach to weigh groups of gold bars and narrow down the possibilities until the fake bar is found.
