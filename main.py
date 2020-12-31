import pandas
monthly_earnings_goal = int(input("What is your monthly earnings goal? \n"))
vehicle_price = 500000
initial_savings = int(input("How much of your savings will go into this? \n"))
earnings_per_vehicle = int(input("How much will you expect monthly per vehicle \n"))
number_of_vehicles = 0
months_elapsed = 0
monthly_earnings = 0

my_data = []


def get_elapsed_time(_earnings):
	"""Returns elapsed time in months"""
	return round(vehicle_price / (initial_savings + _earnings))


while monthly_earnings < monthly_earnings_goal:
	earnings = earnings_per_vehicle * number_of_vehicles
	monthly_earnings = earnings
	elapsed = get_elapsed_time(earnings)
	months_elapsed += elapsed
	data = {"vehicles": number_of_vehicles, "Months": months_elapsed, "Earnings": monthly_earnings}
	my_data.append(data)
	number_of_vehicles += 1

df = pandas.DataFrame(my_data)

print(f"You'll have to wait ~{round(months_elapsed/12) + 1} years")
print(df)
