# Multi-Platform-Server-Search

This script allows you to search for servers based on a query across three platforms: Shodan, ZoomEye, and Censys. The results from each platform are written to a text file.

## Dependencies
This script requires the requests library. You can install it with pip:

pip install requests
## Usage
First, replace 'your_shodan_api_key', 'your_zoomeye_api_key', 'your_censys_api_id', and 'your_censys_api_secret' with your actual API keys.

To run the script, use:
python multi_platform_search.py
When prompted, enter your query string. The script will then search for hosts related to this query across Shodan, ZoomEye, and Censys.

The results will be written to a file called results.txt in the current directory. The results are written in JSON format, with 4 spaces of indentation for readability.

## Note
This script does not handle errors that might occur if the APIs are not reachable. It also does not handle rate limiting, so if you're planning to use this script heavily, you might want to add some functionality to handle that. It also assumes that each host has a 'product' field, which might not always be the case. Also, the NVD database is quite large, so the requests might take some time.
