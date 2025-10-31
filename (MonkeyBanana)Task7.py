class MonkeyBananaProblem:
    def __init__(self):
        # Initial state
        self.state = {
            "monkey_position": "floor",       # Monkey starts on the floor
            "box_position": "corner",         # Box is at corner
            "banana_position": "ceiling",     # Banana is hanging from ceiling
            "monkey_on_box": False,           # Monkey not on box
            "monkey_has_banana": False        # Monkey doesn’t have banana yet
        }

    def move_box(self):
        """Monkey moves the box under the banana."""
        if (self.state["monkey_position"] == "floor" and 
            self.state["box_position"] == "corner"):
            self.state["box_position"] = "under_banana"
            self.state["monkey_position"] = "under_banana"
            print("Step 1: Monkey moves box under the banana.")
        else:
            print("Cannot move box right now.")

    def climb_box(self):
        """Monkey climbs onto the box."""
        if (self.state["monkey_position"] == "under_banana" and 
            self.state["box_position"] == "under_banana"):
            self.state["monkey_on_box"] = True
            print("Step 2: Monkey climbs onto the box.")
        else:
            print("Monkey is not near the box to climb.")

    def grab_banana(self):
        """Monkey grabs the banana if on the box."""
        if (self.state["monkey_on_box"] and 
            self.state["banana_position"] == "ceiling"):
            self.state["monkey_has_banana"] = True
            print("Step 3: Monkey grabs the banana!")
        else:
            print("Monkey cannot reach the banana yet.")

    def solve(self):
        """Perform sequence of actions to achieve the goal."""
        print("--- Monkey and Banana Problem ---")
        print("Initial State:", self.state)
        print()

        self.move_box()
        self.climb_box()
        self.grab_banana()

        print("\nFinal State:", self.state)
        if self.state["monkey_has_banana"]:
            print("✅ Goal Achieved: Monkey has the banana.")
        else:
            print("❌ Goal not achieved.")


# --- Run the problem ---
problem = MonkeyBananaProblem()
problem.solve()
