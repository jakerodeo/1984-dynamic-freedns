# 1984 Dynamic FreeDNS
This is a simple script to update your A records on 1984's FreeDNS service.

## Usage
First, we need the `requests` library in order to talk to 1984's FreeDNS API:

    pip install -r requirements.txt

Second, we need an API key from FreeDNS. You can obtain your API key by visiting
[this page](https://management.1984hosting.com/domains/freednsapi/).

Now that we obtained the dependencies for the code and the API key, we can
update our domain by running the following command and supplementing the actual
API key and domain in the parameters:

    python dynamic-freedns.py "apikey" "domain.com"

This will run continuously, updating the domain every 5 minutes by default.
The 5 minute interval can be changed by specifying an additional parameter
by adding `--interval 300`, where 300 is the number of seconds between updates.
