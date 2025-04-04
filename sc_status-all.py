import argparse
import pexpect
import json
import re
import time
import sys

def parse_output_to_json(output):
    """Parse the Telnet output into a JSON object."""
    result = {}
    lines = output.splitlines()
    current_section = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith('---'):
            continue

        # Match key-value pairs
        match = re.match(r"^(.*?):\s+(.*)$", line)
        if match:
            key, value = match.groups()
            result[key.strip()] = value.strip()
        else:
            # Handle lines that don't match the key-value format
            if current_section:
                result[current_section] += f" {line.strip()}"
            else:
                current_section = line.strip()
                result[current_section] = ""

    return result

def telnet_to_host(host, login, password):
    """Telnet to the host, log in, and execute the command."""
    try:
        # Start the Telnet session
        child = pexpect.spawn(f"telnet {host}")

        # Enable real-time output logging
        # Wait 2 seconds before sending the password
        time.sleep(1)

        # Wait for the 'Password:' prompt
        child.expect(r"  Password:")
        child.sendline(password + "\r")

        # Wait for the 'SC:' prompt
        child.expect("SC:")

        # Send the command
        child.sendline("status sc -all" + "\r")

        # Read the output until the next 'SC:' prompt
        child.expect("SC:")
        output = child.before.decode('utf-8')

        # Exit the session
        child.sendline("exit")
        child.close()

        return output
    except pexpect.exceptions.TIMEOUT as e:
        print("Timeout occurred while waiting for a prompt.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Telnet to a host and parse output to JSON.")
    parser.add_argument("--host", required=True, help="The host to connect to.")
    parser.add_argument("--login", required=True, help="The login username.")
    parser.add_argument("--password", required=True, help="The login password.")
    args = parser.parse_args()

    # Telnet to the host and get the output
    output = telnet_to_host(args.host, args.login, args.password)
    if output:
        # Parse the output to JSON
        parsed_json = parse_output_to_json(output)
        print(json.dumps(parsed_json, indent=4))
    else:
        print("Failed to retrieve output from the host.")

if __name__ == "__main__":
    main()

        child.logfile = sys.stdout.buffer  # Print Telnet output to the console

        # Wait for 5 seconds to allow the server to send the banner and prompt
        time.sleep(5)

        # Wait for the 'User Name:' prompt
        child.expect(r"  User Name:")

        # Send the username
        child.sendline(login + "\r")
