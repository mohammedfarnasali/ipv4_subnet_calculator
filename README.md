# ipv4_subnet_calculator
An IPv4 Subnet Calculator built with Python's Tkinter. This tool allows users to input an IP address in CIDR notation and provides the network address, broadcast address, usable host range, subnet mask, and IP class. It features a user-friendly GUI and handles input validation effectively.

# Features
IP Address and CIDR Notation Input: Users can enter an IP address along with its CIDR notation.
Network Address Calculation: Determines the network address of the provided IP and CIDR.
Broadcast Address Calculation: Calculates the broadcast address for the given network.
Usable Host Range: Displays the range of usable IP addresses within the subnet.
Subnet Mask Calculation: Computes the subnet mask corresponding to the CIDR notation.
IP Class Determination: Identifies the class (A, B, C, D, E) of the entered IP address.

# How to Use
Enter IP Address/CIDR: Input the IP address in the format xxx.xxx.xxx.xxx/xx in the provided text box.
Calculate: Click on the "Calculate" button to view the results.
View Results: The calculated network address, broadcast address, usable host range, subnet mask, and IP class will be displayed.

# Sample Output
![Screenshot 2024-06-08 194317](https://github.com/user-attachments/assets/2204c39f-b2cd-4edd-8bf2-df618fc7dff6)
![Screenshot 2024-06-08 194414](https://github.com/user-attachments/assets/b2ffce47-a182-4258-8c9c-4b4ab7cd0202)

# Code Overview
The main components are:

Tkinter Setup: Creates the main window and sets the title, dimensions, and labels.

Entry Field: A text box for user input.
Calculation Functions:

calculate(): Handles the main logic for parsing the input and performing calculations.

net_add(ip): Calculates the network address.

broadcast_add(net): Calculates the broadcast address.

host_range(net): Calculates the range of usable IP addresses.
subnetmask(cidr): Computes the subnet mask.
ipclass(ip): Determines the IP class.
Result Display: Functions to display the results in the Tkinter window.
Clear Function: Clears previous results when a new calculation is performed.



