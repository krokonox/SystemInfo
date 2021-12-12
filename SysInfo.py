import wmi
import ctypes
import json

class SystemInfoRetreiver:
    wmi = wmi.WMI() 

    def getComponentInfo(self, query):
        query = "SELECT * FROM " + query
        info = []
        for x in self.wmi.query(query):
            info.append(x)
        return info

    def getWindowsStartupTime(self):
        lib = ctypes.windll.kernel32
 
        t = lib.GetTickCount64()
 
        # since the time is in milliseconds i.e. 1000 * seconds
        # therefore truncating the value
        t = int(str(t)[:-3])
 
        mins, sec = divmod(t, 60)
        hour, mins = divmod(mins, 60)
        days, hour = divmod(hour, 24)
 
        return f"{days} days, {hour:02}:{mins:02}:{sec:02}"

    def getSystemInfoData(self):
        data = {}

        data["monitor"] = self.getComponentInfo("Win32_DesktopMonitor")
        data["cpu"] = self.getComponentInfo("Win32_Processor")
        data["keyboard"] = self.getComponentInfo("Win32_Keyboard")
        data["motherboard"] = self.getComponentInfo("Win32_BaseBoard")
        data["mouse"] = self.getComponentInfo("Win32_PointingDevice")
        data["network"] = self.getComponentInfo("Win32_NetworkAdapter")
        data["bios"] = self.getComponentInfo("Win32_BIOS")
        data["startupTime"] = self.getWindowsStartupTime


        return data
