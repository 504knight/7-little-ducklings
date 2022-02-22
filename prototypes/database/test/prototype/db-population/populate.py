from dbtest.models import User, Job, Review
from django.db import connection

#Delete existing test records from database tables

cursor = connection.cursor()
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM jobs")
cursor.execute("DELETE FROM reviews")

#Insert test data
for i in range(10):
    testUser = User(password="testpassword", first_name="Test" + str(i), last_name="User"+str(i), username= "testuser"+str(i),email="testemail@mail.com",balance=0.00, is_active=True)
    testUser.save()

User.objects.all()
