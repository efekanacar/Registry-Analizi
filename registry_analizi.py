import winreg

key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
    for i in range(1024):
        try:
            subkey_name = winreg.EnumKey(key, i)
            subkey_path = key_path + "\\" + subkey_name
            print("Subkey:", subkey_path)
            
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as subkey:
                for j in range(1024):
                    try:
                        name, value, type_ = winreg.EnumValue(subkey, j)
                        print("Value Name:", name)
                        print("Value Data:", value)
                        print("Value Type:", type_)
                    except OSError:
                        break
        except OSError:
            break