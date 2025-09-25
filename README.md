# Vehicle Service Registration Project

This project is designed to manage vehicle service registrations efficiently. It includes modules for customer and vehicle management, service booking and registration, service type and package management, and image and audio capture.

## Project Structure

- **manage.py**: A command-line utility that lets you interact with this Django project.
- **vehicle_service_registration/**: The main project directory containing settings and configuration files.
  - **settings.py**: Configuration settings for the Django project.
  - **urls.py**: URL declarations for the project.
  - **wsgi.py**: WSGI configuration for deployment.
  - **asgi.py**: ASGI configuration for asynchronous deployment.
- **customers/**: Module for managing customer information.
  - **models.py**: Database models for customers.
  - **views.py**: Views for handling customer-related requests.
  - **urls.py**: URL routing for customer-related views.
  - **templates/**: HTML templates for customer forms.
- **vehicles/**: Module for managing vehicle information.
  - **models.py**: Database models for vehicles.
  - **views.py**: Views for handling vehicle-related requests.
  - **urls.py**: URL routing for vehicle-related views.
  - **templates/**: HTML templates for vehicle forms.
- **services/**: Module for managing service bookings.
  - **models.py**: Database models for services.
  - **views.py**: Views for handling service-related requests.
  - **urls.py**: URL routing for service-related views.
  - **templates/**: HTML templates for service forms.
- **service_types/**: Module for managing service types and packages.
  - **models.py**: Database models for service types.
  - **views.py**: Views for handling service type-related requests.
  - **urls.py**: URL routing for service type-related views.
  - **templates/**: HTML templates for service type forms.
- **media/**: Directory for storing uploaded images and audio files.
  - **images/**: Subdirectory for images.
  - **audio/**: Subdirectory for audio recordings.
- **static/**: Directory for static files (CSS, JavaScript, images).
  - **css/**: Directory for CSS files.
  - **js/**: Directory for JavaScript files.
  - **images/**: Directory for static images.

## Features

- **Customer Management**: Add, edit, and delete customer information.
- **Vehicle Management**: Manage vehicle details associated with customers.
- **Service Booking**: Book services for vehicles and manage service records.
- **Service Type Management**: Define and manage different types of services and packages.
- **Image & Audio Capture**: Capture images and audio recordings during service registration.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd vehicle_service_registration
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Run the migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Follow the navigation buttons to manage customers, vehicles, services, and service types.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the @ Ela Solutions License. See the LICENSE file for details.# Vehicle_Service_Registration

# Vehicle_Service_Registration
