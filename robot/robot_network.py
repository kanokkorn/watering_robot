import urllib.request


def internet_on():
    try:
        urllib.request.urlopen("https://google.com", timeout=0.5)
        print("Yay! Network is working normally.")
        return True
    except urllib.request.URLError as err:
        raise Exception("NO! Something's wrong with network")
        return False


if __name__ == "__main__":

    internet_on()
    pass
