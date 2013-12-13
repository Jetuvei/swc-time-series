#I have totally helped in making this code

"""Module containing TimeSeries and derived objects, as created
for the Glasgow SUPA Software Carpentry course on 12th and 13th 
December 2013.
"""

class TimeSeries(object):
    """TimeSeries object contains a dictionary x keys and 
y values.
"""

    def __init__(self, data):
        """Initialise TimeSeries object
"""
        self.data = data
    
    def get(self, x):
        """Input: x
Output: y
where (x,y) exists in the data
"""
        for xi in self.data.keys():
            if xi == x:
                return self.data[xi] # = yi
        
        raise Exception("Didn't find the value")
    
    def view(self):
        """Not implemented yet!
"""
        pass
    

class StepFunctionTimeSeries(TimeSeries):
    """This time series object allows you to find
the nearest point in the data to the 
specified value. ( see get() )
"""

    def get(self, x):
        """Given an X value, get the corresponding Y value.
        
        Uses step interpolation (gets the Y value of the nearest X point)
"""
        
        closest_point = None
        for xi in self.data.keys():
            if closest_point is None:
                closest_point = (xi, self.data[xi]) # = (xi, yi)
            else:
                cx, cy = closest_point
                if abs(xi-x) < abs(cx-x):
                    closest_point = (xi, self.data[xi])
        return closest_point[1]
        


class LinearTimeSeries(TimeSeries):

    def __init__(self, data):
        """Initialise LinearTimeSeries object
"""
        TimeSeries.__init__(self, data)
        self.data.sort()
    
    def get(self, x):
        """Linearly interpolate between points (x1,y1) and (x2,y2) 
to a point specified by x. Returns the y value 
corresponding to this x. (x,y)
"""
 
	# first need sorted x values
	sorted_x = self.data.keys()
	sorted_x.sort()

	# if it's out of range to the left,
        # return the first value
        if x < sorted_x[0]:
            return self.data[0]
        # if it's out of range to the right,
        # return the last value
        elif x > sorted_x[-1]:
            return self.data[-1]
        # otherwise, it's within the range
        for n, xi in enumerate(sorted_x):
            if xi == x:
                return yi
            elif xi > x and sorted_x[n-1] < x:

                n1, n2 = n-1, n

		x1, x2 = sorted_x[n-1], xi

                y1, y2 = self.data[x1], self.data[x2][1]
                d1, d2 = abs(x-x1), abs(x-x2)
                total_weight = float(d1 + d2)
                w1 = y1 * (total_weight-d1) / total_weight
                w2 = y2 * (total_weight-d2) / total_weight
                return w1 + w2 
