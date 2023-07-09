class Solution:
    @staticmethod
    def salary_calculator(days):
        """"
        Jeevitha just started work as a programming trainer for UIT's Placement Cell. She is paid Rs.100 an hour, with a few exceptions. She earns an extra Rs.15 an hour for any part of a day where she works more than 8 hours, and an extra Rs.25 an hour for hours beyond 40 in any one week. Also, she earns a 25% bonus for working on Saturday and a 50% bonus for working on Sunday. The bonuses for Saturday and Sunday are computed based on the hours worked those days; they are not used to calculate any bonus for working more than 40 hours in a week. You'll be given the number of hours Jeevitha worked on each day in a week (Sunday, Monday, ..., Saturday), and you need to compute her salary for the week. Input consists of 7 integers less than or equal to 24 on separate lines. Print Jeevitha's weekly salary as output.
        """
        tot_hours=0
        salary=0
        for i in range(7):
            tot_hours+=days[i]
            salary+=(days[i]*100)
            if i==0: salary+=(50*days[i])
            if i==6: salary+=(25*days[i])
            if days[i]>8:
                rem_hrs=days[i]-8
                salary+=(15*rem_hrs)
        if tot_hours>40:
            salary+=(tot_hours-40)*25

        return salary

if __name__ == '__main__':
    s=Solution()
    print(s.salary_calculator([0,8,8,8,10,6,0]))
    print(s.salary_calculator([4,5,0,8,0,6,0]))
    print(s.salary_calculator([5,3,6,1,1,2,3]))