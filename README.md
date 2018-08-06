# Mozilla-Settings
Python class for changing settings directly in prefs.js for Mozilla Firefox and Thunderbird



Example:
```python
m = MozillaSettings('./prefs.js')

# Add or change current home page in Mozilla Firefox
m.add_or_update_key('browser.startup.homepage', '"www.slo-tech.com"')

# Get current home page
print(m.read_key('browser.startup.homepage'))

# Delete key
m.delete_key("browser.startup.homepage")
```
