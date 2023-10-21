import java.util.Scanner;

public class exp4q4 {
    public static void main(String[] args) {
        // Get the entered date from the user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a date (YYYY-MM-DD): ");
        String dateString = scanner.nextLine();
        scanner.close();

        // Parse the entered date
        int enteredYear = Integer.parseInt(dateString.substring(0, 4));
        int enteredMonth = Integer.parseInt(dateString.substring(5, 7));
        int enteredDay = Integer.parseInt(dateString.substring(8, 10));

        // Calculate the number of days between January 1, 1980, and the entered date
        int startYear = 1980;
        int startMonth = 1;
        int startDay = 1;

        int days = calculateDays(startYear, startMonth, startDay, enteredYear, enteredMonth, enteredDay);

        // Display the result
        System.out.println("Number of days between January 1, 1980, and " + dateString + ": " + days);
    }

    private static boolean isLeapYear(int year) {
        return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
    }

    private static int getDaysInMonth(int year, int month) {
        int[] daysInMonth = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        if (month == 2 && isLeapYear(year)) {
            return 29;
        }
        return daysInMonth[month - 1];
    }

    private static int calculateDays(int startYear, int startMonth, int startDay, int endYear, int endMonth,
            int endDay) {
        int days = 0;

        // Calculate days for each year
        for (int year = startYear; year < endYear; year++) {
            days += isLeapYear(year) ? 366 : 365;
        }

        // Calculate days for each month
        for (int month = 1; month < endMonth; month++) {
            days += getDaysInMonth(endYear, month);
        }

        // Add remaining days in the endMonth
        days += endDay;

        // Subtract days for each month before startMonth
        for (int month = 1; month < startMonth; month++) {
            days -= getDaysInMonth(startYear, month);
        }

        // Subtract remaining days in the startMonth
        days -= startDay;

        return days;
    }
}