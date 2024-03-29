# Generated by Django 4.2.5 on 2023-10-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0017_prescriptionstatus_newprescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Consultation_type', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='reviewofsystem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='medical_history',
            name='consultations',
            field=models.ManyToManyField(to='patientapp.consultation'),
        ),
    ]
