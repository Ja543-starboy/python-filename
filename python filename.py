# File Processor: Read, Modify, and Write Files with Error Handling
import os

def modify_content(content):
    """Example modification - converts to uppercase and adds line numbers"""
    return [f"{i+1}: {line.upper()}" for i, line in enumerate(content)]

def process_file():
    print("📝 File Processor - Read, Modify, and Write Files 📝")
    
    while True:
        try:
            # Get input filename
            input_file = input("\nEnter input filename (or 'quit'): ").strip()
            if input_file.lower() == 'quit':
                break

            # Verify file exists and is readable
            if not os.path.exists(input_file):
                raise FileNotFoundError(f"File '{input_file}' not found")
            if not os.access(input_file, os.R_OK):
                raise PermissionError(f"Cannot read '{input_file}' - permission denied")

            # Read file
            try:
                with open(input_file, 'r') as f:
                    content = f.readlines()
            except UnicodeDecodeError:
                raise UnicodeDecodeError("File appears to be binary - cannot read")

            # Show original content
            print("\nOriginal content:")
            print(''.join(content))

            # Modify content
            modified = modify_content(content)

            # Get output filename
            output_file = input("\nEnter output filename: ").strip()
            
            # Check if output exists
            if os.path.exists(output_file):
                confirm = input(f"'{output_file}' exists. Overwrite? (y/n): ").lower()
                if confirm != 'y':
                    print("Skipping file write")
                    continue

            # Write output
            try:
                with open(output_file, 'w') as f:
                    f.writelines(modified)
                print(f"✅ Successfully wrote to '{output_file}'")
            except PermissionError:
                raise PermissionError(f"Cannot write to '{output_file}' - permission denied")

        except Exception as e:
            print(f"❌ Error: {e}")

        # Continue?
        if input("\nProcess another file? (y/n): ").lower() != 'y':
            print("👋 Exiting...")
            break

if __name__ == "__main__":
    process_file()