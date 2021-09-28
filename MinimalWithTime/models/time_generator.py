import datetime

"""
This class has one public static method:  get_curr_datetime()
"""

class TimeGenerator:
    """
    :returns: current date time as a string:  HR:MIN:SEC YYYY MM DD
    """
    @staticmethod
    def get_curr_datetime():
        return datetime.datetime.now().strftime("%H:%M:%S %Y %m %d")
