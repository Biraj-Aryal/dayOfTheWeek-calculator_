from datetime import datetime

def date_to_day(date_string, verbose=False):
    date = datetime.strptime(date_string, '%Y-%m-%d')
    day = date.day
    month = date.month
    year = date.year-1

    def extract_odd_from_Century(Year):
        # Handle previous centuries
        if verbose == True:
            print('Year: ', Year+1)
        if year >= 400:
            remainderYear = year % 400
        else:
            remainderYear = year
        if verbose:
            print(remainderYear)
        # Handle the current century
        if remainderYear == 300:
            if verbose:
                print(1)
            total_odd_from_years = [15, 0] 
        elif remainderYear > 300:
            if verbose:
                print(2)
            total_odd_from_years = [15, remainderYear - 300] 
        elif remainderYear == 200: 
            if verbose:
                print(3)
            total_odd_from_years = [10, 0]
        elif remainderYear > 200:
            if verbose:
                print(4)
            total_odd_from_years = [10, remainderYear - 200] 
        elif remainderYear == 100:
            if verbose:
                print(5)
            total_odd_from_years = [5, 0] 
        elif remainderYear > 100:
            if verbose:
                print(6)
            total_odd_from_years = [5, remainderYear - 100]    
        else:
            total_odd_from_years = [0, remainderYear]  
            if verbose:
                print(0) 

        if total_odd_from_years[1] >= 4:
            leapYear_odds_from_this_century = total_odd_from_years[1]//4  # second term is for the extra odd days in leap years
        else:
            leapYear_odds_from_this_century = 0
        total_odd_from_years.append(leapYear_odds_from_this_century)

        total_odd_from_years_short = [i%7 for i in total_odd_from_years]
        return Year+1, remainderYear, total_odd_from_years, total_odd_from_years_short

    def extract_odd_from_month(Month):
        if (year+1)%100 == 0:  
            if (year+1)%400 == 0: 
                month_odd_formula = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
            else:
                month_odd_formula = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
        elif (year+1)%4 == 0:
            month_odd_formula = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
        else:
            month_odd_formula = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
        
        previous_month = Month - 1
        if previous_month >= 1: 
            relevant_months = month_odd_formula[:previous_month]
        else:
            relevant_months = [0]
        return Month, relevant_months

    def extract_odd_from_day(Day):
        if Day >= 7:
            days = Day%7
        else:
            days = Day
        return Day, [days] 

    def odd_days_to_weekDay(odd_days):
        if odd_days == 0:
            day = 'Sunday'
        if odd_days == 1:
            day = 'Monday'
        if odd_days == 2:
            day = 'Tuesday'
        if odd_days == 3:
            day = 'Wednesday'
        if odd_days == 4:
            day = 'Thursday'
        if odd_days == 5:
            day = 'Friday'
        if odd_days == 6:
            day = 'Saturday'
        return day

    # step 1: Handling Preceeding Years since last leap century: 
    current_year, preceeding_years, preceeding_years_odds, preceeding_years_odds_short = extract_odd_from_Century(year)
    if verbose:
        print(f"Year: {current_year}")
        print(f"=> Preceeding Years since last leap century: {preceeding_years}") 
        print(f"=> Total odd-days in preceeding years:=> {preceeding_years_odds} => {preceeding_years_odds_short}")

    # step 2: Handling Preceeding Months in current month: 
    current_month, preceeding_months_odds = extract_odd_from_month(month)
    if verbose:
        print(f"Month: {current_month}")
        print(f"=> Total odd-days in preceeding months:=> {preceeding_months_odds}")

    # step 3: Handling Current Month
    current_day, odd_days_upto_current_day = extract_odd_from_day(day)
    if verbose:
        print(f"Day: {current_day}")
        print(f"=> Total odd-days in current month so far:=> {odd_days_upto_current_day[0]}")

    # step 4: Total odd days
    if preceeding_months_odds == [0]:
        total_odd_days = preceeding_years_odds_short + odd_days_upto_current_day
    else:
        total_odd_days = preceeding_years_odds_short + preceeding_months_odds + odd_days_upto_current_day
    if preceeding_years_odds_short[0] == 0:
        total_odd_days = total_odd_days[1:]

    
    sum_of_odd_days = sum(total_odd_days)
    if sum(total_odd_days) >= 7:
        sum_odd_days = sum(total_odd_days)%7
    else:
        sum_odd_days = sum(total_odd_days)
    day_of_the_week = odd_days_to_weekDay(sum_odd_days)
    if verbose:
        print(f"Toal odd days:=> {total_odd_days}=> {sum_of_odd_days} => {sum_odd_days} => {day_of_the_week}")

        # necessary print outputs:
    year_outputs = [current_year, preceeding_years, preceeding_years_odds, preceeding_years_odds_short]
    month_outputs = [current_month, preceeding_months_odds]
    day_outputs = [current_day, odd_days_upto_current_day]
    answer_outputs = [total_odd_days, sum_of_odd_days, sum_odd_days, day_of_the_week]
    all_outputs = [year_outputs, month_outputs, day_outputs, answer_outputs]
    return day_of_the_week, all_outputs


if __name__ == '__main__':
    date = '0001-2-28'
    print(date_to_day(date))


