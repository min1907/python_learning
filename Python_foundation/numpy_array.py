# Practice with NumPy arrays
# Let's practice slicing numpy arrays and using NumPy's broadcasting concept. Remember, broadcasting refers to a numpy array's ability to vectorize operations, so they are performed on all elements of an object at once.
# A two-dimensional numpy array has been loaded into your session (called nums) and printed into the console for your convenience. numpy has been imported into your session as np.
# import numpy as np
# nums = np.array([[1 ,2 ,3 ,4 ,5], [ 6 ,7 ,8 ,9 ,10]])
# print(nums)

# # Print second row of nums
# print(nums[1,:])

# # Print all elements of nums that are greater than six
# print(nums[nums > 6])

# # Double every element of nums
# nums_dbl = nums * 2
# print(nums_dbl)

# # Replace the third column of nums
# nums[:,2] = nums[:,2] + 1
# print(nums)


#########################################################
# Bringing it all together
import numpy as np

names = ["Jerry", "Kramer", "Elaine", "George", "Newman"]

# Create a list of arrival times (unpack a contents into a list using star character)
arrival_times = [*range(10, 60, 10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[name], time) for name, time in enumerate(new_times)]

print(guest_arrivals)

#
def welcome_guest(guest_and_time):
    """
    Returns a welcome string for the guest_and_time tuple.

    Args:
        guest_and_time (tuple): The guest and time tuple to create
            a welcome string for.

    Returns:
        welcome_string (str): A string welcoming the guest to Festivus.
        'Welcome to Festivus {guest}... You're {time} min late.'

    """
    guest = guest_and_time[0]
    arrival_time = guest_and_time[1]
    welcome_string = "Welcome to Festivus {}... You're {} min late.".format(
        guest, arrival_time
    )
    return welcome_string


welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep="\n")
