from MozillaSettings import MozillaSettings


def main():
    m = MozillaSettings('./prefs.js')
    m.add_or_update_key('browser.startup.homepage', '"www.slo-tech.com"')
    print(m.read_key('browser.startup.homepage'))
    #m.delete_key("browser.startup.homepage")


if __name__ == "__main__":
    main()