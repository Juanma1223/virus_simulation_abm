# Virus Spreading Simulation

## Overview

The **Virus Spreading Simulation** models the spread of a virus within a simulated environment consisting of various devices, routers and buildings. It helps visualize and analyze the impact of a virus outbreak in a controlled digital setting.

## Features

- **Device Interaction:** Simulates virus spread through various devices like computers, phones, and IoT devices.
- **Building Networks:** Models the interaction of devices within buildings.
- **Statistical Analysis:** Provides data on the spread.
- **Configurable Simulations:** Users can customize the simulation parameters using a JSON input file.

## Directory Structure

```
Virus-Spreading-Simulation/
├── input.json                # Configuration file for the simulation
├── LICENSE                   # License information
└── src/                      # Source code directory
    ├── classes/              # Contains class definitions
    │   ├── building.py       # Defines buildings and their properties
    │   ├── device/           # Directory for device-related classes
    │   │   ├── computer.py   # Class for computer devices
    │   │   ├── device.py     # Base class for all devices
    │   │   ├── iot.py        # Class for IoT devices
    │   │   ├── phone.py      # Class for phone devices
    │   │   └── __pycache__/  # Compiled Python files (auto-generated)
    │   ├── router.py         # Router class to manage network routing
    │   └── virus.py          # Virus class to simulate infection dynamics
    ├── main.py               # Main script to run the simulation
    ├── simulation.py         # Simulation logic and control
    └── stats.py              # Statistical analysis and reporting
```

## Getting Started

### Prerequisites

- Python 3.10 or above

### Running the Simulation

1. Configure the `input.json` file with your desired simulation parameters.
2. Run the main script:

   ```bash
   python src/main.py
   ```

### Configuration

The `input.json` file should follow this structure:

```json
{
    "buildings": [
        {
            "name": "Sales department",
            "routers": [
                {
                    "devices": [
                        {
                            "name": "Phone 1",
                            "type": 2,
                            "virus": true,
                            "securityLevel": 1
                        },
                        {
                            "name": "Computer 1",
                            "type": 1,
                            "virus": false,
                            "securityLevel": 1
                        }
                    ],
                    "firewall": true,
                    "virus": false
                },
                {
                    "devices": [
                        {
                            "name": "Computer 2",
                            "type": 1,
                            "virus": false,
                            "securityLevel": 1
                        },
                        {
                            "name": "Computer 3",
                            "type": 1,
                            "virus": false,
                            "securityLevel": 1
                        },
                        {
                            "name": "Computer 4",
                            "type": 1,
                            "virus": false,
                            "securityLevel": 1
                        }
                    ],
                    "firewall": true,
                    "virus": false
                }
            ],
            "isCompany": false
        },
        {
            "name": "Engineering department",
            "routers": [
                {
                    "devices": [
                        {
                            "name": "Phone 1",
                            "type": 2,
                            "virus": true,
                            "securityLevel": 1
                        },
                        {
                            "name": "Computer 1",
                            "type": 1,
                            "virus": false,
                            "securityLevel": 1
                        }
                    ],
                    "firewall": true,
                    "virus": false
                },
                {
                    "devices": [
                        {
                            "name": "Computer 2",
                            "type": 1,
                            "virus": false,
                            "securityLevel": 1
                        },
                        {
                            "name": "Computer 3",
                            "type": 1,
                            "virus": false,
                            "securityLevel": 1
                        },
                        {
                            "name": "Computer 4",
                            "type": 1,
                            "virus": false,
                            "securityLevel": 1
                        }
                    ],
                    "firewall": true,
                    "virus": false
                }
            ],
            "isCompany": false
        }
    ],
    "virus": {
        "name": "Trojan",
        "sentByMail": true,
        "sentByMessage": true,
        "networkPropagation": true,
        "selfReplicating": true
    },
    "steps": 10000
}
```

### Output

The simulation generates logs and statistical data in logs.txt and stats.txt

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution

Feel free to fork the project and submit pull requests. Contributions are welcome!

## Author

Juan Manuel Fernandez
