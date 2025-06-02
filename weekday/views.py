from django.shortcuts import render, HttpResponse
from .weekday_real import date_to_day
from .forms import RealWeekDay

# Create your views here.
form = RealWeekDay()


def calendar(request):
    if request.method == 'POST':
        form = RealWeekDay(request.POST, request.FILES)
        if form.is_valid():
            year = form.cleaned_data['year']
            year = year.zfill(4)  # Pad the year with trailing zeros if it has less than four digits
            month = form.cleaned_data['month']
            day = form.cleaned_data['day']
            date = f'{year}-{month}-{day}'

            # Do something with the input data
            print(date)
            output = date_to_day(date)
            day_of_the_week = output[0]
            # year outputs
            current_year = output[1][0][0]
            preceeding_years = output[1][0][1]
            preceeding_years_odds= output[1][0][2]
            preceeding_years_odds_short = output[1][0][3]
            # month and day outputs
            current_month = output[1][1][0]
            preceeding_months_odds = output[1][1][1]
            month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            if preceeding_months_odds == [0]:
                preceeding_months_odds = {'Preceeding Months':'Not applicable since it is the first month of the year'}
            else:
                preceeding_months_odds = {month_names[i]: preceeding_months_odds[i] for i in range(len(preceeding_months_odds))}


            current_day = output[1][2][0]
            odd_days_upto_current_day = output[1][2][1]
            # answer_outputs
            total_odd_days = output[1][3][0]
            sum_of_odd_days = output[1][3][1]
            sum_odd_days = output[1][3][2]
            day_of_the_week = output[1][3][3]
            output_str = ' + '.join(str(num) for num in total_odd_days)

            year1_result = f"""<strong>&nbsp;{preceeding_years_odds_short[0]}</strong>"""
            year2_result = f"""<strong>&nbsp;{preceeding_years_odds_short[1]},&nbsp;{preceeding_years_odds_short[2]}</strong>"""
            remaining_odd_days_a = f"""<strong>&nbsp;{preceeding_years_odds_short[1]}</strong>"""
            remaining_odd_days_b = f"""<strong>&nbsp;{preceeding_years_odds_short[2]}</strong>"""
            month_odd_days = f"""<strong>&nbsp;{odd_days_upto_current_day[0]}</strong>""" 






            # display in html
            year_statement = f"""1. 'Year' is {current_year}. <a href="#" data-toggle="tooltip" title="Not including the current year">{preceeding_years} years</a> have passed since the last 
                    <a href="#" data-toggle="tooltip" title="Any year evenly divisible by 400">Century leap year</a>.
                    We separate {preceeding_years} into <a href="#" data-toggle="tooltip" title="Number of centuries passed since the last 'Century leap year'">Completed Centuries</a> and <a href="#" data-toggle="tooltip" title="Number of years passed since last Completed Century">Remaining Years</a>."""
            year_calculation1 = f"""i. No. of odd days in a century is <a href="#" data-toggle="tooltip" title="This is a constant term">5</a>. Thus, 
                      No. of odd-days in <a href="#" data-toggle="tooltip" 
                      title="Number of centuries passed since the last 'Century leap year'">
                      Completed Centuries</a> = {preceeding_years_odds[0]} <a href="#" data-toggle="tooltip" title="Remainder when divided by 7">(mod 7)</a>: {year1_result}"""  
            print(year2_result)          
            year_calculation2 = f"""ii. No. of odd-days in <a href="#" data-toggle="tooltip" title="Number of years passed since last Completed Century">Remaining Years</a> = <a href="#" data-toggle="tooltip" title="Every normal year is assigned 1 odd day">No. of years</a> + <a href="#" data-toggle="tooltip" title="There will be 1 extra odd day each leap year">No. of leap years</a> = {preceeding_years_odds[1]} + {preceeding_years_odds[2] } (mod 7): {remaining_odd_days_a} + {remaining_odd_days_b}"""
            month_statement = f"""2. 'Month' is {month_names[current_month-1]}. Thus, No. of odd-days in <a href="#" data-toggle="tooltip" title="Total number of days in months from January to the month prior to selected month">Completed Months</a> (mod 7):"""
            month_calculation = f"""{preceeding_months_odds}"""
            day_statement = f"""3. 'Day' = {current_day}. No. of odd-days in <a href="#" data-toggle="tooltip" title="No. of days passed this month is the no of odd days this month">current month</a> (mod 7): {month_odd_days}"""
            day_calculation = f"""{odd_days_upto_current_day[0]}"""
            answer_calculation = f"""<a href="#" data-toggle="tooltip" title="Adding all the odd days from 1(i and ii), 2, and 3">Total odd-days</a> = {output_str} = {sum_of_odd_days} (mod 7):"""
            final_answer = f"""Odd days = {sum_odd_days}. This means it's a <a href="#" data-toggle="tooltip" title="0 = Sun, 1 = Mon,...6 = Sat">{day_of_the_week}</a>"""
            result = f"{day_of_the_week}"

    else:
        form = RealWeekDay()
        final_answer, result, year_statement, year_calculation1, year1_result, year_calculation2, year2_result, month_statement, month_calculation, day_statement, day_calculation, answer_calculation  = '', '', 'Select and Submit a date above to view the calculations here.', '', '', '', '', '', '', '', '', ''

    return render(request, 'weekday/calendar.html', {'form': form, 'year_statement':year_statement, 'year_calculation1': year_calculation1, 'year1_result':year1_result, 'year_calculation2':year_calculation2, 'year2_result':year2_result, 'month_statement':month_statement, 'month_calculation':month_calculation, 'day_statement':day_statement, 'day_calculation':day_calculation, 'answer_calculation':answer_calculation, 'result': result, 'final_answer':final_answer})