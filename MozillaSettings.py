import re

class MozillaSettings:
    """Class for CRUD operations for Mozilla prefs.js file"""

    def __init__(self, file):
        self.file = file
        try:
            file_object = open(self.file, "rt", encoding="utf-8")
            file_object.close()
        except:
            print("Cannot open file:", file)
        

    def add_or_update_key(self, key, value):
        """Add or update key from file. Example for value: true, 123, \"test\" """
        if self.read_key(key) is None:
            # Add to file
            with open(self.file, "at", encoding="utf-8") as file_object:
                file_object.write( '\nuser_pref("{0}", {1});'.format(key,value) )
                return
        else:
            # Update in file
            file_object = open(self.file, "rt", encoding="utf-8")
            output = ""

            for line in file_object.readlines():
                value_regex = re.search(r'^user_pref\(\s*"{0}"\s*,\s*("?.*)"?\);\s*$'.format(key.lower()), line.strip().lower())
                if value_regex:
                    output += re.sub(value_regex.group(1), value, line)
                else:
                    output += line
            file_object.close()
            file_object = open(self.file, "w", encoding="utf-8")
            file_object.write(output)
            file_object.close()


    def read_key(self, key):
        """Read value from file. If not exist return None"""
        file_object = open(self.file, "rt", encoding="utf-8")
        
        for line in file_object.readlines():
            value_regex = re.search(r'^user_pref\(\s*"{0}"\s*,\s*("?.*)"?\);\s*$'.format(key.lower()), line.strip().lower())
            if value_regex:
                file_object.close()
                return str(value_regex.group(1))
        file_object.close()
        return None


    def delete_key(self, key):
        """Delete key,value from file"""
        file_object = open(self.file, "rt", encoding="utf-8")
        output = ""

        for line in file_object.readlines():
            value_regex = re.search(r'^user_pref\(\s*"{0}"\s*,\s*("?.*)"?\);\s*$'.format(key.lower()), line.strip().lower())
            if value_regex:
                pass
            else:
                output += line
        file_object.close()
        file_object = open(self.file, "w", encoding="utf-8")
        file_object.write(output)
        file_object.close()        