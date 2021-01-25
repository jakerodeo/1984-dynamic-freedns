import time
import argparse
import requests


# Location of 1984's FreeDNS API
UPDATE_URL = "https://api.1984.is/1.0/freedns/?apikey={}&domain={}"


def update(apikey: str, domain: str):
    # Send the update request and return the JSON response
    # See: https://management.1984hosting.com/domains/freednsapi/
    return requests.get(UPDATE_URL.format(apikey, domain)).json()


def parseArguments():
    # Setup argparse with all the arguments needed
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("apikey",
                        help="Your FreeDNS API key")
    parser.add_argument("domain",
                        help="Target domain to update (e.g., \"test.example.com\")")
    parser.add_argument("--interval", type=int, default=300,
                        help="Interval between updates in seconds (default: 300s)")

    return parser.parse_args()


def main() -> None:
    args = parseArguments()

    while True:
        # Output time of update
        print("--- {} ---".format(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())))

        try:
            # Update the record for domain
            response = update(args.apikey, args.domain)
            # Output update status
            print("Response Success: {}".format(response["ok"]))
            print(" -> {}".format(response["msg"]))
            if not response["ok"] and "lookup" in response:
                print(" -> lookup: {}".format(response["lookup"]))
        except Exception as e:
            print("Error while updating: {}".format(e))

        # Sleep until it's time to updat again
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
