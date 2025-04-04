# Motorola EBTS Site Controller Status Fetcher
This Python script is designed to interact with a Motorola EBTS Site Controller via Telnet to fetch and parse the controller's status information. The script logs into the Site Controller, executes the status sc -all command, and parses the output into a JSON format for easy readability and further processing.

## Features
* Connects to the Motorola EBTS Site Controller using Telnet.
* Logs in using provided credentials (User Name and Password).
* Executes the ```status sc -all``` command to fetch the controller's status.
* Parses the output into a structured JSON format.
* Outputs the JSON data to the console.

## Requirements
* Python 3.6 or higher
* pexpect library for Telnet communication

## Installation
* Clone or download this repository to your local machine.
* Install the required Python library:
```pip install pexpect```

## Usage
Run the script with the following command-line arguments:

```python3 script.py --host <HOST> --login <USERNAME> --password <PASSWORD>```

### Arguments:
```--host:``` The IP address or hostname of the Motorola EBTS Site Controller.\
```--login:``` The username for logging into the Site Controller.\
```--password:``` The password for logging into the Site Controller.

## Output
The script will output the parsed status information in JSON format. Example:
```
{
    "Overall Status": "Active - NON_SYNC_ADJ_REQ / FREQ_CALIB_TIMER_EXPIRY",
    "BTS type": "EBTS",
    "Site Status": "Wide Trunking(SecurityClass1)",
    "Internal State": "AS_U_E_A",
    "Site Link State": "UP",
    "Netcom Primary": "ACTIVE_S",
    "Netcom Secondary": "STANDBY_S",
    "Position ID": "A",
    "Internal Temp": "33 DegC  (Alarm at: 70 DegC)",
    "Last start up": "18:24:04 27-Feb-2025 (RTC)",
    "Last reset (via SW)": "21:23:48 15-May-2024 (RTC)",
    "Last reset (non SW)": "18:24:04 27-Feb-2025 (RTC)",
    "Last enter to WAT": "10:35:58 04-Apr-2025 (RTC)",
    "Last exit from WAT": "10:35:40 04-Apr-2025 (RTC)",
    "Running in WAT for": "0 days, 00:13:20",
    "Running since reset": "35 days, 16:25:14",
    "Cell 01 State": "CS_U_E_A",
    "BRC  01 (cab=1,pos=1) State": "BS_U_E_A                      DCKs Downloaded and Class Set"
}
```

## Debugging
If the script does not behave as expected:

Enable real-time Telnet output logging by inspecting the console output by uncommenting this line from the code:

```#child.logfile = sys.stdout.buffer  # Print Telnet output to the console```

Ensure the ```User Name:``` and ```Password:``` prompts match the expected format (e.g., leading spaces).
Adjust the delays ```(time.sleep())``` if the server takes longer to respond.

## Notes
This script is specifically designed for Motorola EBTS Site Controllers and may not work with other devices.
Ensure that the Telnet service is enabled and accessible on the Site Controller.
