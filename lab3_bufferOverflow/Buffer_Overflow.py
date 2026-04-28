class BufferOverflowLab:
    def __init__(self):
        # Simulated stack frame:
        # [ buffer (8 bytes) ][ canary (4 bytes) ][ return address (4 bytes) ]
        self.buffer_size = 8
        self.canary_size = 4
        self.ret_size = 4
        self.total_size = self.buffer_size + self.canary_size + self.ret_size

        self.reset_memory()

    def reset_memory(self):
        self.memory = bytearray(self.total_size)

        # Fill buffer with dots for display
        for i in range(self.buffer_size):
            self.memory[i] = ord('.')

        # Canary bytes
        self.memory[8:12] = b"SAFE"

        # Simulated return address
        self.memory[12:16] = b"RET!"

    def display_memory(self):
        buffer_part = self.memory[0:8].decode("latin1")
        canary_part = self.memory[8:12].decode("latin1")
        ret_part = self.memory[12:16].decode("latin1")

        print("\n--- Simulated Stack Frame ---")
        print(f"Buffer (8 bytes):        {buffer_part}")
        print(f"Canary (4 bytes):        {canary_part}")
        print(f"Return Address (4 bytes): {ret_part}")
        print("-----------------------------\n")

    def safe_copy(self, user_input):
        self.reset_memory()
        data = user_input.encode("latin1")

        max_len = min(len(data), self.buffer_size)
        for i in range(max_len):
            self.memory[i] = data[i]

        print("SAFE COPY: input truncated to fit buffer.")
        self.display_memory()
        self.explain_result()

    def vulnerable_copy(self, user_input):
        self.reset_memory()
        data = user_input.encode("latin1")

        print("VULNERABLE COPY: writing input without bounds checking...")

        # Simulate writing past the end of the buffer
        for i in range(len(data)):
            if i < self.total_size:
                self.memory[i] = data[i]
            else:
                # Beyond our simulated stack frame
                print(f"Extra byte '{chr(data[i])}' would write even further into memory.")

        self.display_memory()
        self.explain_result()

    def explain_result(self):
        current_canary = self.memory[8:12].decode("latin1")
        current_ret = self.memory[12:16].decode("latin1")

        if current_canary != "SAFE":
            print("Result: The canary was overwritten.")
            print("Meaning: Data spilled past the buffer and corrupted nearby memory.")

        if current_ret != "RET!":
            print("Result: The return address was overwritten.")
            print("Meaning: In a real unsafe program, execution flow could be changed.")

        if current_canary == "SAFE" and current_ret == "RET!":
            print("Result: No protected memory was overwritten.")
            print("Meaning: The input stayed within the buffer limits.")

        print()

    def run_demo(self):
        print("=== Buffer Overflow Lab (Safe Python Simulation) ===")
        print("This demonstrates how writing too much data into a buffer")
        print("can overwrite nearby memory like a canary or return address.\n")

        while True:
            print("Choose an option:")
            print("1. Show fresh memory layout")
            print("2. Safe copy")
            print("3. Vulnerable copy")
            print("4. Example overflow demo")
            print("5. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.reset_memory()
                self.display_memory()

            elif choice == "2":
                user_input = input("Enter data to copy safely: ")
                self.safe_copy(user_input)

            elif choice == "3":
                user_input = input("Enter data to copy vulnerably: ")
                self.vulnerable_copy(user_input)

            elif choice == "4":
                print("\nExample input: ABCDEFGH1234WXYZ")
                print("This is longer than 8 bytes, so it will overwrite the canary and return address.\n")
                self.vulnerable_copy("ABCDEFGH1234WXYZ")

            elif choice == "5":
                print("Exiting lab.")
                break

            else:
                print("Invalid choice.\n")


if __name__ == "__main__":
    lab = BufferOverflowLab()
    lab.run_demo()
