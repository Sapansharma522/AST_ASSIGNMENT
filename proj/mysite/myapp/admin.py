# admin.py
# admin.py
# admin.py
from django.contrib import admin
from .models import Job
import numpy as np

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'extractedSalary', 'jobLocationCity')
    search_fields = ('title', 'company', 'jobLocationCity')
    actions = ['display_average_salary']

    def display_average_salary(self, request, queryset):
        # Get the extracted salaries for selected jobs
        extracted_salaries = [job.extractedSalary for job in queryset if job.extractedSalary is not None]

        # Calculate the average salary using NumPy
        average_salary = np.mean(extracted_salaries) if extracted_salaries else None

        # Display a message in the admin panel
        if average_salary is not None:
            self.message_user(request, f'Average Salary for selected jobs: {average_salary:.2f}')
        else:
            self.message_user(request, 'No valid salary data available for calculation.')

    display_average_salary.short_description = "Display Average Salary"

admin.site.register(Job, JobAdmin)

