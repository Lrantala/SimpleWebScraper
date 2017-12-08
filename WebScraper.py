import requests


def get_website_contents():
    """This function retrieves and returns the contents of the
    website that is passed to it as an argument."""
    website = requests.get("http://www.darklyrics.com/lyrics/kingdiamond/abigail.html")
    try:
        website.raise_for_status()
    except Exception as exception:
        print("Error encountered: %s" % exception)
    return website.content


def write_website_to_file(contents):
    """This function writes the website contents to a file
    as bytes."""
    write_contents_bytes = bytearray(contents)
    try:
        with open("Abigail.txt", "wb") as file:
            file.write(write_contents_bytes)
    except IOError as exception:
        print("Couldn't save the file. Encountered an error: %s" % exception)


if __name__ == "__main__":
    print("teretere")