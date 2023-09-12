class Appointment:
    def __init__(self, date, time, description):
        self.date = date
        self.time = time
        self.description = description


class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, date, time, description):
        appointment = Appointment(date, time, description)
        self.appointments.append(appointment)

    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("Scheduled Appointments:")
            for idx, appointment in enumerate(self.appointments, start=1):
                print(
                    f"{idx}. Date: {appointment.date}, Time: {appointment.time}, Description: {appointment.description}")


def main():
    scheduler = AppointmentScheduler()

    while True:
        print("\nAppointment Scheduler")
        print("1. Schedule Appointment")
        print("2. View Appointments")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            description = input("Enter appointment description: ")
            scheduler.schedule_appointment(date, time, description)
            print("Appointment scheduled successfully!")
        elif choice == "2":
            scheduler.view_appointments()
        elif choice == "3":
            print("Exiting the appointment scheduler.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
